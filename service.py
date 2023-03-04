from os import environ as env
from pocketbase import PocketBase

client = PocketBase('http://localhost:8090')

# Get all services
print(client.admins.auth_with_password(env.get("ADMIN_EMAIL", ""), env.get("ADMIN_PASSWORD", "")))

def _struct(data):
        data.logo_url = client.get_file_url(data, 'logo', {})
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

def voter_vote(voter):
    res = client.collection("vote").get_full_list(
        query_params={"filter": f'voter = "{voter.id}"', "expand": 'participant'}
    )
    return _struct(getattr(res[0], 'expand')['participant'])

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





