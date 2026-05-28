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
