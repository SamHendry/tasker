import json
import os

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


def add_task(name, do=None, due=None, prior=None, proj=None) -> None:
    # adds a task to the data/ file
    with open('data/tasks.json', 'r+') as f:
        tasks = json.load(f)
        tasks[name] = {'do': do, 'due': due, 'prior': prior, 'proj': proj}
        f.seek(0)
        json.dump(tasks, f, indent=4)
        f.truncate()
        print(f'+ Task {name} added.')


def del_task(names) -> None:
    # moves a task to the trash.json file
    with open('data/tasks.json', 'r+') as f:
        with open('data/trash.json', 'r+') as f2:
            tasks = json.load(f)
            for name in names:
                if name in tasks:
                    trash = json.load(f2)
                    trash[name] = tasks[name]
                    f2.seek(0)
                    json.dump(trash, f2, indent=4)
                    f2.truncate()
                    del tasks[name]
                    f.seek(0)
                    json.dump(tasks, f, indent=4)
                    f.truncate()
                    print(f'+ Task {name} moved to trash.')
                else:
                    print(f'+ Task {name} not found.')


def cpl_task(names) -> None:
    # moves a task to the completed.json file
    with open('data/tasks.json', 'r+') as f:
        with open('data/completed.json', 'r+') as f2:
            tasks = json.load(f)
            for name in names:
                if name in tasks:
                    completed = json.load(f2)
                    completed[name] = tasks[name]
                    f2.seek(0)
                    json.dump(completed, f2, indent=4)
                    f2.truncate()
                    del tasks[name]
                    f.seek(0)
                    json.dump(tasks, f, indent=4)
                    f.truncate()
                    print(f'+ Task {name} completed.')
                else:
                    print(f'+ Task {name} not found.')


def list_tasks() -> None:
    # lists all tasks in the tasks.json file
    with open('data/tasks.json', 'r') as f:
        tasks = json.load(f)
        for task in tasks:
            print(task, tasks[task])
