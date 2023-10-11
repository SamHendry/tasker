from lib import *
import json

def main():
    check_user_data()

    with open('data/tasks.json', 'r') as f:
        tasks = json.load(f)
    
    while True:
        # get commands
        cmds = input('Enter a command: ')
        cmds = cmds.split(' ')
        first = cmds.pop(0)

        # execute commands
        if first == 'exit': break
        try:
            exec(commands[first])
        except KeyError:
            print('Command not found.')

if __name__ == '__main__':
    main()
    