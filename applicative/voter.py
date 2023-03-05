import service
import pocketbase.utils
from .participant import Participant


class Voter:
    def __init__(self, id, fb_id, name, profil_pic, **kwargs):
        self.id = id 
        self.fb_id = fb_id
        self.name = name 
        self.profil_pic = profil_pic

    def __repr__(self) -> str:
        return f"<Voter>{self.__dict__}"
    
    @property
    def vote(self):
        try:
            srv = service.voter_vote(self)
        except pocketbase.utils.ClientResponseError:
            return None
        return Participant(**srv) if srv else None

    @staticmethod
    def from_id(_id):
        return Voter(**service.voter(_id))
    
    @staticmethod
    def from_fb_id(fb_id):
        res = service.voter_from_fb_id(fb_id)
        if res:
            return Voter(**res[0].__dict__)
    
    @staticmethod
    def new(fb_id, name, profil_pic):
        return Voter(**service.voter_create(fb_id, name, profil_pic))