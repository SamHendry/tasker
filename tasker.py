from lib import *
import json

def main():
    check_user_data()
    print()

    with open('data/tasks.json', 'r') as f:
        tasks = json.load(f)
    
    # initial display
    tt_display(tasks)

    while True:
        # get commands
        first, cmds = get_process_cmds()

        # execute commands
        if first == 'exit': break
        try:
            exec(commands[first])
            tt_display(tasks)
        except KeyError:
            print('Command not found.')

if __name__ == '__main__':
    main()
    