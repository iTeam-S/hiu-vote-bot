import service


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

    def save(self):
        return service.contre_vote_save(self)