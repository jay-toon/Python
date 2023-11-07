class students:
    dict = {
        "name": "",
        "age": 0,
        "course": "",
        "grade": ""
    }
    
    def setInfo(self):
        self.dict["name"] = input("Enter name: ")
        self.dict["age"]= input("Enter age: ")
        self.dict["course"] = input("Enter course: ")
        self.dict["grade"] = input("Enter grade: ")
        
    def getInfo(self):
        print(f"Name: {self.dict["name"]}, Age: {self.dict["age"]}, Course: {self.dict["course"]}, Grade: {self.dict["grade"]}")
    
student = students()
student.setInfo()
student.getInfo()
