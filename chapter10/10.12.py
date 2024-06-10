from pathlib import Path
import json
def interest_number():
    path = Path('interest_numbers.json')
    if path.exists():
        contents = path.read_text()
        numbers = json.loads(contents)
        print("number:" + numbers)
    else:
        numbers = input("Please enter an interest number:")
        contents = json.dumps(numbers)
        path.write_text(contents)
        print("number:" + numbers)

interest_number()




