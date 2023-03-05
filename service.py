from os import environ as env
from pocketbase import PocketBase

client = PocketBase(env.get("POCKET_URL", ""))

client.admins.auth_with_password(
    env.get("ADMIN_EMAIL", ""), env.get("ADMIN_PASSWORD", "")
)


def _struct(data):
    data.logo_url = client.get_file_url(data, data.logo, {})
    return data.__dict__


def participants():
    return list(map(_struct, client.collection("participant").get_full_list()))


def participants_from_name_like(name):
    return list(
        map(
            _struct,
            client.collection("participant")
            .get_list(query_params={"filter": f"(univ_name~'%{name}%')"})
            .items,
        )
    )


def participant_vote(participant):
    return map(
        lambda x: x.__dict__,
        client.collection("vote").get_full_list(
            query_params={"filter": f'participant = "{participant._id}"'}
        ),
    )


def participant(_id):
    return _struct(client.collection("participant").get_one(_id))


def voter(_id):
    return client.collection("voter").get_one(_id).__dict__


def voter_from_fb_id(fb_id):
    return client.collection("voter").get_full_list(
        query_params={"filter": f'fb_id = "{fb_id}"'}
    )


def voter_vote(voter):
    res = client.collection("vote").get_full_list(
        query_params={"filter": f'voter = "{voter.id}"', "expand": "participant"}
    )
    return _struct(getattr(res[0], "expand")["participant"])


def voter_create(fb_id, name, profil_pic):
    return (
        client.collection("voter")
        .create({"fb_id": fb_id, "name": name, "profil_pic": profil_pic})
        .__dict__
    )


def vote_save(vote):
    return client.collection("vote").create(
        {
            "voter": vote.voter.id,
            "participant": vote.participant.id,
            "comment": vote.comment,
        }
    )


def vote_update(vote):
    return client.collection("vote").update(
        vote.id,
        {
            "voter": vote.voter.id,
            "participant": vote.participant.id,
            "comment": vote.comment,
        },
    )


def contre_vote_save(contre_vote):
    return client.collection("contre_vote").create(
        {
            "voter": contre_vote.voter.id,
            "participant": contre_vote.participant.id,
            "comment": contre_vote.comment,
        }
    )


def contre_vote_number(voter):
    return len(
        client.collection("contre_vote").get_full_list(
            query_params={"filter": f'voter = "{voter.id}"'}
        )
    )
