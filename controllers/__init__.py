import ampalibe
from . import story
from . import voting
from views import app_view
from ampalibe import Payload
from .base import chat, query
from views import ParticipantView
from response import BackAndMenuButton
from ampalibe import async_simulate as simulate


@ampalibe.command("/get_started")
async def get_started(sender_id, cmd, **ext):
    chat.send_text(
        sender_id,
        "Tonga soa aman-tsara ny HIU 2023 , manasa anao hanohana ny ekipanao ",
    )
    await simulate(sender_id, "/")


@ampalibe.command("/")
def main(sender_id, **ext):
    chat.persistent_menu(sender_id, app_view.persistant_menu())
    chat.send_quick_reply(sender_id, app_view.menu(), "Hijery...")


@ampalibe.command("/participants")
def participants(sender_id, **ext):
    elems = [p.toElement() for p in ParticipantView.from_all()]
    chat.send_generic_template(sender_id, elems, next="Tohiny")


@ampalibe.command("/recherche")
def recherche(sender_id, **ext):
    chat.send_text(sender_id, "Ampidiro ny anaran'ny mpandray anjara tianao jerena")
    query.set_action(sender_id, "/recherche")


@ampalibe.action("/recherche")
def act_recherche(sender_id, cmd, **ext):
    query.set_action(sender_id, None)
    elems = [p.toElement() for p in ParticipantView.from_name(cmd)]
    if elems:
        chat.send_generic_template(sender_id, elems, next="Tohiny")
    else:
        chat.send_text(
            sender_id, "Tsy nahitana ny mpandray anjara misy anarana: " + cmd
        )
        return BackAndMenuButton(Payload("/recherche"), "Hafa 🔎")


@ampalibe.command("/apropos")
def apropos(sender_id, **ext):
    chat.send_text(sender_id, "Momban'ny HIU ( Hackathon Inter Universitaire)")
    chat.send_text(
        sender_id,
        "Lalao hifanandranan’ireo mpianatra ao amin’ny tontolon’ny informatika.",
    )
    return BackAndMenuButton()


@ampalibe.command("/historique")
def historique(sender_id, **ext):
    chat.send_quick_reply(sender_id, app_view.hiu_years(), "Taona faha firy ?")


@ampalibe.command("/about_us")
def about_us(sender_id, **ext):
    chat.send_text(
        sender_id,
        "Ity pejy ity dia natao mba ahafahanao manohana ny Oniversite mandray anjara"
        " amin'ny HIU 2023",
    )
    return BackAndMenuButton()
