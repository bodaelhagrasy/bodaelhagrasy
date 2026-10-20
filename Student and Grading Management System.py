students = ["Ahmed", "Mona", "Ali", "Omar"]
grades = [85, 92, 67, 48]
subjects = ["Python", "Python", "Data Science", "Python"]

while True :

    print(
        "\n-----STUDENT MANAGEMENT SYSTEM-----\n\n"
        "1. Show All Students\n"
        "2. Add New Student\n"
        "3. Search Student\n"
        "4. Update Student Grade\n"
        "5. Remove Student\n"
        "6. Student Statistics\n"
        "7. Sort Grades\n"
        "8. Count Students by Subject\n"
        "9. Show Successful Students\n"
        "10. Exit\n"
    )
# اختيار رقم
    try :
        choice = int(input('Enter number choice :'))
    except ValueError :
        print("Please enter number choice !")
        continue
# عرض جميع الطلاب
    if choice == 1 :
        if not students :
            print("No student now !")
            continue
        if students :
            for number,student in enumerate(students,1) :
                print(f"{number}.{student} -Grade :{grades[number-1]} -Subject :{subjects[number-1]}")
# اضافه طالب جديد
    elif choice == 2 :
        student = input("Enter student name :").strip()
        if not student :
            print("Please enter student name !")
            continue
        if student.lower() in [name.lower() for name in students] :
            print("Student exist !")
        else :
            try :
                grade = int(input("Enter grade number :"))
            except ValueError :
                print("Please enter grade number !")
                continue
            if 0 > grade :
                print("The grade must be greater than zero !")
                continue
            elif grade > 100 :
                print("The grade must be less than or equal to 100 ! ")
                continue
            elif 0 <= grade <= 100 :
                subject = input("Enter subject name :").strip()
                if not subject :
                    print("Please enter subject name !")
                    continue
                students.append(student)
                grades.append(grade)
                subjects.append(subject)
                print("Added successful !")
# البحث عن طالب
    elif choice == 3 :
        student = input("Enter student name search :").strip()
        if not student :
            print("Please enter student name !")
            continue
        if student.lower() in [name.lower() for name in students] :
            index = [name.lower() for name in students].index(student.lower())
            print(f"Student :{student}\nGrade :{grades[index]}\nSubject :{subjects[index]}")
        else :
            print("Student not found !")
# تعديل درجات الطلاب
    elif choice == 4 :
        student = input("Enter student name :").strip()
        if not student :
            print("Please enter student name !")
            continue
        if student.lower() in [name.lower() for name in students] :
            index = [name.lower() for name in students].index(student.lower())            
            try :
                grade = int(input("Enter number update grade :"))
            except ValueError :
                print("Please ente number grade !")
                continue
            if grade == grades[ index] :
                print("The grade is equal to the current grade.")
            elif grade < 0 :
                print("The grade must be greater than zero !")
            elif grade > 100 :
                print("The grade must be loss than or equol 100 !")
            elif 0 <= grade <=100 :
                grades[index] = grade 
                print("The grade update successful !")
        else :
            print("Not found !")
# حذف الطلاب
    elif choice == 5 :
        student = input("Enter student name removed :").strip()
        if not student :
            print("Please enter student name !")
            continue
        if student.lower() in [name.lower() for name in students] : 
            index = [name.lower() for name in students].index(student.lower())
            print("The student is present.")
            delet = input("Do you really want to delete? yes/no").strip()
            if delet.lower() == "yes" :
                students.pop(index)
                grades.pop(index)
                subjects.pop(index)
                print("The student has been deleted.")
            elif delet.lower() == "no" :
                print("Deletion did not take place.")
            else :
                print("You must respond with yes or no.")
        else :
            print("Not found !")
# عرض عدد الطلاب والدرجات 
    elif choice == 6 :
        if not students :
            print("There are no students.")
            continue
        passed = 0
        need_improvement = 0
        for grade in grades:
            if grade >= 50:
                passed += 1
            else:
                need_improvement += 1
        print(
            f"Number of students :{len(students)}\n"
            f"Average score :{round(sum(grades)/len(grades))}\n"
            f"High Grade :{max(grades)}\n"
            f"Lowest grade :{min(grades)}\n"
            f"Number of successful candidates :{passed}\n"
            f"A number of students need improvement :{need_improvement}\n"
        )
# عرض ترتيب الدرجات
    elif choice == 7 :
        print(
            f"Grades ascending :{sorted(grades)}\n"
            f"Descending order of grades :{sorted(grades, reverse=True)}"
        )
# حساب عدد الطلاب المسجلين في الماده 
    elif choice == 8 :
        subject = input("Enter subject name :").strip()
        if not subject :
            print("Please enter student name !")
            continue
        if subject.lower() in [name.lower() for name in subjects] :
            categor = [name.lower() for name in subjects].count(subject.lower())
            print(f"Subject :{subject} Categor :{categor}")
        else :
            print("Not found !")
# حساب عدد الناجحين
    elif choice == 9 :
        passed = 0
        for i in range(len(students)):
            if grades[i] >= 50:
                print(f"Student: {students[i]} | Grade: {grades[i]}")
                passed += 1
        if passed == 0:
            print("There are no successful students.")
# خروج
    elif choice == 10 :
        print("Good bay")
        break
# اختار رقم غلط
    else :
        print("Please enter number choice !")
# الحمد الله خلتص مع اني مصدع اوووي