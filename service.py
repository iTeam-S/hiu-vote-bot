from os import environ as env
from pocketbase import PocketBase

client = PocketBase(env.get("POCKET_URL", ""))

# Get all services
print(client.admins.auth_with_password(env.get("ADMIN_EMAIL", ""), env.get("ADMIN_PASSWORD", "")))

def _struct(data):
        data.logo_url = client.get_file_url(data, data.logo, {})
        return data.__dict__

def participants():
    return list(map(_struct, client.collection("participant").get_full_list()))

def participant_vote(participant):
    return map(lambda x: x.__dict__, client.collection("vote").get_full_list(
        query_params={"filter": f'participant = "{participant._id}"'}
    ))

def participant(_id):
    return client.collection("participant").get_one(_id).__dict__

def voter(_id):
    return client.collection("voter").get_one(_id).__dict__

def voter_from_fb_id(fb_id):
    return client.collection("voter").get_full_list(
        query_params={"filter": f'fb_id = "{fb_id}"'}
    )

def voter_vote(voter):
    res = client.collection("vote").get_full_list(
        query_params={"filter": f'voter = "{voter.id}"', "expand": 'participant'}
    )
    return _struct(getattr(res[0], 'expand')['participant'])

def voter_create(fb_id, name, profil_pic):
    return client.collection("voter").create({
        "fb_id": fb_id,
        "name": name,
        "profil_pic": profil_pic
    }).__dict__

def vote_save(vote):
    return client.collection("vote").create({
        "voter": vote.voter.id,
        "participant": vote.participant.id,
        "comment": vote.comment
    })

def vote_update(vote):
    return client.collection("vote").update(vote.id, {
        "voter": vote.voter.id,
        "participant": vote.participant.id,
        "comment": vote.comment
    })





