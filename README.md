# Orka Offer Skill

Reusable offer-generation package for Orka Informatika d.o.o.

## Purpose

This repo turns reference offers into a repeatable process for creating new business offers.

## Workflow

1. Put reference offers into `/input`.
2. Extract structure and content patterns.
3. Maintain reusable rules in `/rules`.
4. Generate a new offer as Markdown.
5. Convert the final version to DOCX.
6. Save generated files to `/output`.

## Repository structure

- `/input` - reference DOCX offers
- `/extracted` - extracted plain text from DOCX files
- `/rules` - reusable business, pricing, style and legal rules
- `/templates` - reusable offer templates
- `/examples` - summaries and reference examples
- `/scripts` - helper scripts
- `/output` - generated offers

## Inputs needed for a new offer

- client name
- offer topic
- project goal
- scope
- expected timeline
- pricing model
- exclusions
- special legal or technical assumptions
