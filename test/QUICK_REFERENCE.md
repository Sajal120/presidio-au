# Quick Reference - Australian PII Testing

## Run All Tests

```powershell
cd test
.\run_all_tests.ps1
```

## Quick Individual Tests

### Test TFN

```powershell
curl.exe -s -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d "@test/test_tfn.json"
```

### Test ABN

```powershell
curl.exe -s -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d "@test/test_abn.json"
```

### Test BSB

```powershell
curl.exe -s -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d "@test/test_bsb.json"
```

### Test Policy Number

```powershell
curl.exe -s -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d "@test/test_policy_bpk.json"
```

### Test Insurance Remittance (Combined)

```powershell
curl.exe -s -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d "@test/test_insurance_remittance.json"
```

## Analyze + Anonymize Complete Example

```powershell
# Read test file
$text = (Get-Content test/test_insurance_remittance.json | ConvertFrom-Json).text

# Step 1: Analyze
$analyzeBody = @{text=$text; language='en'} | ConvertTo-Json
$entities = curl.exe -s -X POST http://localhost:5002/analyze -H "Content-Type: application/json" -d $analyzeBody | ConvertFrom-Json

# Step 2: Anonymize
$anonymizeBody = @{text=$text; analyzer_results=$entities} | ConvertTo-Json -Depth 10
curl.exe -s -X POST http://localhost:5001/anonymize -H "Content-Type: application/json" -d $anonymizeBody | ConvertFrom-Json | Select-Object -ExpandProperty text
```

## Test Files

| File                             | Entity Types           |
| -------------------------------- | ---------------------- |
| `test_tfn.json`                  | AU_TFN                 |
| `test_abn.json`                  | AU_ABN                 |
| `test_acn.json`                  | AU_ACN                 |
| `test_medicare.json`             | AU_MEDICARE            |
| `test_bsb.json`                  | AU_BSB                 |
| `test_policy_bpk.json`           | AU_POLICY_NUMBER       |
| `test_policy_aubp.json`          | AU_POLICY_NUMBER       |
| `test_policy_lps.json`           | AU_POLICY_NUMBER       |
| `test_account.json`              | AU_ACCOUNT_NUMBER      |
| `test_insurance_remittance.json` | Multiple (7+ entities) |
| `test_customer_details.json`     | Multiple (6+ entities) |
| `test_payment_instruction.json`  | Multiple (4+ entities) |
| `test_business_transaction.json` | Multiple (5+ entities) |

## Detected Entity Types

✅ **AU_TFN** - Tax File Number (score: 1.0)
✅ **AU_ABN** - Australian Business Number (score: 1.0)
✅ **AU_ACN** - Australian Company Number (score: 1.0)
✅ **AU_MEDICARE** - Medicare Number (score: 1.0)
✅ **AU_BSB** - Bank State Branch (score: 1.0)
✅ **AU_POLICY_NUMBER** - Insurance Policy Numbers (score: 1.0)
✅ **AU_ACCOUNT_NUMBER** - Bank Account Numbers (score: 0.75)
✅ **PERSON** - Person Names (score: 0.85)
✅ **EMAIL_ADDRESS** - Email Addresses (score: 1.0)
✅ **PHONE_NUMBER** - Phone Numbers (score: 0.4-0.75)
✅ **DATE_TIME** - Dates (score: 0.85)
✅ **LOCATION** - Locations (score: 0.85)

## Container Commands

### Start Services

```powershell
docker start presidio-analyzer presidio-anonymizer
```

### Check Status

```powershell
docker ps | Select-String presidio
```

### View Logs

```powershell
docker logs presidio-analyzer --tail 20
docker logs presidio-anonymizer --tail 20
```

### Restart Services

```powershell
docker restart presidio-analyzer presidio-anonymizer
```

## Full Documentation

See [TESTING_GUIDE.md](test/TESTING_GUIDE.md) for complete documentation.
