# Direct cURL Commands for Australian PII Testing

This guide provides ready-to-use cURL commands for testing Australian PII detection and anonymization without JSON files.

## Quick Test - All Australian Entities

### Analyze Multiple Entities

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Contact of Sajal is 0424459876, his TFN: 123456782, ABN: 53004085616, Medicare: 2123 45670 1\", \"language\": \"en\"}'
```

### Anonymize Result

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Contact of Sajal is 0424459876, his TFN: 123456782, ABN: 53004085616, Medicare: 2123 45670 1\", \"analyzer_results\": [{\"entity_type\": \"PERSON\", \"start\": 11, \"end\": 16, \"score\": 0.85}, {\"entity_type\": \"PHONE_NUMBER\", \"start\": 20, \"end\": 30, \"score\": 0.75}, {\"entity_type\": \"AU_TFN\", \"start\": 41, \"end\": 50, \"score\": 1.0}, {\"entity_type\": \"AU_ABN\", \"start\": 57, \"end\": 68, \"score\": 1.0}, {\"entity_type\": \"AU_MEDICARE\", \"start\": 80, \"end\": 93, \"score\": 1.0}]}'
```

---

## Individual Entity Tests

### 1. Tax File Number (AU_TFN)

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"My Tax File Number is 123456782 for tax purposes\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"My Tax File Number is 123456782 for tax purposes\", \"analyzer_results\": [{\"entity_type\": \"AU_TFN\", \"start\": 26, \"end\": 35, \"score\": 1.0}]}'
```

**Expected Result:** `My Tax File Number is <AU_TFN> for tax purposes`

---

### 2. Australian Business Number (AU_ABN)

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Company ABN: 53004085616 registered in Victoria\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Company ABN: 53004085616 registered in Victoria\", \"analyzer_results\": [{\"entity_type\": \"AU_ABN\", \"start\": 13, \"end\": 24, \"score\": 1.0}]}'
```

**Expected Result:** `Company ABN: <AU_ABN> registered in Victoria`

---

### 3. Australian Company Number (AU_ACN)

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"The ACN is 004085616 for this business entity\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"The ACN is 004085616 for this business entity\", \"analyzer_results\": [{\"entity_type\": \"AU_ACN\", \"start\": 11, \"end\": 20, \"score\": 1.0}]}'
```

**Expected Result:** `The ACN is <AU_ACN> for this business entity`

---

### 4. Medicare Number (AU_MEDICARE)

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Patient Medicare number: 2123 45670 1 for billing\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Patient Medicare number: 2123 45670 1 for billing\", \"analyzer_results\": [{\"entity_type\": \"AU_MEDICARE\", \"start\": 25, \"end\": 39, \"score\": 1.0}]}'
```

**Expected Result:** `Patient Medicare number: <AU_MEDICARE> for billing`

---

### 5. Bank State Branch (AU_BSB)

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Please transfer to BSB 654-654 for payment processing\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Please transfer to BSB 654-654 for payment processing\", \"analyzer_results\": [{\"entity_type\": \"AU_BSB\", \"start\": 23, \"end\": 30, \"score\": 1.0}]}'
```

**Expected Result:** `Please transfer to BSB <AU_BSB> for payment processing`

---

### 6. Insurance Policy Number - BPK Format (AU_POLICY_NUMBER)

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Insurance policy 118U524989BPK is active and covers property damage\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Insurance policy 118U524989BPK is active and covers property damage\", \"analyzer_results\": [{\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 17, \"end\": 30, \"score\": 1.0}]}'
```

**Expected Result:** `Insurance policy <AU_POLICY_NUMBER> is active and covers property damage`

---

### 7. Insurance Policy Number - AUBP Format

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Policy number AUBP011949 provides comprehensive coverage\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Policy number AUBP011949 provides comprehensive coverage\", \"analyzer_results\": [{\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 14, \"end\": 24, \"score\": 1.0}]}'
```

**Expected Result:** `Policy number <AU_POLICY_NUMBER> provides comprehensive coverage`

---

### 8. Insurance Policy Number - LPS Format

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Lloyds policy LPS016832716-29257 for marine insurance\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Lloyds policy LPS016832716-29257 for marine insurance\", \"analyzer_results\": [{\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 14, \"end\": 32, \"score\": 1.0}]}'
```

**Expected Result:** `Lloyds policy <AU_POLICY_NUMBER> for marine insurance`

---

### 9. Bank Account Number (AU_ACCOUNT_NUMBER)

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Bank account number 6546546 linked to BSB 654-654\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Bank account number 6546546 linked to BSB 654-654\", \"analyzer_results\": [{\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 20, \"end\": 27, \"score\": 0.75}, {\"entity_type\": \"AU_BSB\", \"start\": 41, \"end\": 48, \"score\": 1.0}]}'
```

**Expected Result:** `Bank account number <AU_ACCOUNT_NUMBER> linked to BSB <AU_BSB>`

---

## Complex Scenario Tests

### 10. Insurance Remittance Document

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Insurance Remittance: Policy 118U524989BPK, Broker: Natascha Powne, BSB: 654-654, Account: 6546546, TFN: 123456782, ABN: 53004085616, Amount: $1,500.00\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Insurance Remittance: Policy 118U524989BPK, Broker: Natascha Powne, BSB: 654-654, Account: 6546546, TFN: 123456782, ABN: 53004085616, Amount: $1,500.00\", \"analyzer_results\": [{\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 29, \"end\": 42, \"score\": 1.0}, {\"entity_type\": \"PERSON\", \"start\": 52, \"end\": 66, \"score\": 0.85}, {\"entity_type\": \"AU_BSB\", \"start\": 73, \"end\": 80, \"score\": 1.0}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 91, \"end\": 98, \"score\": 0.75}, {\"entity_type\": \"AU_TFN\", \"start\": 105, \"end\": 114, \"score\": 1.0}, {\"entity_type\": \"AU_ABN\", \"start\": 121, \"end\": 132, \"score\": 1.0}]}'
```

**Expected Result:** `Insurance Remittance: Policy <AU_POLICY_NUMBER>, Broker: <PERSON>, BSB: <AU_BSB>, Account: <AU_ACCOUNT_NUMBER>, TFN: <AU_TFN>, ABN: <AU_ABN>, Amount: $1,500.00`

---

### 11. Customer Details

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Customer: Roterb Rababeh, Address: 123 Collins Street Melbourne VIC 3000, TFN: 987654321, Medicare: 2123 45670 1, Email: roterb@example.com.au\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Customer: Roterb Rababeh, Address: 123 Collins Street Melbourne VIC 3000, TFN: 987654321, Medicare: 2123 45670 1, Email: roterb@example.com.au\", \"analyzer_results\": [{\"entity_type\": \"PERSON\", \"start\": 10, \"end\": 24, \"score\": 0.85}, {\"entity_type\": \"LOCATION\", \"start\": 35, \"end\": 75, \"score\": 0.85}, {\"entity_type\": \"AU_TFN\", \"start\": 82, \"end\": 91, \"score\": 1.0}, {\"entity_type\": \"AU_MEDICARE\", \"start\": 103, \"end\": 116, \"score\": 1.0}, {\"entity_type\": \"EMAIL_ADDRESS\", \"start\": 125, \"end\": 145, \"score\": 1.0}]}'
```

**Expected Result:** `Customer: <PERSON>, Address: <LOCATION>, TFN: <AU_TFN>, Medicare: <AU_MEDICARE>, Email: <EMAIL_ADDRESS>`

---

### 12. Payment Instruction

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Payment Details - Beneficiary: John Smith, BSB: 654-654, Account: 12345678, Reference: Policy BZF2024736, Amount: $2,450.50\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Payment Details - Beneficiary: John Smith, BSB: 654-654, Account: 12345678, Reference: Policy BZF2024736, Amount: $2,450.50\", \"analyzer_results\": [{\"entity_type\": \"PERSON\", \"start\": 32, \"end\": 42, \"score\": 0.85}, {\"entity_type\": \"AU_BSB\", \"start\": 49, \"end\": 56, \"score\": 1.0}, {\"entity_type\": \"AU_ACCOUNT_NUMBER\", \"start\": 67, \"end\": 75, \"score\": 0.75}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 94, \"end\": 104, \"score\": 1.0}]}'
```

**Expected Result:** `Payment Details - Beneficiary: <PERSON>, BSB: <AU_BSB>, Account: <AU_ACCOUNT_NUMBER>, Reference: Policy <AU_POLICY_NUMBER>, Amount: $2,450.50`

---

### 13. Business Transaction Record

**Analyze:**

```powershell
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Transaction Record: Company ABN 53004085616, ACN 004085616, Policy E-GL017-002-032-26246, Contact: Jane Doe, Phone: +61 3 9999 8888\", \"language\": \"en\"}'
```

**Anonymize:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"Transaction Record: Company ABN 53004085616, ACN 004085616, Policy E-GL017-002-032-26246, Contact: Jane Doe, Phone: +61 3 9999 8888\", \"analyzer_results\": [{\"entity_type\": \"AU_ABN\", \"start\": 32, \"end\": 43, \"score\": 1.0}, {\"entity_type\": \"AU_ACN\", \"start\": 49, \"end\": 58, \"score\": 1.0}, {\"entity_type\": \"AU_POLICY_NUMBER\", \"start\": 67, \"end\": 88, \"score\": 1.0}, {\"entity_type\": \"PERSON\", \"start\": 99, \"end\": 107, \"score\": 0.85}, {\"entity_type\": \"PHONE_NUMBER\", \"start\": 116, \"end\": 132, \"score\": 0.75}]}'
```

**Expected Result:** `Transaction Record: Company ABN <AU_ABN>, ACN <AU_ACN>, Policy <AU_POLICY_NUMBER>, Contact: <PERSON>, Phone: <PHONE_NUMBER>`

---

## Custom Anonymization Methods

### Replace with Custom Value

**Mask TFN with asterisks:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"My TFN is 123456782\", \"anonymizers\": {\"AU_TFN\": {\"type\": \"mask\", \"masking_char\": \"*\", \"chars_to_mask\": 6, \"from_end\": false}}, \"analyzer_results\": [{\"entity_type\": \"AU_TFN\", \"start\": 10, \"end\": 19, \"score\": 1.0}]}'
```

**Expected Result:** `My TFN is ******782`

---

**Replace with custom value:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"My TFN is 123456782\", \"anonymizers\": {\"AU_TFN\": {\"type\": \"replace\", \"new_value\": \"XXX-XXX-XXX\"}}, \"analyzer_results\": [{\"entity_type\": \"AU_TFN\", \"start\": 10, \"end\": 19, \"score\": 1.0}]}'
```

**Expected Result:** `My TFN is XXX-XXX-XXX`

---

**Hash the value:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"My TFN is 123456782\", \"anonymizers\": {\"AU_TFN\": {\"type\": \"hash\", \"hash_type\": \"sha256\"}}, \"analyzer_results\": [{\"entity_type\": \"AU_TFN\", \"start\": 10, \"end\": 19, \"score\": 1.0}]}'
```

**Expected Result:** `My TFN is a665a45920422f9d417e4867efdc4fb8a...` (hash value)

---

**Redact completely:**

```powershell
curl.exe -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d '{\"text\": \"My TFN is 123456782\", \"anonymizers\": {\"AU_TFN\": {\"type\": \"redact\"}}, \"analyzer_results\": [{\"entity_type\": \"AU_TFN\", \"start\": 10, \"end\": 19, \"score\": 1.0}]}'
```

**Expected Result:** `My TFN is `

---

## Two-Step Workflow (Analyze then Anonymize)

### PowerShell Script Example

```powershell
# Step 1: Analyze and capture results
$analyzeResponse = curl.exe -s -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Contact of Sajal is 0424459876, his TFN: 123456782\", \"language\": \"en\"}' | ConvertFrom-Json

# Display detected entities
Write-Host "Detected Entities:" -ForegroundColor Yellow
$analyzeResponse | ForEach-Object {
    Write-Host "  - $($_.entity_type) (score: $($_.score))" -ForegroundColor Green
}

# Step 2: Build anonymize request
$anonymizeBody = @{
    text = "Contact of Sajal is 0424459876, his TFN: 123456782"
    analyzer_results = $analyzeResponse
} | ConvertTo-Json -Depth 10

# Anonymize
$anonymizeResponse = curl.exe -s -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d $anonymizeBody | ConvertFrom-Json

# Display result
Write-Host "`nOriginal:   Contact of Sajal is 0424459876, his TFN: 123456782" -ForegroundColor White
Write-Host "Anonymized: $($anonymizeResponse.text)" -ForegroundColor Cyan
```

---

## Quick Test All Entities

```powershell
# Test all Australian entity types in one command
curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"Full Record: Name: Sarah Johnson, TFN: 123456782, ABN: 53004085616, ACN: 004085616, Medicare: 2123 45670 1, BSB: 654-654, Account: 6546546, Policy: 118U524989BPK, Email: sarah@example.com.au, Phone: 0424459876\", \"language\": \"en\"}'
```

**Expected Detection:**

- PERSON (Sarah Johnson)
- AU_TFN (123456782)
- AU_ABN (53004085616)
- AU_ACN (004085616)
- AU_MEDICARE (2123 45670 1)
- AU_BSB (654-654)
- AU_ACCOUNT_NUMBER (6546546)
- AU_POLICY_NUMBER (118U524989BPK)
- EMAIL_ADDRESS (sarah@example.com.au)
- PHONE_NUMBER (0424459876)

---

## Testing Tips

### Format JSON for readability

Use PowerShell here-strings for better readability:

```powershell
$json = @"
{
  "text": "Contact of Sajal is 0424459876, his TFN: 123456782",
  "language": "en"
}
"@

curl.exe -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d $json
```

### Save response to variable

```powershell
$result = curl.exe -s -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"TFN: 123456782\", \"language\": \"en\"}' | ConvertFrom-Json
$result | ConvertTo-Json -Depth 10
```

### Pretty print JSON output

```powershell
curl.exe -s -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d '{\"text\": \"TFN: 123456782\", \"language\": \"en\"}' | ConvertFrom-Json | ConvertTo-Json -Depth 10
```

---

## Service Status Commands

### Check if services are running

```powershell
docker ps | Select-String presidio
```

### Start services

```powershell
docker start presidio-analyzer presidio-anonymizer
```

### View logs

```powershell
docker logs presidio-analyzer --tail 20
docker logs presidio-anonymizer --tail 20
```

### Health check

```powershell
curl.exe http://localhost:5002/health
curl.exe http://localhost:5001/health
```

---

## Common Issues

### Error: "Failed to decode JSON"

- Check that all quotes are properly escaped with `\"`
- Ensure no line breaks in the JSON string
- Use `@"..."@` in PowerShell for multi-line strings

### Error: "Could not connect to server"

- Check if containers are running: `docker ps | grep presidio`
- Start containers: `docker start presidio-analyzer presidio-anonymizer`
- Wait 20-30 seconds after starting for services to be ready

### Empty analyzer_results

- Run analyze first to get actual entity positions
- Copy the exact response from analyze to anonymize
- Use `-Depth 10` with `ConvertTo-Json` to preserve nested arrays

---

## Performance Testing

### Batch test multiple texts

```powershell
$texts = @(
    "TFN: 123456782",
    "ABN: 53004085616",
    "Medicare: 2123 45670 1"
)

foreach ($text in $texts) {
    $json = "{`"text`": `"$text`", `"language`": `"en`"}"
    Write-Host "`nTesting: $text" -ForegroundColor Yellow
    curl.exe -s -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d $json | ConvertFrom-Json | ConvertTo-Json
}
```

---

## Additional Resources

- [JSON Test Files](.) - Pre-made JSON files for easier testing
- [Automated Test Suite](run_all_tests.ps1) - Run all tests automatically
- [Complete Testing Guide](TESTING_GUIDE.md) - Comprehensive documentation
- [Quick Reference](QUICK_REFERENCE.md) - Quick command reference
