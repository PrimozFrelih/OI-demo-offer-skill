import json
import sys
from pathlib import Path


COMPANY_BLOCK = """Orka Informatika d.o.o.  
Ulica Štefana Kovača 10  
9000 Murska Sobota
"""


def money(value):
    return f"{value:,.2f} EUR".replace(",", "X").replace(".", ",").replace("X", ".")


def render_offer(brief):
    price_items = brief.get("price_items", [])
    total = sum(item.get("amount_eur", 0) for item in price_items)

    scope_lines = "\n".join([f"- {item}" for item in brief.get("scope", [])])
    exclusion_lines = "\n".join([f"- {item}" for item in brief.get("exclusions", [])])
    assumption_lines = "\n".join([f"- {item}" for item in brief.get("special_assumptions", [])])

    price_rows = "\n".join(
        [f"| {item.get('name', '')} | {money(item.get('amount_eur', 0))} |" for item in price_items]
    )

    monthly_fee = brief.get("monthly_fee_eur")
    monthly_fee_text = ""
    if monthly_fee:
        monthly_fee_text = (
            f"\n\nMesečna naročnina za uporabo in osnovno vzdrževanje rešitve znaša "
            f"**{money(monthly_fee)} mesečno**. Vključuje osnovno podporo, gostovanje, "
            f"varnostne kopije in redne manjše posodobitve sistema."
        )

    return f"""# {brief.get('offer_title', 'Ponudba')}

**{COMPANY_BLOCK}**

**PONUDBA št. {brief.get('offer_number', '')}**  
**Za naročnika: {brief.get('client_name', '')}**  
{brief.get('client_address', '')}

Murska Sobota, {brief.get('date', '')}

## 1. Namen sodelovanja

Namen sodelovanja je {brief.get('project_goal', '').strip()}

Projekt je zastavljen kot praktična uvedba poslovne rešitve, kjer se najprej uredijo ključni procesi, nato pa se rešitev po potrebi nadgrajuje z dodatnimi funkcionalnostmi, integracijami in poročili.

## 2. Predmet ponudbe

Predmet ponudbe je priprava in uvedba rešitve **{brief.get('solution_name', '')}**.

Rešitev je namenjena podpori dogovorjenemu poslovnemu procesu naročnika in boljši sledljivosti dela, podatkov ter odgovornosti med uporabniki.

## 3. Obseg dela

V ponudbo so vključene naslednje aktivnosti:

{scope_lines}

## 4. Terminski okvir

Predviden terminski okvir izvedbe je **{brief.get('timeline', '')}** od potrditve ponudbe in prejema vseh potrebnih vhodnih informacij.

Terminski okvir je odvisen od razpoložljivosti ključnih uporabnikov naročnika, pravočasnega potrjevanja vsebinskih odločitev in kakovosti vhodnih podatkov.

## 5. Cena

Predvidena vrednost projekta znaša:

| Postavka | Vrednost |
|---|---:|
{price_rows}
| **Skupaj** | **{money(total)}** |

Cene ne vključujejo DDV.{monthly_fee_text}

## 6. Pogoji plačila

Predlagani plačilni pogoji:

{brief.get('payment_terms', '')}

Rok plačila posameznega računa je 15 dni od izdaje računa.

## 7. Odgovornosti naročnika

Naročnik zagotovi pravočasno sodelovanje ključnih uporabnikov, dostop do potrebnih informacij, vsebinske potrditve in testiranje rešitve.

Posebne predpostavke:

{assumption_lines}

## 8. Izključitve

Ponudba ne vključuje:

{exclusion_lines}

Dodatne zahteve se obravnavajo kot sprememba obsega in se ocenijo posebej.

## 9. Pravice in uporaba

Po plačilu vseh obveznosti naročnik pridobi pravico do uporabe razvite rešitve za lastne poslovne potrebe. Prenos izvorne kode, materialnih avtorskih pravic ali posebne licenčne ureditve se opredeli z ločenim dogovorom, če je to potrebno.

## 10. Veljavnost ponudbe

Ponudba velja 30 dni od datuma izdaje.

Za Orka Informatika d.o.o.  
**mag. Primož Frelih, PMP**  
Vodja projektov in svetovalec za digitalizacijo
"""


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/generate_offer.py <brief.json> <output.md>")
        sys.exit(1)

    brief_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not brief_path.exists():
        print(f"Brief file not found: {brief_path}")
        sys.exit(1)

    brief = json.loads(brief_path.read_text(encoding="utf-8"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_offer(brief), encoding="utf-8")

    print(f"Generated {output_path}")


if __name__ == "__main__":
    main()
