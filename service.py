from os import environ as env
from pocketbase import PocketBase
from ampalibe import Configuration as config

client = PocketBase(config.POCKET_URL)

client.admins.auth_with_password(config.ADMIN_EMAIL, config.ADMIN_PASSWORD)


def _struct(data):
    data.logo_url = client.get_file_url(data, data.logo, {})
    return data.__dict__


def participants():
    return list(
        map(
            _struct,
            client.collection("participants").get_full_list(
                query_params={"sort": "univ_name"}
            ),
        )
    )


def participants_from_name_like(name):
    return list(
        map(
            _struct,
            client.collection("participants")
            .get_list(query_params={"filter": f"(univ_name~'%{name}%')"})
            .items,
        )
    )


def participant_vote(participant):
    return map(
        lambda x: x.__dict__,
        client.collection("votes").get_full_list(
            query_params={"filter": f'participant = "{participant._id}"'}
        ),
    )


def participant(_id):
    return _struct(client.collection("participants").get_one(_id))


def voter(_id):
    return client.collection("voters").get_one(_id).__dict__


def voter_from_fb_id(fb_id):
    return client.collection("voters").get_full_list(
        query_params={"filter": f'fb_id = "{fb_id}"'}
    )


def voter_vote(voter, participant=True):
    res = client.collection("votes").get_list(
        query_params={
            "filter": f'voter = "{voter.id}"',
            "expand": "participant",
        }
    )
    return (
        (
            _struct(getattr(res.items[0], "expand")["participant"])
            if res.items
            else {}
        )
        if participant
        else res.items[0].__dict__
    )


def voter_create(fb_id, name, profil_pic):
    return (
        client.collection("voters")
        .create({"fb_id": fb_id, "name": name, "profil_pic": profil_pic})
        .__dict__
    )


def vote_save(vote):
    return client.collection("votes").create(
        {
            "voter": vote.voter.id,
            "participant": vote.participant.id,
            "comment": vote.comment,
        }
    )


def vote_update(vote):
    return client.collection("votes").update(
        vote.id,
        {
            "voter": vote.voter.id,
            "participant": vote.participant.id,
            "comment": vote.comment,
        },
    )


def contre_vote_save(contre_vote):
    return client.collection("contre_votes").create(
        {
            "voter": contre_vote.voter.id,
            "participant": contre_vote.participant.id,
            "comment": contre_vote.comment,
        }
    )


def contre_vote_number(voter):
    return len(
        client.collection("contre_votes").get_full_list(
            query_params={"filter": f'voter = "{voter.id}"'}
        )
    )


def contre_vote_from_fb_id(fb_id):
    return list(map(
        lambda x: x.__dict__,
        client.collection("contre_votes").get_full_list(
            query_params={
                "filter": f'voter.fb_id = "{fb_id}"',
            }
        ),
    ))
