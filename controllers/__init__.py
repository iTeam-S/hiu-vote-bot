import ampalibe
from .base import chat, query

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
    chat.send_generic_template(sender_id, elems, next="Tohiny")


@ampalibe.command('/recherche')
def recherche(sender_id, **ext):
    chat.send_text(sender_id, "Ampidiro ny anaran'ny mpandray anjara tianao jerena")
    query.set_action(sender_id, 'recherche')


@ampalibe.action('recherche')
def act_recherche(sender_id, cmd, **ext):
    query.set_action(sender_id, None)
    elems = [p.toElement() for p in ParticipantView.from_name(cmd)]
    chat.send_generic_template(sender_id, elems, next="Tohiny")


@ampalibe.command('/apropos')
def apropos(sender_id, **ext):
    chat.send_text(sender_id, "Momban'ny HIU")


@ampalibe.command('/historique')
def historique(sender_id, **ext):
    chat.send_text(sender_id, "Tsiaron'ny HIU")
