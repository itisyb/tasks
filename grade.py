length = int(input("Enter number of student:"))  #size of students
student ={} #empty dict
for i in range(length):
    s = input("Enter student name :")
    eng = int(input("Enter marks in english :"))
    math = int(input("Enter marks in maths :"))
    his = int(input("Enter marks in history :"))
    sci = int(input("Enter marks in science :"))
    percent = (eng+math+his+sci)/4 #percentage
    student[s] = {"english":eng,"maths":math,"history":his,"science":sci,"percent":percent}
    print()
    print()
    print(s)
    print(student[s]["percent"])

print()
print()
print(student)
print()
print()

#for finding top scorer in each subject
print("\t\t Top Scorers ")

subject =  ["english","maths","history","science"]
for sub in subject:
    highest = 0
    for key,value in student.items():
        if  value[sub]>highest:
            highest =  value[sub]
            highestvalue = key
    print(highestvalue)
    print(sub)
    print()    
