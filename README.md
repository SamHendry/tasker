# Tasker

This is a small task manager that I built for fun. It saves your tasks in a json file and you can interact with them by running the tasker.py script from the command line. [Mdtask](https://github.com/SamHendry/mdtask) will be a more mature version of this that saves to markdown and includes a time system.

## Functions
Seperate each command, name, and property kwarg with a space. You can use indicies as names. The properties are: pri and proj.

- **add_task:**
    - a \[names] \*\*\[properties]
- **remove_task:**
    - r \[names]
    - "r a" will remove all tasks
- **modify_task:**
    - m \[names] \*\*\[properties]
        - \+ to shift prioritites up and - to shift down
        - If only properties are provided, all tasks will be modified
- **list_commands:**
    - help
