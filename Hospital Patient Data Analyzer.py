
patients = ["Ahmed", "Mona", "Ali", "Omar", "Sara", "Youssef", "Nour"]
ages = [25, 34, 45, 19, 52, 40, 29]
genders = ["Male", "Female", "Male", "Male", "Female", "Male", "Female"]
departments = ["Cardiology","Neurology","Orthopedics","Cardiology","Neurology","Orthopedics","Cardiology"]
visit_counts = [3, 5, 2, 4, 6, 1, 3]
medical_costs = [1500, 2500, 1200, 1800, 3000, 900, 1600]

while True :
    print(
        "\n===== Hospital Patient Data Analyzer =====\n\n"
    "1. Show All Patients\n"
    "2. Add New Patient\n"
    "3. Search Patient\n"
    "4. Update Patient Data\n"
    "5. Remove Patient\n"
    "6. Calculate Patients Statistics\n"
    "7. Analyze Medical Costs\n"
    "8. Sort Patients\n"
    "9. Filter Patients\n"
    "10. Analyze Data Using Pandas\n"
    "11. Exit\n"
    )

    try :
        choice = int(input("Enter choice :"))
    except ValueError :
        print("Please enter choice")
        continue
# Show All Patients
    if choice == 1 :
        if not patients :
            print("No patients found !")
            continue
        for number,patient in enumerate(patients,1) :
            print(f"{number}.{patient} -Age :{ages[number-1]} -Gender :{genders[number-1]} -Departments :{departments[number-1]} -Visit counts :{visit_counts[number-1]} -Medical costs :{medical_costs[number-1]}")
# Add New Patient
    elif choice == 2 :
        patient = input("\nEnter patient name :").strip()
        if not patient :
            print("\nPlease enter patient name !")
            continue
        if patient.lower() in [name.lower() for name in patients] :
            print("\nThe patient exsist !")
        else :
            try :
                age = int(input("\nEnter your age :"))
            except ValueError :
                print("\nPlease enter age !")
                continue
            if 0 < age :
                gender = input("\nEnter gender (male/female) :").strip()
                if not gender :
                    print("\nPlease ente gender !")
                    continue
                if gender.lower() == "male" or gender.lower() == "female" :
                    department = input("\nEnter department :").strip()
                    if not department :
                        print("\nPlease enter department !")
                        continue
                    try :
                        visit_count = int(input("\nEnter number visit counts :"))
                    except ValueError :
                        print("\nPlease enter visit counts !")
                        continue
                    if 0 < visit_count :
                        try :
                            medical_cost = int(input("\nEnter medical costs :"))
                        except ValueError :
                            print("\nPlease enter medical costs !")
                            continue
                        if 0 < medical_cost :
                            patients.append(patient)
                            ages.append(age)
                            genders.append(gender)
                            departments.append(department)
                            visit_counts.append(visit_count)
                            medical_costs.append(medical_cost)
                            print("\nPatinent edded successful \n")
                        else :
                            print("\nThe medical cost must be equal zero !")
                    else :
                        print("\nThe visit count must be equal zero !")
                else :
                    print("\nPlease enter the male/female !")
            else :
                print("\nThe age must be equal zero !")
# Search Patient
    elif choice == 3 :
        patient = input("\nEnter patient shear :").strip()
        if not patient :
            print("\nPlease enter patient !")
            continue
        if patient.lower() in [name.lower() for name in patients] :
            index = [name.lower() for name in patients].index(patient.lower())
            print(
                f"\n-Patient :{patient}\n"
                f"-Age :{ages[index]}\n"
                f"-Gender :{genders[index]}\n"
                f"-Department :{departments[index]}\n"
                f"-Visit counts :{visit_counts[index]}\n"
                f"-Medical costs :{medical_costs[index]}"
            )
        else :
            print("\nNo patient found !")
# Update Patient Data
    elif choice == 4 :
        patient = input("\nEnter patinent name updata :").strip()
        if not patient :
            print("\nPlease enter patinent name !")
            continue
        if patient.lower() in [name.lower() for name in patients] :
            index = [name.lower() for name in patients].index(patient.lower())
            while True :
                print(
                    "\n1. Update Age\n"
                    "2. Update Gender\n"
                    "3. Update Department\n"
                    "4. Update Visit Count\n"
                    "5. Update Medical Cost\n"
                )
                try :
                    choice = int(input("\nEmter choice number :"))
                except ValueError :
                    print("\nPlease enter choice number !")
                    continue
                if choice == 1 :
                    try :
                        age = int(input("\nEnter updata age :"))
                    except ValueError :
                        print("\nPlease enter age !")
                        continue
                    if age == ages[index] :
                        print("\nThe old age equl new age !")
                    elif 0 >= age :
                        print("\nThe age must be than equl zero !")
                    else :
                        ages[index] = age
                        print("\nUpdata successful")
                        break
                elif choice == 2 :
                    gender = input("Enter updata gender :").strip()
                    if not gender :
                        print("Please enter gender !")
                        continue
                    lower_gender = [name.lower() for name in genders]
                    if lower_gender[index] == gender.lower() :
                        print("The gender old equl gender new ")
                    elif gender.lower() == "female" or gender.lower() == "male" :
                        genders[index] = gender
                        print("\nupdata successful")
                        break
                    else :
                        print("\nPlease enter gender male/female")
                elif choice == 3 :
                    department = input("\nEnter department updata :").strip()
                    if not department :
                        print("\nPlease enter departmant !")
                        continue
                    lower_department = [name.lower() for name in departments]
                    if lower_department[index] == department.lower() :
                        print("\nThe old department equl new department ")
                    else :
                        departments[index] = department
                        print("\nUpdata successful")
                        break
                elif choice == 4 :
                    try :
                        visit_count = int(input("\nEnter updata visit count :"))
                    except ValueError :
                        print("\nPlease enter number visit count !")
                        continue
                    if visit_count == visit_counts[index] :
                        print("\nThe old visit conunt equl new visit count !")
                    elif 0 <= visit_count :
                        visit_counts[index] = visit_count
                        print("\nUpdata successful ")
                        break
                    else :
                        print("\nThe visit count must be than equl zero !")
                elif choice == 5 :
                    try :
                        medical_cost = int(input(""))
                    except ValueError :
                        print("\nPlease enter medical cost !")
                        continue
                    if medical_costs[index] == medical_cost or 0 > medical_cost :
                        print("\nThe old value cannot be equal to the new value, nor can it be equal to zero.")
                    else :
                        medical_costs[index] = medical_cost
                        print("\nUpdata successful")
                        break
                else :
                    print("Please enter choice number !")
        else :
            print("No patient found")
# Remove Patient
    elif choice == 5 :
        patient = input("\nEnter patinent name updata :").strip()
        if not patient :
            print("\nPlease enter patinent name !")
            continue
        if patient.lower() in [name.lower() for name in patients] :
            index = [name.lower() for name in patients].index(patient.lower())
            sure = input("\nAre you sure you want to delete? yes/no :").strip()
            if not sure :
                print("\nPlease enter yes/no !")
                continue
            if sure.lower() == "yes" :
                patients.pop(index)
                ages.pop(index)
                genders.pop(index)
                visit_counts.pop(index)
                departments.pop(index)
                medical_costs.pop(index)
                print("\nDelete successful ")
            elif sure.lower() == "no" :
                print("\nThe deletion has been reversed.")
            else :
                print("\nPlease enter yes/no !")
        else :
            print("\nNo patient found !")
# Calculate Patients Statistics
    elif choice == 6 :
        print(
            f"\nTotal number of patients :{len(patients)}\n"
            f"Average age of patients :{sum(ages)/len(ages)}\n"
            f"Maximum age :{max(ages)}\n"
            f"Minimum age :{min(ages)}\n"
            f"Total number of visits :{sum(visit_counts)}\n"
            f"Average number of visits :{sum(visit_counts)/len(visit_counts)}\n"
            f"Patient with the highest number of visits :{max(visit_counts)}"
        )
# Analyze Medical Costs
    elif choice == 7 :
        index_high_cost = medical_costs.index(max(medical_costs))
        print(
            f"Total medical costs :{sum(medical_costs)}\n"
            f"Average cost per patient :{sum(medical_costs)/len(medical_costs)}\n"
            f"Highest cost :{max(medical_costs)}\n"
            f"Lowest cost :{min(medical_costs)}\n"
            f"Patient with the highest cost : {patients[index_high_cost]}\n"
        )
        set_department = set(departments)
        for department in set_department :
            total_cost = sum(
                medical_costs[i] for i in range(len(departments))
                if departments[i] == department
            )
            print(f"Total cost per medical department :{department}-{total_cost}")
# Sort Patients
    elif choice == 8 :
        sorted_age = sorted(zip(ages,patients))[::-1]
        print("\n-----Age, from oldest to youngest.-----\n")
        for age,patient in sorted_age :
            print(f"Patient :{patient} -Age :{age}")
        sorted_visit = sorted(zip(visit_counts,patients))[::-1]
        print("\number of visits, from highest to lowest.\n")
        for visit,patient in sorted_visit :
            print(f"patient :{patient} -visit count :{visit}")
        sorted_medical = sorted(zip(medical_costs,patients))[::-1]
        print("\nMedical cost, from highest to lowest.\n")
        for medical,patient in sorted_medical :
            print(f"Pantient :{patient} -Medical count :{medical}")
# Filter Patients
    elif choice == 9 :
        while True :
            print(
                "\n1. Patients above a certain age.\n"
                "2. Patients with a number of visits exceeding a certain value.\n"
                "3. Patients whose costs exceed a certain value.\n"
                "4. Patients in a specific medical department.\n"
                "5. Patients categorized by gender.\n"
                            )
            try :
                choice = int(input("Enter choice number :"))
            except ValueError :
                print("Please enter choice number !")
                continue
            if choice == 1 :
                try :
                    age = int(input("enter age shear :\n"))
                except ValueError :
                    print("Please enter age !")
                    continue
                if 0 >= age :
                    print("The age must be equl zero !")
                else :
                    found = False
                    for i in range(len(ages)) :
                        if age <= ages[i] :
                            print(f"patient :{patients[i]} -age :{ages[i]}")
                            found = True
                    if found == False :
                        print("No found patient at age")
                        continue
                    else :
                        break
            elif choice == 2 :
                try :
                    visit = int(input("Enter visit counts :"))
                except ValueError :
                    print("Please enter visit counts !")
                    continue
                if 0 > visit :
                    print("The visit counts must be equl zero !")
                else :
                    found = False
                    for i in range(len(visit_counts)) :
                        if visit_counts[i] >= visit :
                            print(f"patient :{patients[i]} -visit counts :{visit_counts[i]}")
                            found = True
                    if found == False :
                        print("No found patinent at visit counts !")
                        continue
                    else :
                        break
            elif choice == 3 :
                try :
                    medical_cost = int(input("Enter medical cost shear :"))
                except ValueError :
                    print("Please enter midical cost !")
                    continue
                if 0 > medical_cost :
                    print("The medical cost must be than equal zero !")
                else :
                    found = False
                    for i in range(len(medical_costs)) :
                        if medical_costs[i] == medical_cost :
                            print(f"patient :{patients[i]} -medical cost :{medical_costs[i]}")
                            found = True
                    if found == False :
                        print("No patient found !")
                        continue
                    else :
                        break
            elif choice == 4 :
                department = input("Enter department :").strip()
                if not department :
                    print("Please enter department !")
                    continue
                if department.lower() in [name.lower() for name in departments] :
                    found = False
                    lower_department = [name.lower() for name in departments]
                    for i in range(len(lower_department)) :
                        if lower_department[i] == department.lower() :
                            print(f"patient :{patients[i]} -department :{departments[i]}")
                            found = True
                    if found == False :
                        print("No found patient !")
                        continue
                    else :
                        break
                else :
                    print("Please enter department !")
            elif choice == 5 :
                gender = input("Enter gender :").strip()
                if not gender :
                    print("Please enter gender !")
                    continue
                if gender.lower() == "male" or gender.lower() == "female" :
                    found = False
                    for i in range(len(genders)) :
                        if genders[i] == gender :
                            print(f"patient :{patients[i]} -gender :{genders[i]}")
                            found = True
                    if found == False :
                        print("No found pantient !")
                    else :
                        break
                else :
                    print("Please enter gender !")
            else :
                print("Please enter choice number !")
# Analyze Data Using Pandas
    elif choice == 10 :
        import pandas as dp 
        data = {
            "Patients" : patients ,
            "Ages" : ages ,
            "Genders" : genders ,
            "Departments" : departments ,
            "Visit counts" : visit_counts ,
            "Medical costs" : medical_costs ,
        }
        df = dp.DataFrame(data)
        print(df)
        print("\n----- Avrege age -----\n")
        print(df["Ages"].mean())
        print("\n----- Total Visit counts -----\n")
        print(df["Visit counts"].mean())
        print("\n----- Patients Aged 40 or Adove -----\n")
        print(df[df["Ages"] >= 40])
        print("\n----- Patients With Medical costs Adove 2000 -----\n")
        print(df[df["Medical costs"] > 2000])
        df["Total medical cost"] = (
            df["Medical costs"] * df["Visit counts"]
        )
        print("\n----- Total Medical Cost -----")
        print(df["Patients","Total medical cost"])
        print("\n----- Sort Patients By Total Medical Cost -----\n")
        print(df.sort_values(
            by="Total medical cost" ,ascending=False
        ))
        print("\n----- Statistical Description -----\n")
        print(df.describe())
        print("\n----- Total Medical Cost By Departmment -----\n")
        print(df.groupby("Departments")["Total medical cost"].sum())
# Exit
    elif choice == 11 :
        print("Goodbay")
        break

    else :
        print("Please enter choice number !")

10/11/2026