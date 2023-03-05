import ampalibe
from ampalibe import Payload
from ampalibe import Messenger, Model

from views import app_view
from views import ParticipantView

from applicative import Vote, Voter

chat = Messenger()
query = Model()


@ampalibe.command('/get_started')
def get_started(sender_id, cmd, **ext):
    # chat.send_text(sender_id, "Hello, Ampalibe")
    pass

@ampalibe.command('/')
def main(sender_id, cmd, **ext):
    chat.send_quick_reply(sender_id,  app_view.menu(), "Safidio...")

@ampalibe.command('/participants')
def participants(sender_id, cmd, **ext):
    elems = [p.toElement() for p in ParticipantView.from_all()]
    chat.send_generic_template(sender_id, elems, next=True)

@ampalibe.command('/vote')
def vote(sender_id, participant, **ext):
    voter = Voter.from_fb_id(sender_id)
    if not voter:
        profil = chat.get_user_profile(sender_id)
        if profil:
            Voter.new(profil['id'], f"{profil['first_name']} {profil['last_name']}", profil['profile_pic'])
        else:
            Voter.new(sender_id, "User", "")
    chat.send_quick_reply(sender_id, app_view.is_yes('/comment_vote', participant=participant), "Hanampy teny fanohanana?")


@ampalibe.command('/comment_vote')
def comment_vote(sender_id, yes, participant, **ext):
    if yes:
        chat.send_text(sender_id, "Misaotra anao, Sorato ny teny fanohananao")
        query.set_action(sender_id, Payload('/save_vote', participant=participant))
    else:
        voter = Voter.from_fb_id(sender_id)
        vote = Vote(voter, participant, "")
        vote.save()
        chat.send_text(sender_id, f"Misaotra anao, tontosa ny fanohananao an'i: {participant.univ_name}")


@ampalibe.action('/save_vote')
def save_vote(sender_id, cmd, participant, **ext):
    query.set_action(sender_id, None)
    voter = Voter.from_fb_id(sender_id)
    vote = Vote(voter, participant, cmd)
    vote.save()
    chat.send_text(sender_id, f"Misaotra anao, tontosa ny fanohananao an'i: {participant.univ_name}")
    chat.send_text(sender_id, "Ny teny fanohananao dia: \n\n" + cmd)