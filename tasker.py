from lib import (tt_display, 
                 add_task, 
                 remove_task, 
                 modify_task, 
                 list_commands, 
                 get_cmds, 
                 check_user_data,
                 commands)
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
        try:
            cmd, names, kwargs = get_cmds(tasks)
        except IndexError:
            print('Please enter a valid command.')
            continue

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
    