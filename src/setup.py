import json

def get_token():
    file = open('secrets.json', 'r')
    token = json.load(file).get('DiscordKey')
    file.close()
    return token

def get_admin():
    file = open('secrets.json', 'r')
    admin = json.load(file).get('AdminUsers')
    file.close()
    return admin
