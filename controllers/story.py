import ampalibe
from .base import chat

data = {
    "2018": """
- 1e : CNTEMAD
- 2e : IT University
- 3e : ESPA
Coup de coeur : EMIT 
""",
    "2019": """
- 1e : EMIT
- 2e : IT University
- 3e : ESPA
""",
    "2022": """
- 1e : ISPM
- 2e : ESTI
- 3e : EMIT
Coup de coeur : EMIT
""",
}


@ampalibe.command("/hiu_year")
def hiu_year(sender_id, annee, **ext):
    chat.send_text(sender_id, "Momban'ny HIU " + annee)
    chat.send_text(sender_id, data[annee])
