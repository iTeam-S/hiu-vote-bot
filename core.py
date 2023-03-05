import ampalibe
from controllers import chat

# create a get started option to get permission of user.
# chat.get_started('/get_started')

@ampalibe.before_receive()
def before_receive(sender_id, **ext):
    # do something before receive message
    
    return True

@ampalibe.after_receive()
def after_receive(sender_id, **ext):
    # do something after receive message
    pass


    
