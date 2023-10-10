from lib import *

def main():
    check_user_data()

    while True:
        cmds = input('Enter a command: ')

        cmds = cmds.split(' ')
        if cmds[0] == 'add':
            add_task(*cmds[1:])
        elif cmds[0] == 'del':
            del_task(cmds[1:])
        elif cmds[0] == 'cpl':
            cpl_task(cmds[1:])
        elif cmds[0] == 'list':
            list_tasks()
        elif cmds[0] == 'exit':
            print('Exiting...')
            break
        else:
            print('Invalid command.')

if __name__ == '__main__':
    main()
    