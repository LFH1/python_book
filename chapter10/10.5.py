from pathlib import Path
path = Path('guest_book.txt')
active = 1
content = ''
while active:
    name = input('Enter your name or press q to quit: ')
    if name == 'q':
        break
    else:
        content = content + name + '\n'
for line in content.splitlines():
    print('hello ' + line)



