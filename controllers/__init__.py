import ampalibe
from .base import chat

from views import app_view
from views import ParticipantView

from . import voting  


@ampalibe.command('/get_started')
def get_started(sender_id, cmd, **ext):
    # chat.send_text(sender_id, "Hello, Ampalibe")
    pass

@ampalibe.command('/')
def main(sender_id, **ext):
    chat.send_quick_reply(sender_id,  app_view.menu(), "Safidio...")

@ampalibe.command('/participants')
def participants(sender_id, **ext):
    elems = [p.toElement() for p in ParticipantView.from_all()]
    chat.send_generic_template(sender_id, elems, next=True)


@ampalibe.command('/apropos')
def apropos(sender_id, **ext):
    chat.send_text(sender_id, "Momban'ny HIU")


@ampalibe.command('/historique')
def historique(sender_id, **ext):
    chat.send_text(sender_id, "Tsiaron'ny HIU")
