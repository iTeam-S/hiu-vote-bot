from ampalibe import Payload
from applicative import Participant
from ampalibe.ui import Type, Button, Element


class ParticipantView(Participant):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def from_all():
        return [ParticipantView(**p.__dict__) for p in Participant.get_full_list()]

    @staticmethod
    def from_name(name):
        return [ParticipantView(**p.__dict__) for p in Participant.from_name_like(name)]

    def toElement(self):
        return Element(
            title=f"{self.univ_name} ({self.city})",
            subtitle=self.full_univ_name,
            image_url=self.logo_url,
            buttons=[
                Button(
                    type=Type.postback,
                    title="Alaiko 🔥 ...",
                    payload=Payload("/vote", participant_id=self.id),
                ),
                Button(
                    type=Type.postback,
                    title="Zakanay 🦾 ...",
                    payload=Payload("/contre_vote", participant_id=self.id),
                ),
                Button(
                    type=Type.postback,
                    title="Mombamomba ℹ️",
                    payload=Payload("/description", participant_id=self.id),
                ),
            ],
        )
