import service


class Vote:
    def __init__(self, voter, participant, comment=""):
        self.voter = voter
        self.participant = participant
        self.comment = comment

    def __repr__(self) -> str:
        return f"<Vote>{self.__dict__}"

    def can_vote(self):
        if self.voter.vote is None:
            return True

    def change_vote(self, participant, comment=""):
        self.participant = participant
        self.comment = comment
        self.save(update=True)

    def save(self, update=False):
        if update:
            return service.vote_update(self)
        return service.vote_save(self)
