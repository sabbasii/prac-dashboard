import os
import json

if __name__ == "__main__":
    # Tell Django which settings file to use
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    # Initialize the Django application
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    # Import database models so they can be used in this script
    from db.models import BannedWord, Message, User
    
    with open("data/result.json", "r") as f:
        data = json.load(f)
    
    # Drop existing data
    for user in User.objects.all():
        user.delete()
    
    for message in Message.objects.all():
        message.delete()
                
    # Populate the database with new data                
    for message in data['messages']:
        #print(message.keys())
        #print(message['type'])
        #print(message['from'])
        
        if message['type'] != 'message':
            continue
        # print(message)
        
        user, _ =User.objects.get_or_create(
            id=int(message['from_id'].replace("user", "")),
            username=message['from']
        )
        
        
        plain_text = message['text']
        if not isinstance(message['text'], str):
            plain_text = ""
            for part in message['text']:
                if isinstance(part, str):
                    plain_text += part
                elif isinstance(part, dict) and 'text' in part:
                    plain_text += part['text']
        
        Message.objects.create(
            message_id=message['id'],
            text=plain_text,
            #text=message['text'],
            user=user,
            date=message['date'],
        )
        #break
            
            
