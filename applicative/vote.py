import service


class Vote:
    def __init__(self, voter, participant, id=None, comment=""):
        self.id = id
        self.voter = voter
        self.participant = participant
        self.comment = comment

    def __repr__(self) -> str:
        return f"<Vote>{self.__dict__}"

    def refresh(self):
        data = service.voter_vote(self.voter, False)
        self.id = data.get("id")
        self.comment = data.get("comment")

    def can_vote(self):
        if self.voter.vote is None:
            return True

    def change_vote(self, participant, comment=None):
        self.participant = participant
        if comment:
            self.comment = comment
        self.save(update=True)

    def save(self, update=False):
        if update:
            return service.vote_update(self)
        return service.vote_save(self)
