from objects.connection import Con

objectCon = Con()
cursor = objectCon.mycursor
mydb = objectCon.mydb

class UserStats():

    user:str = ''
    password:str = ''

    def __init__(self,user:str,password:str,method:int) -> None:
        self.user = user
        self.password = password
        self.method = method

    def userVerify(self) -> bool:
        
        l:list = []
        list:list = []
        cursor.execute("SELECT * FROM usuario")
        myresult = cursor.fetchall()
        
        if self.method == 0:
            for x in myresult:
                if x[1] == self.user and x[2] == self.password:
                    return True

        elif self.method == 1:
            for x in myresult:
                l.append(x)
            for y in l:
                list.append(y[1])

            if self.user in list:
                print('User already registered.')
                return False
            else:
                return True

        else:
            print('There was some error...')
            exit()

    def registerUser(self) -> bool:

        sql = "INSERT INTO usuario (user, senha) VALUES (%s, %s)"
        val = (self.user, self.password)
        cursor.execute(sql, val)
        mydb.commit()
        print("User successfully registered!")


            
    
            
















