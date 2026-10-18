employees = ["Ahmed", "Mona", "Ali"]
salaries = [8000, 9500, 7000]
departments = ["IT", "HR", "Sales"]

while True :
    print("===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Show All Employees")
    print("2. Add New Employee")
    print("3. Search Employee")
    print("4 .Update Employee Salary")
    print("5. Remove Employee")
    print("6. Employee Statistics")
    print("7. Sort Salaries")
    print("8. Count Employees by Department")
    print("9. Exit")

    try :
        choice = int(input("Enter your choice:"))
    except ValueError :
        print("Please enter number choice !")
        continue
# عرض الموظفين
    if choice == 1 :
        if employees :
            for number,p in enumerate(employees,1) :
                print(f"{number}.{p} -Salary :{salaries[number-1]} -Department :{departments[number-1]}")
        else :
            print("Not employees found !")
# اضافه موظفين جدد
    elif choice == 2 :
            employe = input("Enter employee name :").strip()
            if not employe :
                print("Please enter a name !")
                continue
            if employe.lower() in [name.lower() for name in employees] :
                print("Employe alreade exists !")
                continue
            try :
                salary = int(input("ُEnter empioye salary :"))
            except ValueError :
                print("Please enter number salary !")
                continue 
            if salary <= 0 :
                print("Salary must be greater than zero !")
                continue
            depar = input("Enter deparment :").strip()
            if not depar :
                print("Please enter a deparment !")
                continue
            employees  .append(employe)
            salaries   .append(salary)
            departments.append(depar)
            print(
                f"Empioye :{employe} - Salary :{salary} - Department :{depar}\n"
                "Employe added !"
                )
# البحث عن موظف
    elif choice == 3 :
        employe = input("Enter enploye name :").strip()
        if not employe :
            print("Please enter a name !")
            continue
        if employe.lower() in [name.lower() for name in employees] :
            index = [name.lower() for name in employees].index(employe.lower())
            print(
                f"Employe :{employe} -Salary :{salaries[index]} -departmant :{departments[index]}"
                )
        else :
            print("Not found !")    
            continue
# تغيير مرتبات الموظفين
    elif choice == 4 :
        employe = input("Enter employe name :").strip()
        if not employe :
            print("Please enter employe !")
            continue
        if employe.lower() in [name.lower() for name in employees] :
            try :
                salary = int(input("Enter new salary :"))
            except ValueError :
                print("Please enter number salary !")
                continue
            if salary <= 0 :
                print("Salary must be greater than zero !")
                continue
            index = [name.lower() for name in employees ].index(employe.lower())
            salaries[index] = salary
            print(
                    f"Emplooy :{employe}\nSalary :{salaries[index]}\n"
                    "Successful "
                )
        else :
            print("Not found !")
# حذف موظفين 
    elif choice == 5 :
        employe = input("Enter employee name :").strip()
        if not employe :
            print("Please enter name :")
            continue
        if employe.lower() in [name.lower() for name in employees] :
            index = [name.lower() for name in employees].index(employe.lower())
            remove = input("Are you sure you want to delete the employee? yes/no :")
            if not remove :
                print("Please enter yes or no !")
                continue
            if remove == "yes" :
                employees.pop(index)
                salaries.pop(index)
                departments.pop(index)
                # هنا انا استخدمت pop بدل remove علشان انا جايب رقم الموظف بدل الاسم
                print("employe removed !")
            elif remove == "no" :
                print("Deletion did not take place.")
            else :
                print("The choice is wrong.")
        else :
            print("Not founde !")
# عرض الموظفين والرواتب
    elif choice == 6 :
        if not employees :
            print("Not founde !")
            continue 
        print(f"employees :{len(employees)}\nApproximating average salaries :{sum(salaries) / len(salaries)}\nAverage salaries :{round(sum(salaries) / len(salaries))}\nHigt salaries :{max(salaries)}\nLow salaies :{min(salaries)}")
# ترتيب المرتبات من الاصغر الي الاكبر
    elif choice == 7 :
        # دي علي طول اسهل
        print(f"Sorted salaries :{sorted(salaries)}")
        # دي لو عايز اعمل variabel
        # sorted_salaries = sorted(salaries)
        # print(f"Sorted salaries :{sorted_salaries}")
        # دي لو انا عايز من الاكبر للاصغر
        # من غير متغير علي طول 
        # print(f"Sorted salaries :{sorted(salaries, reverse=True)}")
# 
    elif choice == 8 :
        print(f"departments :{departments}")
        depar = input("Enter department name :").strip()
        if not depar :
            print("Please enter department name !")
            continue
        if depar.lower() in [name.lower() for name in departments] :
            # هنا ممكن نعملها بمتغير او بامر الطباعه علي طول 
            # بالطباعه ونريح نفسنا 
            print(f"{depar} appears {[name.lower() for name in departments].count(depar.lower())} times")
            # لو عايزين نعله في متغير 
            # count_depart = departments.count(depar)
            # print(f"{depar} appears {count_depart}")
        else :
            print("Not found !")

    elif choice == 9 :
        print("good bay")
        break