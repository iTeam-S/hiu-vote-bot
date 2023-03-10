from ampalibe import Payload
from ampalibe.ui import QuickReply, Button, Type


def menu():
    return [
        QuickReply(
            title="Mpandray anjara đ", payload=Payload("/participants")
        ),
        QuickReply(title="Hitady đ", payload=Payload("/recherche")),
        QuickReply(title="Momban'ny HIU âšī¸", payload=Payload("/apropos")),
        QuickReply(title="Tsiaron'ny HIU đ", payload=Payload("/historique")),
    ]


def persistant_menu():
    return [
        Button(
            type=Type.postback,
            title="đ Mpandray anjara", payload=Payload("/participants")
        ),
        Button(
            type=Type.postback,
            title="đ Hijery ny safidiko",
            payload=Payload("/get_votes"),
        ),
        Button(
            type=Type.postback,
            title="âšī¸ Mombamomba anay",
            payload=Payload("/about_us"),
        ),
    ]


def is_yes(route, **payload):
    return [
        QuickReply(title="Eny â", payload=Payload(route, yes=True, **payload)),
        QuickReply(
            title="Tsia âī¸", payload=Payload(route, yes=False, **payload)
        ),
    ]


def hiu_years():
    return [
        QuickReply(title=annee, payload=Payload("/hiu_year", annee=annee))
        for annee in ("2018", "2019", "2022")
    ]
