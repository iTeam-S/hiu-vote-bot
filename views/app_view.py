from ampalibe import Payload
from ampalibe.ui import QuickReply

def menu():
    return [
        QuickReply(title='Lisitry mpandray anjara', payload=Payload('/participants')),
        QuickReply(title="Momban'ny HIU", payload=Payload('/apropos')),
        QuickReply(title="Tsiaron'ny HIU", payload=Payload('/historique')),
    ]


def is_yes(route, **payload):
    return [
        QuickReply(title="Eny", payload=Payload(route, yes=True, **payload)),
        QuickReply(title="Tsia", payload=Payload(route, yes=False, **payload)),
    ]