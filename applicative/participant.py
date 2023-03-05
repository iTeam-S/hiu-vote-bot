import service


class Participant:
    def __init__(
        self, id, full_univ_name, univ_name, logo_url, city, description, **kwargs
    ):
        self.id = id
        self.full_univ_name = full_univ_name
        self.univ_name = univ_name
        self.logo_url = logo_url
        self.description = description
        self.city = city

    def __repr__(self) -> str:
        return f"<Participant>{self.__dict__}"

    @staticmethod
    def from_id(_id):
        return Participant(**service.participant(_id))

    @staticmethod
    def get_full_list():
        return [Participant(**data) for data in service.participants()]

    @staticmethod
    def from_name_like(name):
        return [
            Participant(**data) for data in service.participants_from_name_like(name)
        ]
