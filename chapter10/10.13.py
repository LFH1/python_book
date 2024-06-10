from pathlib import Path
import json
def greet_user():
    user = {'name': '', 'age': '', 'sex': ''}
    path = Path('user_information.json')
    if path.exists():
        contents = path.read_text()
        infomations = json.loads(contents)
        print(f"Hello {infomations['name']},age:{infomations['age']},sex:{infomations['sex']}" )
    else:
        user['name'] = input("Please input your name:")
        user['age'] = input("Please input your age:")
        user['sex'] = input("Please input your sex:")
        infomations = json.dumps(user)
        path.write_text(infomations)
        print(f"Hello {infomations['name']},age:{infomations['age']},sex:{infomations['sex']}" )

greet_user()





