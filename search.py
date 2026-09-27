import json
from pathlib import Path

# Mets ici une phrase ou un mot exact du message que tu as trouvé
TEXTE_A_CHERCHER = "suis sur Discord depuis 2015"

dossier_messages = Path("./messages")
trouve = False

for sous_dossier in dossier_messages.iterdir():
    if not sous_dossier.is_dir():
        continue

    fichier_msg = sous_dossier / "messages.json"
    if fichier_msg.exists():
        try:
            with open(fichier_msg, "r", encoding="utf-8") as f:
                messages = json.load(f)

            for m in messages:
                contenu = m.get("Contents", "")
                if TEXTE_A_CHERCHER.lower() in contenu.lower():
                    print(f"\nMessage trouvé !")
                    print(f"Dossier : {sous_dossier.name}")
                    print(f"Date    : {m.get('Timestamp')}")
                    print(f"Contenu : {contenu}\n")
                    trouve = True
                    break
        except Exception:
            continue

if not trouve:
    print("Aucun message correspondant trouvé.")