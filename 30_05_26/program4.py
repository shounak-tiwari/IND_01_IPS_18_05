from mysql.connector import connect

class student:
    def InputDetails(insName):
        insName.StudName =  input("Enter the Name : ")
        insName.StudAge = input("Enter the Age :  ")
        insName.StudContact = input("Enter the Contact :  ")

    def OutputDetails(insName):
        print("The name of student : ",insName.StudName)
        print("The age of student : ",insName.StudAge)
        print("The contact of student  : ",insName.StudContact)

    def saveToDb(insName):
        try:
            connection = connect(
                host = "localhost",
                port = 3306,
                database = "ipsStudData",
                user ="root",
                password ="root"
            )

            if connection.is_connected():
                print("Run Success Fully")
            else:
                print("Database not connect ")
        except: 
            print("Some exp")

obj = student()
obj.InputDetails()
obj.OutputDetails()
obj.saveToDb()  


'''

'''