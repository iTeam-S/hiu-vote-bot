from ampalibe import Payload
from ampalibe.ui import QuickReply, Button, Type


def menu():
    return [
        QuickReply(
            title="Mpandray anjara 📜", payload=Payload("/participants")
        ),
        QuickReply(title="Hitady 🔎", payload=Payload("/recherche")),
        QuickReply(title="Momban'ny HIU ℹ️", payload=Payload("/apropos")),
        QuickReply(title="Tsiaron'ny HIU 👀", payload=Payload("/historique")),
    ]


def persistant_menu():
    return [
        Button(
            type=Type.postback,
            title="📜 Mpandray anjara", payload=Payload("/participants")
        ),
        Button(
            type=Type.postback,
            title="👀 Hijery ny safidiko",
            payload=Payload("/get_votes"),
        ),
        Button(
            type=Type.postback,
            title="ℹ️ Mombamomba anay",
            payload=Payload("/about_us"),
        ),
    ]


def is_yes(route, **payload):
    return [
        QuickReply(title="Eny ✅", payload=Payload(route, yes=True, **payload)),
        QuickReply(
            title="Tsia ✖️", payload=Payload(route, yes=False, **payload)
        ),
    ]


def hiu_years():
    return [
        QuickReply(title=annee, payload=Payload("/hiu_year", annee=annee))
        for annee in ("2018", "2019", "2022")
    ]
