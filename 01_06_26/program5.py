class StudentProfDetails:
    def __init__(self,User_Clg,courseName=""):
        if isinstance(User_Clg,StudentProfDetails):
            self.collegeName = User_Clg.collegeName
            self.courseName = User_Clg.courseName
        else:
            self.collegeName = User_Clg
            self.courseName = courseName
    def output(self):
        print("Name of college : ",self.collegeName)
        print("Name of college : ",self.courseName)
        
Akash = StudentProfDetails("ips","CSE")
Madhur = StudentProfDetails("RGPV","IT")
Adtiya = StudentProfDetails(Akash)
Rehan = StudentProfDetails(Madhur)
Akash.output()
Adtiya.output()
Madhur.output()
Rehan.output()