#!/usr/bin/env pwsh
# Script to rebuild Presidio Analyzer with new Australian custom recognizers
# RUN THIS AT HOME (not on corporate network due to SSL inspection)

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "PRESIDIO ANALYZER - REBUILD INSTRUCTIONS" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "New recognizers added:" -ForegroundColor Yellow
Write-Host "  ? AU_BSB - Australian Bank State Branch codes" -ForegroundColor Green
Write-Host "  ? AU_POLICY_NUMBER - Insurance policy numbers" -ForegroundColor Green  
Write-Host "  ? AU_ACCOUNT_NUMBER - Bank account numbers" -ForegroundColor Green

Write-Host "`nModified files:" -ForegroundColor Yellow
Write-Host "  - presidio_analyzer/predefined_recognizers/country_specific/australia/au_bsb_recognizer.py (NEW)" -ForegroundColor White
Write-Host "  - presidio_analyzer/predefined_recognizers/country_specific/australia/au_policy_recognizer.py (NEW)" -ForegroundColor White
Write-Host "  - presidio_analyzer/predefined_recognizers/country_specific/australia/au_account_recognizer.py (NEW)" -ForegroundColor White
Write-Host "  - presidio_analyzer/predefined_recognizers/country_specific/australia/__init__.py (UPDATED)" -ForegroundColor White
Write-Host "  - presidio_analyzer/predefined_recognizers/__init__.py (UPDATED)" -ForegroundColor White
Write-Host "  - presidio_analyzer/conf/default_recognizers.yaml (UPDATED)" -ForegroundColor White

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "STEP 1: REBUILD DOCKER IMAGE" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "This will take ~5 minutes. DO NOT CANCEL.`n" -ForegroundColor Yellow

Write-Host "Command:" -ForegroundColor White
Write-Host "  docker build -t presidio-analyzer-au:latest ./presidio-analyzer`n" -ForegroundColor Cyan

$confirmation = Read-Host "Start build now? (y/n)"
if ($confirmation -eq 'y') {
    Write-Host "`nBuilding..." -ForegroundColor Yellow
    docker build -t presidio-analyzer-au:latest ./presidio-analyzer
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n? Build successful!" -ForegroundColor Green
        
        Write-Host "`n========================================" -ForegroundColor Cyan
        Write-Host "STEP 2: RESTART CONTAINER" -ForegroundColor Cyan
        Write-Host "========================================`n" -ForegroundColor Cyan
        
        Write-Host "Stopping old container..." -ForegroundColor Yellow
        docker rm -f presidio-analyzer
        
        Write-Host "Starting new container..." -ForegroundColor Yellow
        docker run -d -p 5002:3000 -e PORT=3000 -e WORKERS=1 --name presidio-analyzer --entrypoint "/bin/sh" presidio-analyzer-au:latest /app/entrypoint.sh
        
        Write-Host "Waiting 25 seconds for startup..." -ForegroundColor Yellow
        Start-Sleep -Seconds 25
        
        Write-Host "`n========================================" -ForegroundColor Cyan
        Write-Host "STEP 3: TEST NEW RECOGNIZERS" -ForegroundColor Cyan
        Write-Host "========================================`n" -ForegroundColor Cyan
        
        # Test 1: BSB Number
        Write-Host "Test 1: BSB Number (654-654)" -ForegroundColor Yellow
        $test1 = @{text='My BSB is 654-654 for the account'; language='en'} | ConvertTo-Json -Compress
        $result1 = curl.exe -X POST http://localhost:5002/analyze -H 'Content-Type: application/json' -d $test1 | ConvertFrom-Json
        $bsbDetected = $result1 | Where-Object { $_.entity_type -eq 'AU_BSB' }
        if ($bsbDetected) {
            Write-Host "  ? BSB detected (score: $($bsbDetected.score))" -ForegroundColor Green
        } else {
            Write-Host "  ? BSB NOT detected" -ForegroundColor Red
        }
        
        # Test 2: Policy Number
        Write-Host "`nTest 2: Policy Number (118U524989BPK)" -ForegroundColor Yellow
        $test2 = @{text='Policy number 118U524989BPK is active'; language='en'} | ConvertTo-Json -Compress
        $result2 = curl.exe -X POST http://localhost:5002/analyze -H 'Content-Type: application/json' -d $test2 | ConvertFrom-Json
        $policyDetected = $result2 | Where-Object { $_.entity_type -eq 'AU_POLICY_NUMBER' }
        if ($policyDetected) {
            Write-Host "  ? Policy detected (score: $($policyDetected.score))" -ForegroundColor Green
        } else {
            Write-Host "  ? Policy NOT detected" -ForegroundColor Red
        }
        
        # Test 3: Account Number
        Write-Host "`nTest 3: Account Number (6546546)" -ForegroundColor Yellow
        $test3 = @{text='Account number 6546546 for BSB 654-654'; language='en'} | ConvertTo-Json -Compress
        $result3 = curl.exe -X POST http://localhost:5002/analyze -H 'Content-Type: application/json' -d $test3 | ConvertFrom-Json
        $accountDetected = $result3 | Where-Object { $_.entity_type -eq 'AU_ACCOUNT_NUMBER' }
        if ($accountDetected) {
            Write-Host "  ? Account detected (score: $($accountDetected.score))" -ForegroundColor Green
        } else {
            Write-Host "  ? Account NOT detected" -ForegroundColor Red
        }
        
        # Test 4: Combined test with all patterns
        Write-Host "`nTest 4: Combined Australian data" -ForegroundColor Yellow
        $test4 = @{text='Policy 118U524989BPK, BSB: 654-654, Account: 6546546, TFN: 123456782'; language='en'} | ConvertTo-Json -Compress
        $result4 = curl.exe -X POST http://localhost:5002/analyze -H 'Content-Type: application/json' -d $test4 | ConvertFrom-Json
        Write-Host "`nAll detected entities:" -ForegroundColor Cyan
        $result4 | Sort-Object -Property start | ForEach-Object {
            Write-Host "  - $($_.entity_type.PadRight(25)) (score: $($_.score))" -ForegroundColor Green
        }
        
        Write-Host "`n========================================" -ForegroundColor Cyan
        Write-Host "STEP 4: SAVE IMAGE (OPTIONAL)" -ForegroundColor Cyan
        Write-Host "========================================`n" -ForegroundColor Cyan
        
        Write-Host "To transfer back to corporate network:`n" -ForegroundColor Yellow
        Write-Host "  docker save presidio-analyzer-au:latest | gzip > presidio-analyzer-au.tar.gz" -ForegroundColor Cyan
        Write-Host "`nThen at work:" -ForegroundColor Yellow
        Write-Host "  docker load -i presidio-analyzer-au.tar.gz" -ForegroundColor Cyan
        
    } else {
        Write-Host "`n? Build failed! Check error above." -ForegroundColor Red
        Write-Host "Make sure you're at home (not on corporate network)" -ForegroundColor Yellow
    }
} else {
    Write-Host "`nBuild cancelled. When ready, run:" -ForegroundColor Yellow
    Write-Host "  .\rebuild_at_home.ps1" -ForegroundColor Cyan
}
