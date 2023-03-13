from objects.connection import Con

objectCon = Con()
cursor = objectCon.mycursor
mydb = objectCon.mydb
cursorFilter = objectCon.cursorFilter

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

        tuple1 = user

        query = "SELECT * FROM tarefa WHERE fk_usuario_user = 'teste' " 
        cursor.execute(query)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)

    
