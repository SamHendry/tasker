import json
import os
import termtables as tt # needs to be installed (TODO: put in requirements.txt)


commands = {
    'help': 'list_commands()',
    'a': 'add_task(tasks, *cmds)',
    'd': 'del_task(tasks, cmds)',
    'c': 'cpl_task(tasks, cmds)'
}


def list_commands() -> None:
    # lists all commands
    for command in commands:
        print(command, end=', ')
    print('exit')


def check_user_data():
    # checks for the relevant files
    # if not, creates them

    # the tasks.json file
    if not os.path.exists('data/tasks.json'):
        print('No tasks.json file found. Creating a new one...')
        with open('data/tasks.json', 'w') as f:
            json.dump({}, f)

    # the trash.json file
    if not os.path.exists('data/trash.json'):
        print('No trash.json file found. Creating a new one...')
        with open('data/trash.json', 'w') as f:
            json.dump({}, f)
    
    # the completed.json file
    if not os.path.exists('data/completed.json'):
        print('No completed.json file found. Creating a new one...')
        with open('data/completed.json', 'w') as f:
            json.dump({}, f)


def save_user_data(data, z: str) -> None:
    if z == 'tasks':
        with open('data/tasks.json', 'w') as f:
            json.dump(data, f, indent=4)
    elif z == 'trash':
        with open('data/trash.json', 'w') as f:
            json.dump(data, f, indent=4)
    elif z == 'completed':
        with open('data/completed.json', 'w') as f:
            json.dump(data, f, indent=4)


def add_task(tasks, name, do=None, due=None, prior=None, proj=None, notes=None) -> None:
    # adds a task to the tasks.json file
    # TODO: add way to interact with just a single task attributeas
    tasks[name] = {'do': do, 'due': due, 'prior': prior, 'proj': proj, 'notes': notes}
    save_user_data(tasks, 'tasks')
    print(f'+ Task {name} added.')


def check_for_indexes(tasks, names) -> list:
    # checks if the names are indexes
    # returns a list of the names
    for i, name in enumerate(names):
        if type(name) is int: names[i] = list(tasks.keys())[name]
    return names


def del_task(tasks, names) -> None:
    # moves a task to the trash.json file
    with open('data/trash.json', 'r') as f:
        trash = json.load(f)

    for name in check_for_indexes(tasks, names):
        try:
            trash[name] = tasks.pop(name)
            print(f'- Task {name} moved to trash.')
        except KeyError:
            print(f'- Task {name} not found.')
    
    save_user_data(tasks, 'tasks')
    save_user_data(trash, 'trash')


def cpl_task(tasks, names) -> None:
    # moves a task to the completed.json file
    with open('data/completed.json', 'r') as f:
        completed = json.load(f)
    
    for name in check_for_indexes(tasks, names):
        try:
            completed[name] = tasks.pop(name)
            print(f'✓ Task {name} completed.')
        except KeyError:
            print(f'✓ Task {name} not found.')
    
    save_user_data(tasks, 'tasks')
    save_user_data(completed, 'completed')


# TODO: modify task function


def list_tasks(tasks) -> None:
    # lists all tasks in the tasks.json file
    for task in tasks:
        print(task, tasks[task])


def tt_display(tasks):
    header = [' ', 'name', 'do', 'due', 'prior', 'proj', 'notes'] #TODO: generate this instead of hardcoding
    # convert dic to displayable array
    data = []
    for i, task in enumerate(tasks):
        data.append([
            i,
            task, 
            tasks[task]['do'], 
            tasks[task]['due'], 
            tasks[task]['prior'], 
            tasks[task]['proj'], 
            tasks[task]['notes']
        ])
    # display
    tt.print(
        data, 
        header=header, 
        padding=(0, 1), 
        alignment='l')
    

def get_process_cmds() -> tuple: 
    #TODO: redo command system to handle explicit calls to change/delete specifc attributes and tasks
    # processes the commands
    # returns a list of the commands
    cmds = input('tasker > ').split()
    for i, cmd in enumerate(cmds):
        # if the string contains only numbers, change it to an int
        if cmd.isdigit():
            cmds[i] = int(cmd)
        else:
            # turns dashes into spaces
            cmds[i] = cmd.replace('-', ' ')

    return cmds[0], cmds[1:]