import json
import os
import termtables as tt # needs to be installed (TODO: put in requirements.txt)


commands = {
    'help': 'list_commands()',
    'a': 'add_task(tasks, names, **kwargs)',
    'r': 'remove_task(tasks, names)',
    'c': 'remove_task(tasks, names)',
    'm': 'modify_task(tasks, names, **kwargs)'
}


def list_commands() -> None:
    # lists all commands
    for command in commands:
        print(command, end=', ')
    print('exit')


def check_user_data():
    # checks for the relevant files
    # if not, creates them

    # the data folder
    if not os.path.exists('data'):
        os.mkdir('data')

    # the tasks.json file
    if not os.path.exists('data/tasks.json'):
        with open('data/tasks.json', 'w') as f:
            json.dump({}, f)

    # the trash.json file
    if not os.path.exists('data/trash.json'):
        with open('data/trash.json', 'w') as f:
            json.dump({}, f)


def save_user_data(data, z: str) -> None:
    if z == 'tasks':
        with open('data/tasks.json', 'w') as f:
            json.dump(data, f, indent=4)
    elif z == 'trash':
        with open('data/trash.json', 'w') as f:
            json.dump(data, f, indent=4)


def add_task(tasks, names, do='', due='', pri='', proj='') -> None:
    '''adds a task to the tasks.json file'''

    for name in names:
        if name in tasks:
            print(f'X Task {name} already exists.')
        else:
            tasks[name] = {
                'do': do,
                'due': due,
                'prior': pri,
                'proj': proj
            }
            print(f'+ Task {name} added.')
    
    save_user_data(tasks, 'tasks')


def modify_task(tasks, names, do=None, due=None, pri=None, proj=None) -> None:
    '''modifies a task'''

    names = list(tasks.keys()) if not names else names # support for batch modifications
        
    for name in names:
        if name not in tasks: 
            print(f'X Task {name} not found.')
            continue

        if do: tasks[name]['do'] = do
        if due: tasks[name]['due'] = due
        if pri: tasks[name]['prior'] = pri
        if proj: tasks[name]['proj'] = proj
        print(f'* Task {name} modified.')
    
    save_user_data(tasks, 'tasks')


def remove_task(tasks, names) -> None:
    # moves a task to the trash.json file
    with open('data/trash.json', 'r') as f:
        trash = json.load(f)

    for name in names:
        try:
            trash[name] = tasks.pop(name)
            print(f'- Task {name} moved to trash.')
        except KeyError:
            print(f'X Task {name} not found.')
    
    save_user_data(tasks, 'tasks')
    save_user_data(trash, 'trash')


def list_tasks(tasks) -> None:
    # lists all tasks in the tasks.json file
    for task in tasks:
        print(task, tasks[task])


def tt_display(tasks): 
    # TODO: display settings
    # TODO: fix indexes
        
    # convert dic to displayable array
    data = []
    for i, task in enumerate(tasks):
        data.append([i, task])
        data[-1].extend([element if element else '' for element in tasks[task].values()]) # there has got to be a simpler way lmao
    
    # sort by priority
    data = sorted(data, key=lambda x: x[4])

    # display
    header = [' ', 'name']; header.extend(tasks[list(tasks.keys())[0]].keys())
    tt.print(
        data, 
        header=header, 
        padding=(0, 1), 
        alignment='l')


def get_cmds(tasks) -> tuple: 
    '''processes the raw input'''

    # gets input
    user_input = input('tasker > ').split()
    cmd = user_input.pop(0)

    # gets names and kwargs
    names, kwargs = [], []
    while user_input:
        if '=' in user_input[0]: # then it's a kwarg
            kwargs.append(user_input.pop(0))
        else: # then it's a name
            names.append(user_input.pop(0))

    # if a name is an index, convert it to the real name
    for i, name in enumerate(names):
        try:
            names[i] = list(tasks.keys())[int(name)]
        except ValueError:
            pass
    
    # takes a list of kwargs and return's the corresponding dict
    kwargs_dict = {}
    for kwarg in kwargs:
        kwarg = kwarg.split('=')
        kwargs_dict[kwarg[0]] = int(kwarg[1]) if isinstance(kwarg[1], int) else kwarg[1]

    return cmd, names, kwargs_dict