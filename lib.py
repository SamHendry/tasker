import json
import os
import termtables as tt # needs to be installed (TODO: put in requirements.txt)


commands = {
    'help': 'list_commands()',
    'a': 'add_task(tasks, names, **kwargs)',
    'r': 'remove_task(tasks, names)',
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
    if not os.path.exists('data/trash.txt'):
        with open('data/trash.txt', 'w') as f:
            f.write('')


def sort_tasks(tasks, sort_by='pri') -> None: #TODO: can modify to sort by dates later
    '''sorts tasks by sort_by'''
    task_list = list(tasks.items())
    task_list.sort(key=lambda x: x[1][sort_by] if x[1][sort_by] else '999')
    tasks.clear()
    tasks.update(dict(task_list))


def save_user_data(data, z: str) -> None:
    '''sorts and saves data to the relevant file'''

    if z == 'tasks':
        sort_tasks(data)
        with open('data/tasks.json', 'w') as f:
            json.dump(data, f, indent=4)
    elif z == 'trash':
        with open('data/trash.txt', 'a') as f:
            f.write(repr(data) + '\n')


def process_time(date: str): # TODO: implement using datetime
    pass


def add_task(tasks, names, do='', due='', pri='', proj='') -> None:
    '''adds a task to the tasks.json file'''

    for name in names:
        if name in tasks:
            print(f'X Task {name} already exists.')
        else:
            tasks[name] = {
                'do': do, # TODO: procces time function call
                'due': due, # TODO: process time function call
                'pri': pri,
                'proj': proj
            }
            print(f'+ Task {name} added.')
    
    save_user_data(tasks, 'tasks')


def modify_task(tasks, names, name=None, do=None, due=None, pri=None, proj=None) -> None:
    '''modifies a task'''

    names = list(tasks.keys()) if not names else names # support for batch modifications
        
    for edit_name in names:
        if edit_name not in tasks: 
            print(f'X Task {edit_name} not found.')
            continue
        
        if name: tasks[name] = tasks.pop(edit_name)
        if do: tasks[edit_name]['do'] = do
        if due: tasks[edit_name]['due'] = due
        if pri: tasks[edit_name]['pri'] = pri
        if proj: tasks[edit_name]['proj'] = proj
        print(f'* Task {edit_name} modified.')
    
    save_user_data(tasks, 'tasks')


def remove_task(tasks, names) -> None:
    # moves a task to the trash.json file
    if names == ['a']:
        names = list(tasks.keys())
    removed = []
    for name in names:
        try:
            removed.append(tasks.pop(name))
            print(f'- Task {name} moved to trash.')
        except KeyError:
            print(f'X Task {name} not found.')
    
    save_user_data(tasks, 'tasks')
    save_user_data(removed, 'trash')


def tt_display(tasks): 
    # TODO: display settings
    # TODO: fix indexes
        
    # convert dic to displayable array
    data = []
    for i, task in enumerate(tasks):
        data.append([i, task])
        data[-1].extend([element for element in tasks[task].values()])

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
    # TODO: fix indexes
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
