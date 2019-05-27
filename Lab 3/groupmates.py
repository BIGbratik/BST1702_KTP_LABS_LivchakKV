#coding:utf-8
groupmates=[
    {
        "name":u"Иван",
        "group":"17-01",
        "age":20,
        "marks":[4,4,5,3,4]
    },
    {
        "name":u"Екатерина",
        "group":"17-01",
        "age":19,
        "marks":[5,4,5,5,4]
    },
    {
        "name":u"Пётр",
        "group":"17-03",
        "age":21,
        "marks":[3,4,5,3,5]
    },
    {
        "name":u"Сергей",
        "group":"17-02",
        "age":20,
        "marks":[2,5,5,3,2]
    },
    {
        "name":u"Александр",
        "group":"17-02",
        "age":21,
        "marks":[5,3,5,3,4]
    },
]

def print_students(students):
    print u"Имя студента".ljust(15),\
          u"Группа".ljust(8),\
          u"Возраст".ljust(8),\
          u"Оценка".ljust(20)
    for student in students:
        print \
              student["name"].ljust(15),\
              student["group"].ljust(8),\
              str(student["age"]).ljust(8),\
              str(student["marks"]).ljust(20)
        print "\n"

print_students(groupmates)

def filter_students(students):
    print u"Введите среднюю оценку:"
    a_sr=int(raw_input())
    TrueStudents=[]
    print u"Список студентов, удовлетворяющих условию средней оценки"
    for student in students:
        l=len(student["marks"])
        k=sum(student["marks"])
        if (k/l)>=a_sr:
            TrueStudents.append(student)
    print_students(TrueStudents)
            
filter_students(groupmates)
            
    
