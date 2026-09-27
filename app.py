from flask import Flask, render_template, jsonify
from pathlib import Path
import json

app = Flask(__name__)
MESSAGES_DIR = Path("./messages")
INDEX_FILE = MESSAGES_DIR / "index.json"

def load_index():
    if INDEX_FILE.exists():
        try:
            with open(INDEX_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def get_channels_list():
    channels = []
    if not MESSAGES_DIR.exists():
        return channels

    index_map = load_index()

    for folder in MESSAGES_DIR.iterdir():
        if not folder.is_dir():
            continue
        
        c_id = folder.name
        # Si le dossier a un préfixe comme 'c123456', on extrait la clé numérique pour index.json
        clean_id = c_id[1:] if c_id.startswith("c") and c_id[1:].isdigit() else c_id
        
        c_file = folder / "channel.json"
        m_file = folder / "messages.json"
        
        # Vérifie qu'il y a bien des messages à lire
        if m_file.exists():
            # 1. Priorité au mapping de index.json
            name = index_map.get(clean_id) or index_map.get(c_id)
            
            # 2. Repli sur channel.json si présent
            if not name and c_file.exists():
                try:
                    with open(c_file, "r", encoding="utf-8") as f:
                        c_data = json.load(f)
                    name = c_data.get("name")
                    if not name:
                        recipients = c_data.get("recipients", [])
                        name = f"Discussion ({len(recipients)} pers.)" if recipients else None
                except Exception:
                    pass

            if not name:
                name = f"Salon {c_id}"

            # Détecter si c'est un MP pour extraire le pseudo du contact
            is_dm = "Direct Message with" in name
            dm_user = name.replace("Direct Message with", "").strip() if is_dm else None

            channels.append({
                "id": c_id,
                "name": name,
                "is_dm": is_dm,
                "dm_user": dm_user
            })

    return sorted(channels, key=lambda x: str(x["name"]).lower())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/channels")
def api_channels():
    return jsonify(get_channels_list())

@app.route("/api/channel/<folder_id>")
def api_channel_messages(folder_id):
    folder_path = MESSAGES_DIR / Path(folder_id).name
    m_file = folder_path / "messages.json"

    if not m_file.exists():
        return jsonify({"error": "Salon introuvable"}), 404

    try:
        with open(m_file, "r", encoding="utf-8") as f:
            messages = json.load(f)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Tri chronologique (du plus ancien au plus récent)
    messages_sorted = sorted(messages, key=lambda m: m.get("Timestamp", ""))
    return jsonify(messages_sorted)

if __name__ == "__main__":
    print("Application démarrée sur http://127.0.0.1:5000")
    app.run(port=5000, debug=True)