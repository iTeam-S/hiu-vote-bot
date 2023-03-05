import ampalibe
from ampalibe import Payload

from applicative.contre_vote import ContreVote

from .base import chat, query

from views import app_view
from applicative import Participant, Vote, Voter


@ampalibe.command("/vote")
def vote(sender_id, participant_id, **ext):
    voter = Voter.from_fb_id(sender_id)
    if not voter:
        profil = chat.get_user_profile(sender_id)
        if profil:
            voter = Voter.new(
                profil["id"],
                f"{profil['first_name']} {profil['last_name']}",
                profil["profile_pic"],
            )
        else:
            voter = Voter.new(sender_id, "User", "")
    if not voter.vote:
        chat.send_quick_reply(
            sender_id,
            app_view.is_yes("/comment_vote", participant_id=participant_id),
            "Hanampy teny fanohanana?",
        )
    elif voter.vote.id == participant_id:
        chat.send_text(
            sender_id,
            "Efa io indrindra ny safidinao 💥 \n\nMisaotra anao, tokam-po tsy miala amn'ny ekipa: "
            + voter.vote.univ_name,
        )
    else:
        chat.send_quick_reply(
            sender_id,
            app_view.is_yes("/vote_change", participant_id=participant_id),
            "Efa manana ekipa tohanina enao... ovaina ? 😱",
        )


@ampalibe.command("/vote_change")
def vote_change(sender_id, participant_id, yes, **ext):
    if yes:
        chat.send_quick_reply(
            sender_id,
            app_view.is_yes("/comment_vote", participant_id=participant_id),
            "Hanampy teny fanohanana?",
        )
    else:
        voter = Voter.from_fb_id(sender_id)
        participant = voter.vote if voter else None
        if participant:
            chat.send_text(
                sender_id,
                "Misaotra anao, tokam-po tsy miala amn'ny ekipa: "
                + participant.univ_name,
            )


@ampalibe.command("/comment_vote")
def comment_vote(sender_id, yes, participant_id, **ext):
    participant = Participant.from_id(participant_id)
    if yes:
        chat.send_text(sender_id, "Misaotra anao, Sorato ny teny fanohananao")
        query.set_action(
            sender_id, Payload("/save_vote", participant_id=participant.id)
        )
    else:
        voter = Voter.from_fb_id(sender_id)
        vote = Vote(voter, participant, "")
        vote.save()
        chat.send_text(
            sender_id,
            f"Misaotra anao, tontosa ny fanohananao an'i: {participant.univ_name}",
        )


@ampalibe.action("/save_vote")
def save_vote(sender_id, cmd, participant_id, **ext):
    participant = Participant.from_id(participant_id)
    query.set_action(sender_id, None)
    voter = Voter.from_fb_id(sender_id)
    vote = Vote(voter, participant, cmd)
    vote.save()
    chat.send_text(
        sender_id,
        f"Misaotra anao, tontosa ny fanohananao an'i: {participant.univ_name}",
    )
    chat.send_text(sender_id, "Ny teny fanohananao dia: \n\n" + cmd)


@ampalibe.command("/contre_vote")
def contre_vote(sender_id, participant_id, **ext):
    voter = Voter.from_fb_id(sender_id)
    if not voter:
        chat.send_text(
            sender_id,
            "Mila misafidy ekipa tohanina aloha vao afaka mazaka ny ekipa hafa...",
        )
        return
    participant = Participant.from_id(participant_id)

    contre_vote = ContreVote(voter, participant, "zakanay")

    if contre_vote.can_vote:
        contre_vote.save()
        chat.send_text(
            sender_id,
            f"Misaotra anao, zakanareo ny ekipa an'i: {participant.univ_name} 🙀",
        )
    else:
        chat.send_text(
            sender_id,
            f"Aoka zay 😌 Efa miotrin'ny telo ny ekipa zakanareo 🙃",
        )


@ampalibe.command("/description")
def description(sender_id, participant_id, **ext):
    participant = Participant.from_id(participant_id)
    chat.send_text(sender_id, participant.description)