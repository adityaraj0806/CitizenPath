# CitizenPath Integration Checklist

## TASK-001 — National Portal of India
- Start URL: https://www.india.gov.in/
- Required fields: service_name, service_url
- Verify: returned name and URL match the official source.

## TASK-002 — Government Schemes
- Start URL: https://www.myscheme.gov.in/
- Required fields: service_name, service_purpose, service_url
- Verify: returned information is supported by the official source.

## TASK-003 — Aadhaar Information
- Start URL: https://uidai.gov.in/
- Required fields: organization_name, organization_purpose, service_url
- Verify: returned information is supported by the official source.

## API integration checks
- [ ] POST /api/runs accepts a valid task_id.
- [ ] The response includes a run_id and status.
- [ ] GET /api/runs/{run_id} returns the current run.
- [ ] The returned task_id matches the requested task.
- [ ] Required result fields are present.
- [ ] Evidence URLs support the extracted information.
- [ ] Verification results reflect actual checks.
- [ ] Score is derived from the agreed scoring rules.
- [ ] Errors and blockers are reported accurately.
- [ ] Dashboard status matches the backend response.

## Safety
- Use public, read-only information.
- Stop if login, OTP, CAPTCHA, or payment is required.
- Do not enter personal information.

Note: Do not mark an integration check as passed until it has been tested against the working API.