# Tasker

This is a task CLI that I built for fun.

## Functions
Seperate each command, name, and property kwarg with a space. You can use indicies as names. The properties are: pri and proj.

- **add_task:**
    - a \[names] \*\*\[properties]
- **remove_task:**
    - r \[names]
- **modify_task:**
    - m \[names] \*\*\[properties]
        - \+ to shift prioritites up and - to shift down
        - If only properties are provided, all tasks will be modified
- **list_commands:**
    - help
