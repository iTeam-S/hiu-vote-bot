import ampalibe
from controllers import chat
from ampalibe.messenger import Action


@ampalibe.before_receive()
def before_receive(sender_id, **ext):
    chat.send_action(sender_id, Action.mark_seen)
    chat.send_action(sender_id, Action.typing_on)
    return True


@ampalibe.after_receive()
def after_receive(sender_id, **ext):
    chat.send_action(sender_id, Action.typing_off)
