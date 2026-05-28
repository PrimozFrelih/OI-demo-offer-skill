# Orka offer generation package

This repository contains a reusable package for generating Slovenian business offers for Orka Informatika d.o.o.

## Goal

Generate new business offers based on:
- reference DOCX offers in `/input`,
- extracted structure and style rules,
- reusable templates in `/templates`,
- business rules in `/rules`.

## Company identity

Company:
Orka Informatika d.o.o.  
Ulica Štefana Kovača 10  
9000 Murska Sobota  
Slovenia

## Expected output

Default output format:
- Markdown first
- DOCX if requested

Generated offers must be saved to `/output`.

## Rules

- Do not blindly copy text from reference offers.
- Extract reusable structure, tone, assumptions, pricing logic and legal clauses.
- Ask for missing business-critical inputs before generating final offer.
- Keep Slovenian business tone.
- Use clear numbered sections.
- Include tables where useful.
- Avoid unnecessary marketing fluff.
- Do not invent binding legal commitments beyond the provided rules.
- If something is unclear, state assumptions before generating the offer.

## Default offer sections

Use this structure unless the user requests otherwise:

1. Namen sodelovanja
2. Predmet ponudbe
3. Obseg dela
4. Terminski okvir
5. Cena
6. Pogoji plačila
7. Odgovornosti naročnika
8. Izključitve
9. Pravice, licence and intellectual property, if relevant
10. Veljavnost ponudbe

## Default assumptions

- Prices exclude VAT unless stated otherwise.
- Offer validity is 30 days.
- Payment deadline is 15 days from invoice issue.
- Missing integrations are excluded unless explicitly included.
- Additional requests are treated as scope changes.

## Default user interaction mode

When the user asks to prepare a new offer, create a new business offer, generate an offer, or says something similar, immediately switch to interview mode.

Do not ask all questions at once.

Start by asking only for:
1. client name,
2. client address,
3. offer subject.

After the user answers, continue step by step with the next missing information:
- business goal,
- proposed solution name,
- scope of work,
- timeline,
- pricing or pricing assumptions,
- exclusions,
- special assumptions.

When enough information is available:
1. create a new brief JSON file in `/briefs`,
2. generate the offer in Markdown in `/output`,
3. convert the Markdown offer to DOCX in `/output`,
4. tell the user the exact path to the final DOCX file.

Use the existing repository assets:
- `README.md`,
- `rules/`,
- `templates/`,
- `scripts/generate_offer.py`,
- `scripts/build_docx.py`,
- reference offers in `/input`.

Do not delete existing files.
Use clean file names without spaces or Slovenian characters.
If minor information is missing, make reasonable assumptions and clearly state them.

## Strict interview wizard behavior

For offer generation, behave as a step-by-step wizard.

When the user says they want to prepare a new offer, do not list all required inputs.

Ask only the first question group and then wait for the user's answer.

### Interview sequence

Step 1:
Ask only for:
- client name,
- client address,
- offer subject.

Do not ask anything else in Step 1.

Step 2:
After the user answers Step 1, ask only for:
- business goal,
- proposed solution name.

Step 3:
After the user answers Step 2, ask only for:
- scope of work,
- main activities included in the offer.

Step 4:
After the user answers Step 3, ask only for:
- timeline,
- expected start or deadline, if relevant.

Step 5:
After the user answers Step 4, ask only for:
- price items or total price,
- monthly fee, if relevant.

Step 6:
After the user answers Step 5, ask only for:
- exclusions,
- special assumptions.

Step 7:
Summarize the collected information and ask for confirmation before generating files.

Only after confirmation:
1. create a new brief JSON file in `/briefs`,
2. generate Markdown offer in `/output`,
3. convert Markdown to DOCX in `/output`,
4. tell the user the exact final DOCX path.

### Hard rules

- Never ask all questions at once.
- Never show a full checklist of all future questions.
- Ask one step only, then wait.
- Keep each question short.
- If the user gives extra information early, store it and do not ask for it again.
- If a minor detail is missing, propose a reasonable assumption at the confirmation step.
