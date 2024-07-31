from datetime import datetime
fecha_hora_actual = datetime.now()

globalTodoList = {}
#nombre : [fecha, hora, realizado?]

def addTask(todoList, task):
    todoList[task] = [fecha_hora_actual.strftime("%Y-%m-%d"),fecha_hora_actual.strftime("%H:%M"),0]

def listTasks(todoList):
    for task in todoList:
        print(task,"---",todoList[task][0],"---",todoList[task][1],"---",("Pendiente","Realizado")[todoList[task][2]])

def markTask(todoList,task):
    if task in todoList:
        todoList[task][2]=1
    else:
        print("Task no existe.")

def clearList(todoList):
    todoList = {}

def markAllCompleted(todoList):
    for task in todoList:
        todoList[task][2] = 1