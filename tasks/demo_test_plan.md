# CitizenPath Demo Test Plan

## Objective
Demonstrate that CitizenPath can run a public information-discovery task and independently verify the result.

## Test 1 — National Portal of India
- Task ID: TASK-001
- Start URL: https://www.india.gov.in/
- Expected fields: service_name, service_url
- Pass condition: Both fields are returned and verified against the official source.

## Test 2 — Government Schemes
- Task ID: TASK-002
- Start URL: https://www.myscheme.gov.in/
- Expected fields: service_name, service_purpose, service_url
- Pass condition: All required fields are returned and supported by evidence.

## Test 3 — Aadhaar Information
- Task ID: TASK-003
- Start URL: https://uidai.gov.in/
- Expected fields: organization_name, organization_purpose, service_url
- Pass condition: All required fields are returned and supported by evidence.

## Integration checks
1. Dashboard displays the available tasks.
2. User can start a task.
3. Backend returns a run ID and status.
4. Run results include extracted fields and evidence URLs.
5. Verification checks the required fields and source.
6. Dashboard displays success, partial, blocked, or failed.
7. Score is based on actual verification results, not an assumed success.

## Safety boundaries
- Use public, read-only information.
- Do not enter personal information.
- Stop if login, OTP, CAPTCHA, or payment is required.

## Demo note
Example JSON files are illustrative. Record actual outcomes only after running the integrated application.