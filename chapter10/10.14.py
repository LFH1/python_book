from pathlib import Path
import json
def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username = input('Enter your username: ')
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        answer = input(f"is {username} your username? (y/n): ")
        if answer.lower() == 'y':
            print('Hello, ' + username + '!')
        else:
            username = get_new_username(path)
            print(f"Hello, {username}! we'll remember you")
    else:
        username = get_new_username(path)
        print(f"Hello, {username}! we'll remember you")

greet_user()







