# Australian Broker Remittance Data - PII Detection Testing

This file contains curl commands to test PII detection with your actual broker remittance JSON files.

**Location:** `c:\new project\others'\broker remittance\`

**Prerequisites:**

- Analyzer container running: `docker ps | Select-String presidio-analyzer-au`
- Anonymizer container running: `docker ps | Select-String presidio-anonymizer-au`
- PowerShell on Windows

---

## Test 1: PSC Network Remittance ($7,876.55)

**File:** `$7,876.55 PSC.json`

**Contains:**

- Policy Numbers: 47-ZBC-000361, BZF2024736, LPS019877447-11886, BZF2024547
- ABN: 23 141 574 914
- Business names and addresses
- Account numbers

### Analyze

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"PSC NETWORK Policy 47-ZBC-000361 for DIDEAN PTY LTD ABN 23 141 574 914. Policy BZF2024736 for Inscope Plumbing Group. Policy LPS019877447-11886 for SMARTTECH CONSULTANCY SERVICES. Policy BZF2024547 for BMP TAXATION SERVICES PTY LTD. Level 7, 35 Collins Street Melbourne VIC 3000. Tel: (03) 9862 6550. Email: info@pscconnect.com.au. Reference: PSCNNORTHERN Account No: 0291162\", \"language\": \"en\"}'
```

**Expected Entities:**

- AU_POLICY_NUMBER (4 detections): 47-ZBC-000361, BZF2024736, LPS019877447-11886, BZF2024547
- AU_ABN: 23 141 574 914
- PHONE_NUMBER: (03) 9862 6550
- EMAIL_ADDRESS: info@pscconnect.com.au
- LOCATION: Melbourne
- AU_ACCOUNT_NUMBER: 0291162

### Anonymize

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"PSC NETWORK Policy 47-ZBC-000361 for DIDEAN PTY LTD ABN 23 141 574 914. Policy BZF2024736 for Inscope Plumbing Group. Policy LPS019877447-11886 for SMARTTECH CONSULTANCY SERVICES. Policy BZF2024547 for BMP TAXATION SERVICES PTY LTD. Level 7, 35 Collins Street Melbourne VIC 3000. Tel: (03) 9862 6550. Email: info@pscconnect.com.au. Reference: PSCNNORTHERN Account No: 0291162\", \"analyzer_results\": [{\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 19, \"end\": 33, \"score\": 1.0}, {\"entity_type\": \"AU_ABN\", \"start\": 58, \"end\": 73, \"score\": 1.0}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 82, \"end\": 92, \"score\": 1.0}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 130, \"end\": 149, \"score\": 1.0}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 199, \"end\": 209, \"score\": 1.0}, {\"entity_type\": \"PHONE_NUMBER\", \"start\": 307, \"end\": 321, \"score\": 0.75}, {\"entity_type\": \"EMAIL_ADDRESS\", \"start\": 330, \"end\": 352, \"score\": 1.0}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 390, \"end\": 397, \"score\": 0.75}]}'
```

---

## Test 2: GIBA Underwriter Remittance ($1,314.31)

**File:** `$1,314.31 GIBA.json`

**Contains:**

- Policy Numbers: 118U524989BPK, LPS016832716-29257, LPS024857046-M90567
- ABN: 135 132 455
- Names: Natascha Kate Powne, Roterb Rababeh
- Addresses

### Analyze

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"General Insurance Brokers of Australia Pty Ltd ABN 135 132 455. Suite 1105, 109 Pitt St SYDNEY NSW 2000. Invoice 278624 for Natascha Kate Powne Policy 118U524989BPK Business Package. Invoice 278634 Policy LPS016832716-29257 Professional Indemnity. Invoice 274305 for Roterb Rababeh Policy LPS024857046-M90567 Professional Indemnity. BizCover Pty Ltd Level 2 338 Pitt Street Sydney NSW 2000\", \"language\": \"en\"}'
```

**Expected Entities:**

- AU_ABN: 135 132 455
- AU_POLICY_NUMBER (3): 118U524989BPK, LPS016832716-29257, LPS024857046-M90567
- PERSON (2): Natascha Kate Powne, Roterb Rababeh
- LOCATION: SYDNEY, Sydney

### Anonymize

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"General Insurance Brokers of Australia Pty Ltd ABN 135 132 455. Suite 1105, 109 Pitt St SYDNEY NSW 2000. Invoice 278624 for Natascha Kate Powne Policy 118U524989BPK Business Package. Invoice 278634 Policy LPS016832716-29257 Professional Indemnity. Invoice 274305 for Roterb Rababeh Policy LPS024857046-M90567 Professional Indemnity. BizCover Pty Ltd Level 2 338 Pitt Street Sydney NSW 2000\", \"analyzer_results\": [{\"entity_type\": \"AU_ABN\", \"start\": 50, \"end\": 61, \"score\": 1.0}, {\"entity_type\": \"PERSON\", \"start\": 120, \"end\": 139, \"score\": 0.85}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 147, \"end\": 160, \"score\": 1.0}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 201, \"end\": 220, \"score\": 1.0}, {\"entity_type\": \"PERSON\", \"start\": 268, \"end\": 283, \"score\": 0.85}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 291, \"end\": 310, \"score\": 1.0}]}'
```

---

## Test 3: AB Comsure Remittance ($317.20)

**File:** `New Text Document1.json.txt`

**Contains:**

- Policy Numbers: 02U369936BPK
- Reference: 1055628 /001
- Account: I0442845 REN
- Insured: YALGANSUNG, Yalgan Sunglasses

### Analyze

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Express Cover ABN 68 127 707 975. Level 2, 338 Pitt Street SYDNEY NSW 2000. Date 09.12.25 COM/FPI/Y5749 YALGANSUNG Reference 1055628 /001 Policy 02U369936BPK Premium 300.00 Brokerage 75.00 Nett Due 317.20. Date 19.12.25 Yalgan Sunglasses Reference I0442845 REN\", \"language\": \"en\"}'
```

**Expected Entities:**

- AU_ABN: 68 127 707 975
- AU_POLICY_NUMBER: 02U369936BPK
- DATE_TIME: 09.12.25, 19.12.25
- LOCATION: SYDNEY

### Anonymize

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Express Cover ABN 68 127 707 975. Level 2, 338 Pitt Street SYDNEY NSW 2000. Date 09.12.25 COM/FPI/Y5749 YALGANSUNG Reference 1055628 /001 Policy 02U369936BPK Premium 300.00 Brokerage 75.00 Nett Due 317.20. Date 19.12.25 Yalgan Sunglasses Reference I0442845 REN\", \"analyzer_results\": [{\"entity_type\": \"AU_ABN\", \"start\": 17, \"end\": 30, \"score\": 1.0}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 133, \"end\": 145, \"score\": 1.0}]}'
```

---

## Test 4: EFT Refund Data

**File:** `EFTRefund_30-01-2025.json`

**Contains:**

- BSB: 6546546 (invalid format but should be detected)
- Account Numbers: 54654, 6546
- Customer: MXrk TXXXXon (partially redacted)
- App ID: 7148632

### Analyze

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"BizCover EFT Refund 30-01-2025. Customer MXrk TXXXXon App ID 7148632. Account Name 54654 BSB 6546546 Account Number 6546. Trust - EFT Refund Type Client Refund ID 61464 Amount $205.87. Total Trust EFT Refund $205.87 Total Funding EFT Refund $0.00\", \"language\": \"en\"}'
```

**Expected Entities:**

- DATE_TIME: 30-01-2025
- PERSON: MXrk TXXXXon
- AU_BSB: 6546546 (if pattern matches)
- AU_ACCOUNT_NUMBER: 54654, 6546, 7148632, 61464

### Anonymize

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"BizCover EFT Refund 30-01-2025. Customer MXrk TXXXXon App ID 7148632. Account Name 54654 BSB 6546546 Account Number 6546. Trust - EFT Refund Type Client Refund ID 61464 Amount $205.87. Total Trust EFT Refund $205.87 Total Funding EFT Refund $0.00\", \"analyzer_results\": [{\"entity_type\": \"DATE_TIME\", \"start\": 20, \"end\": 30, \"score\": 0.85}, {\"entity_type\": \"PERSON\", \"start\": 41, \"end\": 54, \"score\": 0.85}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 61, \"end\": 68, \"score\": 0.75}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 83, \"end\": 88, \"score\": 0.75}, {\"entity_type\": \"AU_BSB\", \"start\": 93, \"end\": 100, \"score\": 0.5}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 116, \"end\": 120, \"score\": 0.75}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 158, \"end\": 163, \"score\": 0.75}]}'
```

---

## Test 5: Complex AEI Remittance ($9,363.59)

**File:** `$9,363.59AEI 1.json`

**Contains:**

- Multiple policy numbers with various formats
- ABN: 55 636 434 412, 68 127 707 975
- Account numbers: 0241976, 0259050, 0252258, etc.
- Policy formats: BZF, E-GL, BPK, LPS

### Analyze

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"AEI Canberra Pty Ltd ABN 55 636 434 412. PO Box 727 FYSHWICK ACT 2609. Bizcover Pty Ltd T/As Express Cover ABN 68 127 707 975. Level 2, 501 La Trobe Street MELBOURNE VIC 3000. Account 0241976 /003 Policy BZF2002402. Account 0259050 /000 Policy E-GL-0004621. Account 0252258 /002 Policy 114U043180BPK. Account 0252258 /003 Policy 114U043180BPK. Account 0259035 /000 Policy LPS024418354-23962\", \"language\": \"en\"}'
```

**Expected Entities:**

- AU_ABN (2): 55 636 434 412, 68 127 707 975
- AU_POLICY_NUMBER (5+): BZF2002402, E-GL-0004621, 114U043180BPK, LPS024418354-23962
- AU_ACCOUNT_NUMBER: 0241976, 0259050, 0252258, 0259035
- LOCATION: MELBOURNE, FYSHWICK

### Anonymize

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"AEI Canberra Pty Ltd ABN 55 636 434 412. PO Box 727 FYSHWICK ACT 2609. Bizcover Pty Ltd T/As Express Cover ABN 68 127 707 975. Level 2, 501 La Trobe Street MELBOURNE VIC 3000. Account 0241976 /003 Policy BZF2002402. Account 0259050 /000 Policy E-GL-0004621. Account 0252258 /002 Policy 114U043180BPK. Account 0252258 /003 Policy 114U043180BPK. Account 0259035 /000 Policy LPS024418354-23962\", \"analyzer_results\": [{\"entity_type\": \"AU_ABN\", \"start\": 25, \"end\": 39, \"score\": 1.0}, {\"entity_type\": \"AU_ABN\", \"start\": 113, \"end\": 127, \"score\": 1.0}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 181, \"end\": 188, \"score\": 0.75}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 202, \"end\": 212, \"score\": 1.0}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 222, \"end\": 229, \"score\": 0.75}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 243, \"end\": 256, \"score\": 0.9}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 266, \"end\": 273, \"score\": 0.75}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 287, \"end\": 300, \"score\": 1.0}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 310, \"end\": 317, \"score\": 0.75}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 331, \"end\": 344, \"score\": 1.0}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 354, \"end\": 361, \"score\": 0.75}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 375, \"end\": 395, \"score\": 1.0}]}'
```

---

## Test 6: MartenGreen Underwriter Remittance ($2,039.99)

**File:** `$2,039.99 MartenGreen 20260127 Underwriter Remittance Advice - BIZCOVER $2,039.99.json`

### Analyze

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"BIZCOVER PTY LTD PO Box 823 EDGECLIFF NSW 2027. MartenGreen Underwriter Remittance Advice dated 27-01-2026. Reference PSCNNORTHERN Amount $2,039.99 AUD. Professional Indemnity Insurance policies processed. Contact details available at business address.\", \"language\": \"en\"}'
```

**Expected Entities:**

- DATE_TIME: 27-01-2026
- LOCATION: EDGECLIFF

### Anonymize

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"BIZCOVER PTY LTD PO Box 823 EDGECLIFF NSW 2027. MartenGreen Underwriter Remittance Advice dated 27-01-2026. Reference PSCNNORTHERN Amount $2,039.99 AUD. Professional Indemnity Insurance policies processed. Contact details available at business address.\", \"analyzer_results\": [{\"entity_type\": \"DATE_TIME\", \"start\": 97, \"end\": 107, \"score\": 0.85}]}'
```

---

## Combined Multi-Entity Test

Test all entity types together from multiple files:

### Analyze All

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"BIZCOVER PTY LTD ABN 68 127 707 975. Contact Natascha Kate Powne at Level 2, 338 Pitt Street Sydney NSW 2000. Policies: BZF2024736, LPS019877447-11886, 118U524989BPK, E-GL-0004621. BSB 062-000 Account 12345678. TFN 123456782 Medicare 2123 45670 1. Email info@pscconnect.com.au Phone (03) 9862 6550. Reference date 27-01-2026.\", \"language\": \"en\"}'
```

**Expected Entities:**

- AU_ABN: 68 127 707 975
- PERSON: Natascha Kate Powne
- LOCATION: Sydney
- AU_POLICY_NUMBER (4): BZF2024736, LPS019877447-11886, 118U524989BPK, E-GL-0004621
- AU_BSB: 062-000
- AU_ACCOUNT_NUMBER: 12345678
- AU_TFN: 123456782
- AU_MEDICARE: 2123 45670 1
- EMAIL_ADDRESS: info@pscconnect.com.au
- PHONE_NUMBER: (03) 9862 6550
- DATE_TIME: 27-01-2026

### Anonymize All

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"BIZCOVER PTY LTD ABN 68 127 707 975. Contact Natascha Kate Powne at Level 2, 338 Pitt Street Sydney NSW 2000. Policies: BZF2024736, LPS019877447-11886, 118U524989BPK, E-GL-0004621. BSB 062-000 Account 12345678. TFN 123456782 Medicare 2123 45670 1. Email info@pscconnect.com.au Phone (03) 9862 6550. Reference date 27-01-2026.\", \"analyzer_results\": [{\"entity_type\": \"AU_ABN\", \"start\": 20, \"end\": 34, \"score\": 1.0}, {\"entity_type\": \"PERSON\", \"start\": 44, \"end\": 63, \"score\": 0.85}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 118, \"end\": 128, \"score\": 1.0}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 130, \"end\": 149, \"score\": 1.0}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 151, \"end\": 164, \"score\": 1.0}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 166, \"end\": 179, \"score\": 0.9}, {\"entity_type\": \"AU_BSB\", \"start\": 185, \"end\": 192, \"score\": 1.0}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 201, \"end\": 209, \"score\": 0.75}, {\"entity_type\": \"AU_TFN\", \"start\": 215, \"end\": 224, \"score\": 1.0}, {\"entity_type\": \"AU_MEDICARE\", \"start\": 234, \"end\": 248, \"score\": 1.0}, {\"entity_type\": \"EMAIL_ADDRESS\", \"start\": 257, \"end\": 279, \"score\": 1.0}, {\"entity_type\": \"PHONE_NUMBER\", \"start\": 286, \"end\": 300, \"score\": 0.75}, {\"entity_type\": \"DATE_TIME\", \"start\": 318, \"end\": 328, \"score\": 0.85}]}'
```

---

## Custom Anonymization Methods

### Hash Sensitive Data

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Policy BZF2024736 ABN 68 127 707 975 TFN 123456782\", \"analyzer_results\": [{\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 7, \"end\": 17, \"score\": 1.0}, {\"entity_type\": \"AU_ABN\", \"start\": 22, \"end\": 36, \"score\": 1.0}, {\"entity_type\": \"AU_TFN\", \"start\": 41, \"end\": 50, \"score\": 1.0}], \"anonymizers\": {\"DEFAULT\": {\"type\": \"hash\"}}}'
```

### Mask with Asterisks

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Policy BZF2024736 ABN 68 127 707 975 TFN 123456782\", \"analyzer_results\": [{\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 7, \"end\": 17, \"score\": 1.0}, {\"entity_type\": \"AU_ABN\", \"start\": 22, \"end\": 36, \"score\": 1.0}, {\"entity_type\": \"AU_TFN\", \"start\": 41, \"end\": 50, \"score\": 1.0}], \"anonymizers\": {\"DEFAULT\": {\"type\": \"mask\", \"masking_char\": \"*\", \"chars_to_mask\": 10, \"from_end\": false}}}'
```

### Replace with Custom Values

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Policy BZF2024736 ABN 68 127 707 975\", \"analyzer_results\": [{\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 7, \"end\": 17, \"score\": 1.0}, {\"entity_type\": \"AU_ABN\", \"start\": 22, \"end\": 36, \"score\": 1.0}], \"anonymizers\": {\"AU_POLICY_NUMBER\": {\"type\": \"replace\", \"new_value\": \"POLICY_REDACTED\"}, \"AU_ABN\": {\"type\": \"replace\", \"new_value\": \"ABN_REDACTED\"}}}'
```

---

## PowerShell Testing Script

Save this as `test_broker_data.ps1`:

```powershell
# Test Australian Broker Remittance Data PII Detection

Write-Host "`n=== TESTING BROKER REMITTANCE DATA ===" -ForegroundColor Green

# Test 1: PSC Network
Write-Host "`n--- Test 1: PSC Network ($7,876.55) ---" -ForegroundColor Cyan
$text = "PSC NETWORK Policy 47-ZBC-000361 for DIDEAN PTY LTD ABN 23 141 574 914. Policy BZF2024736 for Inscope Plumbing Group. Policy LPS019877447-11886 for SMARTTECH CONSULTANCY SERVICES. Account No: 0291162"
$response = curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d "{`"text`": `"$text`", `"language`": `"en`"}" | ConvertFrom-Json
Write-Host "Detected:" -ForegroundColor Yellow
$response | ForEach-Object { Write-Host "  $($_.entity_type): $($text.Substring($_.start, $_.end - $_.start)) (score: $($_.score))" }

# Test 2: GIBA
Write-Host "`n--- Test 2: GIBA Underwriter ($1,314.31) ---" -ForegroundColor Cyan
$text = "General Insurance Brokers ABN 135 132 455. Policy 118U524989BPK for Natascha Kate Powne. Policy LPS016832716-29257 Professional Indemnity."
$response = curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d "{`"text`": `"$text`", `"language`": `"en`"}" | ConvertFrom-Json
Write-Host "Detected:" -ForegroundColor Yellow
$response | ForEach-Object { Write-Host "  $($_.entity_type): $($text.Substring($_.start, $_.end - $_.start)) (score: $($_.score))" }

# Test 3: Combined Multi-Entity
Write-Host "`n--- Test 3: Combined Multi-Entity ---" -ForegroundColor Cyan
$text = "BIZCOVER ABN 68 127 707 975. Contact Natascha Kate Powne. Policies: BZF2024736, LPS019877447-11886, 118U524989BPK. BSB 062-000 Account 12345678. TFN 123456782 Medicare 2123 45670 1."
$response = curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d "{`"text`": `"$text`", `"language`": `"en`"}" | ConvertFrom-Json
Write-Host "Detected:" -ForegroundColor Yellow
$response | Sort-Object -Property start | ForEach-Object {
    $entityText = $text.Substring($_.start, $_.end - $_.start)
    $color = if ($_.entity_type -match '^AU_') { 'Green' } else { 'Cyan' }
    Write-Host "  $($_.entity_type.PadRight(25)): $entityText (score: $($_.score))" -ForegroundColor $color
}

Write-Host "`n=== ALL TESTS COMPLETE ===" -ForegroundColor Green
```

**Run:** `.\test_broker_data.ps1`

---

## Troubleshooting

### Containers Not Running

```powershell
docker ps
docker start presidio-analyzer-au
docker start presidio-anonymizer-au
```

### Check Container Health

```powershell
curl.exe http://localhost:5002/health
curl.exe http://localhost:5001/health
```

### View Container Logs

```powershell
docker logs presidio-analyzer-au
docker logs presidio-anonymizer-au
```

### Test Connection

```powershell
Test-NetConnection localhost -Port 5002
Test-NetConnection localhost -Port 5001
```

---

## Notes

1. **JSON Escaping:** All quotes inside the JSON payload must be escaped with `\"`
2. **PowerShell:** Use `curl.exe` not `curl` (which is an alias for `Invoke-WebRequest`)
3. **Entity Positions:** Start/end positions are 0-indexed and refer to character positions in the text
4. **Score Threshold:** Default is 0.0 (all entities), can be adjusted with `score_threshold` parameter
5. **Language:** Always specify `"language": "en"` for English text
6. **Policy Patterns:** Our custom recognizers detect 8+ Australian policy number formats
7. **BSB Format:** Supports both XXX-XXX and XXXXXX formats
8. **Account Numbers:** 6-9 digit numbers with context keywords like "account", "bsb", "transfer"

---

## Performance Tips

- **Batch Processing:** For multiple files, collect all text and analyze in one request
- **Caching:** Docker image layers are cached, rebuilds are fast (~5 seconds)
- **Parallel Testing:** Run multiple curl commands simultaneously in different terminal windows
- **Large Files:** Split very large JSON files into smaller chunks for analysis

---

**Last Updated:** 2026-03-02
**Version:** Australian-only build with 7 custom recognizers
**Containers:** presidio-analyzer-au:latest, presidio-anonymizer-au:latest
