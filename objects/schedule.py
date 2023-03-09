from objects.connection import Con

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