employees = ["Ahmed", "Mona", "Ali", "Omar"]
salaries = [8000, 9500, 6500, 7000]
departments = ["IT", "HR", "IT", "Finance"]
attendance = [22, 25, 18, 24]
bonuses = [1000, 1500, 0, 500]

while True :

    print(
        "----- EMPLOYEE MANAGEMENT SYSTEM -----\n\n"
        "1. Show All Employees\n"
        "2. Add New Employee\n"
        "3. Search Employee\n"
        "4. Update Employee Data\n"
        "5. Remove Employee\n"
        "6. Calculate Employee Salary\n"
        "7. Department Statistics\n"
        "8. Salary Statistics\n"
        "9. Sort Employees by Salary\n"
        "10. Search Employees by Salary Range\n"
        "11. Show Employees by Department\n"
        "12. Exit\n"
    )
# ادخال الاختيار
    try :
        choice = int(input("Enter choice number :"))
    except ValueError  :
        print("Please enter choice number !")
        continue
# عرض جميع الموظفين 
    if choice == 1 :
        if not employees :
            print("NOt found !")
            continue
        elif employees :
            for number,employ in enumerate(employees,1) :
                print(f"{number}.{employ} -Salary :{salaries[number-1]} -Department :{departments[number-1]} -Attendance :{attendance[number-1]} -Bonuse :{bonuses[number-1]}")
# اضافه موظف
    elif choice == 2 :
        employ = input("Enter employ name add :").strip()
        if not employ :
            print("Please enter name employ !")
            continue
        if employ.lower() in [name.lower() for name in employees] :
            print("Employ exist !")
            continue
        else :
            try :
                salary = int(input("Enter salary :"))
            except ValueError :
                print("Please enter number salary !")
                continue
            if 0 >= salary :
                print("The salary must be than zero !")
            else :
                department = input("Enter debartment :").strip()
                if not department :
                    print("Please enter department name !")
                    continue
                try :
                    attend = int(input("Enter attendance employ :"))
                except ValueError :
                    print ("Please enter attendance number !")
                    continue
                if 0 < attend <= 31 :
                    try :
                        bonus = int(input("Enter to bonas :"))
                    except ValueError :
                        print("Please enter donas number !")
                        continue
                    if 0 <= bonus :
                        employees.append(employ)
                        salaries.append(salary)
                        departments.append(department)
                        attendance.append(attend)
                        bonuses.append(bonus)
                        print("Enployed add successsful !")
                    else :
                        print("The bonus must be than zero !")
                else :
                    print("Attendance is required for a period ranging from one day up to 31 days.")
# البحث عن موظف
    elif choice == 3 :
        employ = input("Enter employ name !").strip()
        if not employ :
            print("Please enter employ name !")
            continue
        if employ.lower() in [name.lower() for name in employees] :
            index = [name.lower() for name in employees].index(employ.lower())
            print(f"Employ :{employ}\nSalary :{salaries[index]}\nDepartment :{departments[index]}\nAttendance :{attendance[index]}\nBonases :{bonuses[index]}")
        else :
            print("Not found !")
# تعديل بيانات الموظفين
    elif choice == 4 :
        employ = input("Enter employ name !").strip()
        if not employ :
            print("Please enter employ name :")
            continue
        if employ.lower() in [name.lower() for name in employees] :
            index = [name.lower() for name in employees].index(employ.lower())
            print(
                "\n1. Salary adjustment\n"
                "2. Edit section\n"
                "3. Adjusting attendance days\n"
                "4. Bonus adjustment\n"
            )
            try :
                choicee = int(input("Enter choice number :"))
            except ValueError :
                print("Please enter choice number !")
                continue
            if  choicee == 1 :
                try :
                    salary = int(input("Enter the new salary :"))
                except ValueError :
                    print("Please enter saleary number !")
                    continue
                if salary == salaries[index] :
                    print("The new salary is the same as the old one.")
                elif 0 >= salary :
                    print("The salary must be greater than zero.")
                else :
                    salaries[index] = salary
                    print("The salary has been updated.")
            elif choicee == 2 :
                department = input("Enter the new section").strip()
                if not department :
                    print("Please enter department name !")
                    continue
                departments[index] = department
                print("successful !")
            elif choicee == 3 :
                try :
                    attend = int(input("Enter the new number of days :"))
                except ValueError :
                    print("Please enter attendance number !")
                    continue
                if attend == attendance :
                    print("The old value is equal to the new value.")
                if 0 < attend <= 31 :
                    attendance[input] = attend
                    print("successsful !")                
            elif choicee == 4 :
                try :
                    bonus = int(input("Access the new bonus :"))
                except ValueError :
                    print("Please enter bonus number !")
                    continue
                if bonus == bonuses :
                    print("The old value is equal to the new value.")
                elif 0 >= bonus :
                    print("The salary must be greater than zero.")
                else :
                    bonuses[index] = bonus
                    print("Successful ")
            else :
                print("The correct option must be chosen.")
# حذف موظف
    elif choice == 5 :
        employ = input("Enter employ name !").strip()
        if not employ :
            print("Please enter employ name :")
            continue
        if employ.lower() in [name.lower() for name in employees] :
            index = [name.lower() for name in employees].index(employ.lower())
            confirm = input("Do you really want to delete? yes/no").strip()
            if not confirm :
                print("Please enter yes/no ")
                continue
            if confirm == "yes" :
                employees.pop(index)
                salaries.pop(index)
                departments.pop(index)
                attendance.pop(index)
                bonuses.pop(index)
                print("Deletion confirmed")
            elif confirm == "no" :
                print("The deletion has been reversed.")
            else :
                print("Please enter yes or no.")
# حساب مرتب الموظف النهائي
    elif choice == 6 :
        employ = input("Enter employ name !").strip()
        if not employ :
            print("Please enter employ name :")
            continue
        if employ.lower() in [name.lower() for name in employees] :
            index = [name.lower() for name in employees].index(employ.lower())
            presence = attendance[index]*100
            absence = (attendance[index]-30)*150
            final_salary = salaries[index] + bonuses[index]  + presence - absence
            print(f"Employ :{employ}\nSalary :{salaries[index]}\nDepartment :{departments[index]}\nAttendance :{attendance[index]}\nBonuse :{bonuses[index]}\nPresence :{presence}\nAbsence :{absence}\nFinal salary :{final_salary}")
        else :
            print("Not found !")
# احصائيات الاقسام
    elif choice == 7 :
        department = input("Enter department :").strip()
        if not department :
            print("Please enter department name !")
            continue
        if department.lower() in [name.lower for name in departments] :
            count_deparmtent = [name.lower() for name in departments].count(department.lower())
            print(
                f"Number of employees :{count_deparmtent}\n"
                f"Total Salaries :{sum(salaries[count_deparmtent])}\n"
                f"Average salaries :{round(sum(salaries[count_deparmtent])/len(salaries[count_deparmtent]))}\n"
            )
        else :
            print("Not found")
# احصائيات المرتبات
    elif choice == 8 :
        if not employees :
            print("No employees found !")
            continue
        print(
            f"Number of employees :{len(employees)}\n"
            f"Total Salaries :{sum(salaries)}\n"
            f"Average salaries :{round(sum(salaries)/len(salaries))}\n"
            f"Higt salaries :{max(salaries)}\n"
            f"Low salaries :{min(salaries)}\n"
        )
# ترتيب الموظفين
    elif choice == 9 :
        sorted_salaries = sorted(salaries)
        print("-----Ascending order-----")
        for salary in sorted_salaries :
            index = salaries.index(salary)
            print(f"Employee :{employees[index]} - Salary :{salary}")
        sorted1 = sorted(salaries, reverse=True)
        print("-----Descending order-----")
        for salary in sorted1 :
            index = salaries.index(salary)
            print(f"Employee :{employees[index]} - Salary :{salary}")
# البحث عن موظف داخل نطاق المرتب
    elif choice == 10 :
        try :
            min_salary = float(input("Enter minimum salary :"))
            max_salary = float(input("Enter maximum salary :"))
        except ValueError :
            print("Please enter valid salary number !")
            continue
        if min_salary >= max_salary :
            print("Invalid range ! minimum salary cannot exced maximum salary !")
            continue
        found = False
        for i in range(len(employees)) :
            if min_salary <= salaries[i] <= max_salary :
                print(f"Employee :{employees[i]} -salary :{salaries[i]}")
                found = True
        if not found :
            print("No employees found in thin salary range !")
# عرض الموظفين حسب القسم
    elif choice == 11 :
        department = input("Enter department :").strip()
        if not department :
            print("Please enter department name !")
            continue
        found =False
        for i in range(len(employees)) :
            print(f"Employees :{employees[i]} -Salary :{salaries[i]} -Attendance :{attendance[i]} -Bonuses :{bonuses[i]}")
            found = True
        if not found :
            print("No employees found !")
# خروج
    elif choice == 12 :
        print("Good bay ")
        break
# ادخال اختيار خطا
    else :
        print("The choice is incorrect.")

# الكود في اخطاء علشان لما ارجع اشوفه تاني اعرف مستواي كان عامل ايه وقت ما انا عملته 
# 21/10/2026