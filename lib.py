import json
import os


commands = {
    'help': 'list_commands()',
    'add': 'add_task(tasks, *cmds)',
    'del': 'del_task(tasks, cmds)',
    'cpl': 'cpl_task(tasks, cmds)',
    'list': 'list_tasks(tasks)',
    'display': 'display_tasks(tasks)',
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


def add_task(tasks, name, do=None, due=None, prior=None, proj=None) -> None:
    # adds a task to the data/tasks.json file
    tasks[name] = {'do': do, 'due': due, 'prior': prior, 'proj': proj}
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
            print(f' Task {name} completed.')
        except KeyError:
            print(f' Task {name} not found.')
    
    save_user_data(tasks, 'tasks')
    save_user_data(completed, 'completed')


def list_tasks(tasks) -> None:
    # lists all tasks in the tasks.json file
    for task in tasks:
        print(task, tasks[task])


def display_tasks(tasks):
    # displays all tasks in the tasks.json file in a table format
    print()
    print('name \t\tdo \tdue \tprior \taproj')
    for task in tasks:
        spaces = 16-len(task)
        print(task, end=' ' * spaces)
        for key in tasks[task]:
            print(tasks[task][key], end='\t')
        print()
    print()