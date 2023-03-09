# Imports
from objects.userStats import UserStats
from objects.schedule import Schedule
from datetime import datetime

# user status
session:str = ''
sessionName:str = ''

# supplementary function
def toolUser():
    try:
        user = str(input('User: '))
        while len(user) < 1:
            print('Try again...')
            user = str(input('User: '))

        password = str(input('Password: '))
        while len(password) < 1 or len(password) > 16:
            print('Try again...')
            password = str(input('Password: '))
        return user, password
    except:
        print('There was some error...')
        start()

# user panel function
def panel():
    esc = str(input(f'\n****** User Panel ******\n -- Welcome {sessionName}\nSchedule Tasks (1)\nView Tasks (2)\nModify Tasks (3)\nExit (4)\n'))
    if esc == '1':
        scheduleTasks()

# task scheduling function
def scheduleTasks():
    try:
        taskName = str(input('\nTask name: '))
        while len(taskName) < 1:
            print('Try again...')
            taskName = str(input('Task name: '))

        taskDescription = str(input('Task description: '))
        while len(taskDescription) < 1:
            print('Try again...')
            taskDescription = str(input('Task description: '))

        try:
            str_date = str(input('Ex: 01/01/0001\ntaskDuration: '))
            while int(str_date[-4::]) < 2023:
                print('\nWrong year!\n') 
                str_date = str(input('Ex: 01/01/0001\ntaskDuration: '))
            taskDuration = datetime.strptime(str_date, '%d/%m/%Y').date()
        except:
            print('\nIncorrect date format!')
            scheduleTasks()

        esc = str(input(f'\nTask Name: {taskName}\nTask Description: {taskDescription}\nTask Duration: {str_date}\nConfirm task creation S/N\n')).lower()
        if esc == 's':
            user = sessionName
            if user == '':
                print('\nThere was some error...')
                panel()
            obj = Schedule(taskName, taskDescription, taskDuration, user)
            if obj.registerTask() == True:
                print("Task successfully registered!")
                panel()
            else:
                print('\nThere was some error...')
                panel()
        else:
            panel()

    except NameError:
        print('\nThere was some error...')
        panel()

# start function
def start():
    esc = str(input(('\n****** Task Scheduling ******\nLogin (1)\nRegister (2)\nUser Panel (3)\nExit (4)\n')))
    if esc == '1':
        sign()
    elif esc == '2':
        register()
    elif esc == '3': 
        if session == 'start':
            panel()
        else:
            print('User not logged in!')
            start()
    elif esc == '4':
        print('Leaving...')
        exit()
    else:
        start()

# sign-in function
def sign():
    global session, sessionName
    print('***** Sign-In ******')
    try:
        toolReturn = toolUser()
        user = toolReturn[0]
        password = toolReturn[1]
        method = 0
        obj = UserStats(user, password, method)
        if obj.userVerify() == True:
            print('User logged successfully!')
            session = 'start'
            sessionName = obj.user
            panel()
        else:
            print('Incorrect username or password, try again.')
            start()
    except:
        print('\nThere was some error...')
        start()

# register function
def register():
    global session, sessionName
    print('\n***** Register ******')
    try:
        toolReturn = toolUser()
        user = toolReturn[0]
        password = toolReturn[1]
        method = 1
        obj = UserStats(user, password, method)
        if obj.userVerify() == True:
            obj.registerUser()
            session = 'start'
            sessionName = obj.user
            panel()
        else:
            register()
    
    except NameError:
        print('There was some error...')
        start()
        


# call functions
start()