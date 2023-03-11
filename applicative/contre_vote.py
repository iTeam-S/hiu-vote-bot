import service
from .voter import Voter
from .participant import Participant


class ContreVote:
    def __init__(self, voter, participant, comment=""):
        self.voter = voter
        self.participant = participant
        self.comment = comment

    def __repr__(self) -> str:
        return f"<ContreVote>{self.__dict__}"

    @property
    def can_vote(self):
        if service.contre_vote_number(self.voter) > 2:
            return False
        return True

    @staticmethod
    def from_fb_id(fb_id):
        cv_res = service.contre_vote_from_fb_id(fb_id)

        return [
            ContreVote(
                voter=Voter(**r["expand"]["voter"].__dict__),
                participant=Participant(**r["expand"]["participant"].__dict__),
                comment=r["comment"],
            )
            for r in cv_res
        ]

    def save(self):
        return service.contre_vote_save(self)
