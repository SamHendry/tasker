from lib import *
import json

def main():
    check_user_data()
    print()

    with open('data/tasks.json', 'r') as f:
        tasks = json.load(f)
    
    while True:
        # initial display
        tt_display(tasks)
        # get commands
        cmds = input('tasker > ')
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
    