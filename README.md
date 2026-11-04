# TalentFlow AI — Autonomous HR Agency
**Prepared by:** Apurva Arpit  
**University:** Riga Nordic University (RNU)  
**Agency type:** HR / recruitment operations  
**Status:** Implementation scaffold; live integrations require local credentials and verification.

## Overview
TalentFlow AI coordinates eight role-based agents. The Project Manager records each run as
`Timestamp | Agent Name | Task Performed | Output Status`, optionally appends the ledger to Google
Sheets, and optionally sends a daily brief by email.

## Upstream repository
This project is designed to complement, not misrepresent, the upstream
[markfulton/ai-employees](https://github.com/markfulton/ai-employees) repository. That repository
provides its own eight employee kits and installer. TalentFlow's HR roles below are project-specific
role prompts; they are not claimed to be native kits shipped by the upstream project.

To inspect and install the upstream toolkit, follow its current README. For example, the repository
documents a Claude Code plugin installation:
```text
/plugin marketplace add markfulton/ai-employees
/plugin install ai-employees@ai-employees
```
Or, when using the npm package and the current CLI:
```bash
npx ai-employees hire --help
```
Use the CLI's supported employee IDs and options from the installed version. The upstream installer
generates its own `.installed.json`; do not overwrite that file with this project's metadata.

## Quick start (Windows PowerShell)
1. Install Python 3.10+.
2. Extract this project to a local folder outside OneDrive/Dropbox/Google Drive/iCloud sync.
3. Open PowerShell in the project folder.
4. Create an environment and install packages:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```
5. Run a local demo:
```powershell
python automation/daily_workflow.py --demo
```
This writes `data/activity_log.csv` and `data/daily_brief.md`. In demo mode, no external messages are sent.

## Google Sheets integration
1. Create a Google Cloud project and enable Google Sheets API.
2. Create a service account and download its JSON key to a secure local path.
3. Share the destination spreadsheet with the service account's email as Editor.
4. Set `GOOGLE_SERVICE_ACCOUNT_FILE` and `GOOGLE_SHEET_ID` in `.env`.
5. Add `GOOGLE_WORKSHEET_NAME=Activity Log`.
6. Run `python automation/daily_workflow.py --live-sheets` only after confirming the spreadsheet ID and sharing.

Required sheet header:
`Timestamp | Agent Name | Task Performed | Output Status`

## Email integration
The starter supports SMTP with an app password (not your normal account password). For Gmail, enable 2-Step Verification and create an app password if available to your account. Store it only in `.env`, never in GitHub.
Set `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_APP_PASSWORD`, and `REPORT_TO`.
Run `python automation/daily_workflow.py --send-email` to send a brief after the workflow has run. A daily schedule must be configured separately in Windows Task Scheduler or cron.

## Safe operation
- The included agents produce recruitment workflow activity and templates; an LLM or browser agent is not magically enabled by this scaffold.
- Use fictional/test candidate data during demonstrations.
- Do not make hiring decisions solely from automated scores. Keep human review for shortlisting and all consequential decisions.
- Do not infer protected traits or use them to rank candidates.
- Email sending and external writes are opt-in flags, disabled by default.
- Never commit `.env`, OAuth tokens, service-account keys, CVs, or candidate personal data.

## Deliverables
- `agents/`: eight role cards and operating prompts
- `automation/daily_workflow.py`: runnable local demo and optional integrations
- `integrations/google_sheets.py`, `integrations/email_report.py`: integrations
- `.installed.json`: TalentFlow project manifest, **not** the upstream installer's generated record
- `documentation/agency_plan.docx`, `documentation/project_presentation.pptx`
- `documentation/screen_recording_checklist.md`
