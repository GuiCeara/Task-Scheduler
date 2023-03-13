import mysql.connector

class Con():
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="agendamento_tarefa"
    )

    mycursor = mydb.cursor()
    cursorFilter = connection.cursor(prepared=True)