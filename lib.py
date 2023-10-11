import json
import os
import termtables as tt # needs to be installed (TODO: put in requirements.txt)


commands = {
    'help': 'list_commands()',
    'a': 'add_task(tasks, *cmds)',
    'd': 'del_task(tasks, cmds)',
    'c': 'cpl_task(tasks, cmds)',
    'list': 'list_tasks(tasks)',
    'dsp': 'display_tasks(tasks)',
    'pdsp': 'tt_display(tasks)'
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
    # adds a task to the data/tasks.json file
    tasks[name] = {'do': do, 'due': due, 'prior': prior, 'proj': proj, 'notes': notes}
    save_user_data(tasks, 'tasks')
    print(f'+ Task {name} added.')


def del_task(tasks, names) -> None:
    # moves a task to the trash.json file
    with open('data/trash.json', 'r') as f:
        trash = json.load(f)
    
    for name in names:
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
    
    for name in names:
        try:
            completed[name] = tasks.pop(name)
            print(f'✓ Task {name} completed.')
        except KeyError:
            print(f'✓ Task {name} not found.')
    
    save_user_data(tasks, 'tasks')
    save_user_data(completed, 'completed')


def list_tasks(tasks) -> None:
    # lists all tasks in the tasks.json file
    for task in tasks:
        print(task, tasks[task])


def display_tasks(tasks): # rudimentary
    # displays all tasks in the tasks.json file in a table format
    print()
    print('name \t\tdo \tdue \tprior \tproj \tnotes')
    for task in tasks:
        spaces = 16-len(task)
        print(task, end=' ' * spaces)
        for attribute in tasks[task]:
            if tasks[task][attribute] is None:
                print('\t', end='')
            else:
                print(tasks[task][attribute], end='\t')
        print()
    print()


def tt_display(tasks):
    header = ['name', 'do', 'due', 'prior', 'proj', 'notes']
    # convert dic to displayable array
    data = []
    for task in tasks:
        data.append([task, tasks[task]['do'], tasks[task]['due'], tasks[task]['prior'], tasks[task]['proj'], tasks[task]['notes']])
    # display
    tt.print(data, header=header, style=tt.styles.ascii_thin_double, padding=(0, 1), alignment='c')