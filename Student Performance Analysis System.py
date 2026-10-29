# بسم الله الرحمن الرحيم
students = ["Ahmed", "Mona", "Ali", "Omar", "Sara"]
study_hours = [2, 5, 1, 4, 6]
attendance = [70, 95, 60, 85, 98]
grades = [65, 88, 50, 78, 92]

while True :
    print(
        "===== Student Performance Analysis =====\n\n"
        "1. Show All Students\n"
        "2. Add New Student\n"
        "3. Search for Student\n"
        "4. Update Student Data\n"
        "5. Remove Student\n"
        "6. Calculate Statistics\n"
        "7. Analyze Student Performance\n"
        "8. Sort Students by Grades\n"
        "9. Filter Students\n"
        "10. Exit\n"
    )

    try :
        choice = int(input("Enter choice number :"))
    except ValueError :
        print("Please enter choice number !")
        continue
# عرض الكل
    if choice == 1 :
        if not students :
            print("No students found !")
            continue
        else :
            for number,student in enumerate(students,1) :
                print(f"{number}.{student} -Study hours :{study_hours[number-1]} -Attendance :{attendance[number-1]} -Grades :{grades[number-1]}")
# اضافه طالب جديد
    elif choice == 2 :
        student = input("Enter student name add :").strip().lower()
        if not student :
            print("Please enter student name !")
            continue
        if student in [name.lower() for name in students] :
            print("The student already exsist !")
            continue
        else :
            try :
                study_hour = int(input("Enter study hour :"))
            except ValueError :
                print("Please enter study hour !")
                continue
            if study_hour < 0 :
                print("The study hour must be than 0 !")
                continue
            try :
                attend = int(input("Enter study attendance :"))
            except ValueError :
                print("Please enter study attendance !")
                continue
            if 0 <= attend <= 100 :
                try :
                    grade = int(input("Enter student grade :"))
                except ValueError :
                    print("Please enter student grade !")
                    continue
                if 0 <= grade <= 100 :
                    students.append(student)
                    study_hours.append(study_hour)
                    attendance.append(attend)
                    grades.append(grade)
                    print("Student added successful ")
                else :
                    print("The grade must be than 0 at 100 !")
                    continue
            else :
                print("The attendance must be than 0 at 100 !")
                continue
# البحث عن طالب
    elif choice == 3 :
        student = input("Enter student name Search :").strip().lower()
        if not student :
            print("Please enter student name !")
            continue
        else :
            if student in [name.lower() for name in students] :
                index = [name.lower() for name in students].index(student)
                print(f"Student :{student}\nStudy hours :{study_hours[index]}\nAttendance :{attendance[index]}\nGrades :{grades[index]}")
            else :
                print("No student found !")
# تحديث بيانات الطلاب
    elif choice == 4 :
        student = input("Enter student name updata :").strip().lower()
        if not student :
            print("Please enter student name !")
            continue
        else :
            if student in [name.lower() for name in students] :
                index = [name.lower() for name in students].index(student)
                try :
                    study_hour = int(input("Enter study hour updata:"))
                except ValueError :
                    print("Please enter study hour !")
                    continue
                if study_hours[index] == study_hour :
                    print("The old value cannot be equal to the new one.")
                    continue
                if study_hour < 0 :
                    print("The study hour must be than 0 !")
                    continue
                else :
                    try :
                        attend = int(input("Enter study attendance updata :"))
                    except ValueError :
                        print("Please enter study attendance !")
                        continue
                    if attendance[index] == attend :
                        print("The old value cannot be equal to the new one.")
                        continue
                    if 0 > attend > 100 :
                        print("The attendance must be than 0 at 100 !")
                        continue
                    if 0 <= attend <= 100 :
                        try :
                            grade = int(input("Enter student grade updata :"))
                        except ValueError :
                            print("Please enter student grade !")
                            continue
                    if grades[index] == grade :
                            print("The old value cannot be equal to the new one.")
                    if 0 > grade > 100 :
                            print("The grade must be than 0 at 100 !")
                            continue
                    if 0 <= grade <= 100 :
                                study_hours[index] = study_hour
                                attendance[index] = attend
                                grades[index] = grade
                                print("The student updata successful ")
            else :
                print("No student found")
# حذف طالب
    elif choice == 5 :
        student = input("Enter student name remove :").strip().lower()
        if not student :
            print("Please enter student name remove !")
            continue
        if student in [name.lower() for name in students] :
            index = [name.lower() for name in students].index(student)
            cont = input("Do you really want to delete? yes/no").strip().lower()
            if not cont :
                print("Please enter yes/no ")
                continue
            if cont == "yes" :
                students.pop(index)
                study_hours.pop(index)
                attendance.pop(index)
                grades.pop(index)
                print("Student removed successful ")
            elif cont == "no" :
                print("The deletion has been reversed.")
            else :
                print("Please ente yes/no")
        else :
            print("No student found !")
# عرض الدرجات من العدد والمتوسط وغيره
    elif choice == 6 :
        if not students :
            print("No students found !")
            continue
        index_max_grade = grades.index(max(grades))
        index_min_grade = grades.index(min(grades))
        grade_up = 0
        for  grade in grades :
            if grade >= 85 :
                grade_up += 1
        print(
            f"Number student :{len(students)}\n"
            f"Averge srudy hours :{sum(study_hours)/len(study_hours)}\n"
            f"Averge attendance :{sum(attendance)/len(attendance)}\n"
            f"Avegre grades :{sum(grades)/len(grades)}\n"
            f"Student :{students[index_max_grade]} -High grades :{max(grades)}\n"
            f"Student :{students[index_min_grade]} -Loow grades :{min(grades)}\n"
            f"Grades up 85 :{grade_up}"
        )
# تصنيف الدرجات حسب الدرجه
    elif choice == 7 :
        if not students :
            print("No students found")
            continue
        for i,grade in enumerate(grades) :
            attend = attendance[i]
            study_hour = study_hours[i]
            if grade >= 85 and attend >= 80 and study_hour >=3 :
                performance = "High performance "
            elif grade >= 65 and attend >= 60 :
                performance = "Medium  Performent "
            else :
                performance = "Needs improvement "
            print(f"Student {students[i]} -Performance :{performance}")
# ترتيب تصاعدي
    elif choice == 8 :
        if not students :
            print("No students found")
            continue
        sorted_grades = sorted(grades,reverse=True)
        for grade in sorted_grades :
            index = grades.index(grade)
            print(f"Student :{students[index]} -Grade :{grade}")
# قوائم
    elif choice == 9 :
        import pandas as pd 
        data = {
            "Student" : students ,
            "Study hours" : study_hours ,
            "Attendance" : attendance ,
            "Grades" : grades ,
        }
        df = pd.DataFrame(data)
        print(df)
        print("\n\n-----High attendance-----\n")
        high_attand = df[df["Attendance"] >= 80]
        print(high_attand)
        print("\n-----High grades-----\n")
        high_hours =df[df["Study hours"] >= 4]
        print(high_hours)
        print("\n-----Average-----\n")
        average = df["Grades"].mean()
        print(average)
# خروج
    elif choice == 10 :
        print("Goodbay")
        break
# تم بحمد الله
# 29/10/2026