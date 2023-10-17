from lib import *
import json

def main():
    check_user_data()
    print()

    with open('data/tasks.json', 'r') as f:
        tasks = json.load(f)
    
    # initial display
    if tasks: tt_display(tasks)
    else: print('No tasks.')

    while True:
        # get commands
        cmd, names, kwargs = get_cmds(tasks)

        print(cmd)
        # execute commands
        if cmd == 'exit': break
        try:
            exec(commands[cmd])
            if tasks: tt_display(tasks)
            else: print('No tasks.')
        except KeyError:
            print('Command not found.')

if __name__ == '__main__':
    main()
    