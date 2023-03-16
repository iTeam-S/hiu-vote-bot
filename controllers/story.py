import ampalibe
from .base import chat
from ampalibe import Payload
from response import BackAndMenuButton

data = {
    "2018": """
- Volohany : 🥇 CNTEMAD
- Faharoa : 🥈 IT University
- Fahatelo : 🥉 ESPA
Coup de coeur : ♥️ EMIT 
""",
    "2019": """
- Volohany : 🥇 EMIT
- Faharoa : 🥈 IT University
- Fahatelo : 🥉 ESPA
""",
    "2022": """
- Volohany : 🥇 ISPM
- Faharoa : 🥈 ESTI
- Fahatelo : 🥉 EMIT
Coup de coeur : ♥️ EMIT
""",
}


@ampalibe.command("/hiu_year")
def hiu_year(sender_id, annee, **ext):
    chat.send_text(sender_id, "Momban'ny HIU " + annee)
    chat.send_text(sender_id, data[annee])
    return BackAndMenuButton(Payload("/historique"), "Taona Hafa ? ")
