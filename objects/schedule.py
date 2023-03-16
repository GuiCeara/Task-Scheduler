from objects.connection import Con
from datetime import date

objectCon = Con()
cursor = objectCon.mycursor
mydb = objectCon.mydb

class Schedule():
    
    user:str = ''
    taskName:str = ''
    taskDescription:str = ''

    def __init__(self, taskName, taskDescription, taskDuration, user) -> None:
        self.taskName = taskName
        self.taskDescription = taskDescription
        self.taskDuration = taskDuration
        self.user = user

    def registerTask(self) -> bool:

        sql = "INSERT INTO tarefa (id, nome, descricao, tempoduracao, fk_usuario_user) VALUES (%s, %s, %s, %s, %s)"
        val = (0, self.taskName, self.taskDescription, self.taskDuration, self.user)
        cursor.execute(sql, val)
        mydb.commit()
        return True

    @classmethod
    def listTasks(cls, user):

        current_date = date.today()
        current_date = format(current_date, "%d/%m/%Y")
        cursor.execute(f"SELECT * FROM tarefa WHERE fk_usuario_user = '{user}' " )
        myresult = cursor.fetchall()
        for x in myresult:
            dateTask = x[3]
            dateTask = format(dateTask, "%d/%m/%Y")
            if current_date > dateTask:
                status = 'Inactive'
            else:
                status = "Active"
            print(f"Task Id: {x[0]}\nTask Name: {x[1]}\nTask Description: {x[2]}\nStatus: {status}\n")

    
