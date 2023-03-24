def addStudent():
    global listStudents
 
    infor = {
        'id' : '',
        'name' : '',
        'score' : ''
    }
    id = input("Input Student ID:")
 
    while True:
        student = findStudent(id)
        if student != False:
            print("This ID was exist!")
            id = input("Input Student ID: ")
        else:
            break
 
    infor['id'] = id
    infor['name'] = input("Input Name Student: ")
    infor ['score'] = int(input("Input Ave Score: "))
    listStudents.append(infor)
    
 
def findStudent(id):
    global listStudents
    for i in range(0, len(listStudents)):
        if listStudents[i]['id'] == id:
            return [i, listStudents[i]]
    return False

def deleteStudent():
    id = input("Input ID need to delete: ")
 
    global listStudents
    student = findStudent(id)
 
    if student != False:
        listStudents.remove(student[1])
        print("ID delete successfull")
    else :
        print("ID don't exist!")
 
def showStudents():
    print("*** List of students ***")
    global listStudents
    for i in range(0, len(listStudents)):
        print("[",listStudents[i]['id'],"]", "[",listStudents[i]['name'], ",score average:" ,listStudents[i]['score'],"]")
 
def editStudent():
    print("*** Update student infomation ***")
    global listStudents
    id = input("Input ID need to fix: ")
    student = findStudent(id)
    if student == False:
        print("Don't find!", id)
    else :
        name = input("Input student name: ")
        student[1]['name'] = name
        listStudents[student[0]] = student[1]

def sortByDiemTB(self):
        listStudents=[]
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

action = 0
listStudents = []
while action >= 0:
    if action == 1:
        addStudent()
    elif action == 2:
        deleteStudent()
    elif action == 3:
        editStudent()
    elif action == 4:
        showStudents()
    elif action == 5:
        print(sortByDiemTB)

    print("===================================================")
    print("-------------------Choose functions----------------")
    print("===================================================")
    print("=====-----Click 1: Add student--------------=======")
    print("=====-----Click 2: delete student-----------=======")
    print("=====-----Click 3: Update student-----------=======")
    print("=====-----Click 4: Show list of student-----=======")
    print("=====-----Click 5: Sort students by GPA-----=======")
    print("=====-------------Click 0: Exit!------------=======")
    print("===================================================")
    action = int(input("Choose number of functions: "))
    if action == 0:
        break