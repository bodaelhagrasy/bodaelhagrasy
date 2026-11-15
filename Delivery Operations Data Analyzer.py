delivery_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
customers = ["Ahmed", "Mona", "Ali", "Omar","Sara", "Youssef", "Nour"]
cities = ["Cairo", "Alexandria", "Giza", "Cairo","Mansoura", "Giza", "Alexandria"]
delivery_fees = [50, 80, 40, 60, 70, 45, 90]
delivery_times = [2, 5, 1, 3, 4, 2, 6]
distances = [10, 25, 8, 15, 20, 12, 30]
statuses = ["Delivered", "Pending", "Delivered","Cancelled", "Delivered", "Pending", "Delivered"]

while True :
    print(
    "\n===== Delivery Operations Data Analyzer =====\n\n"
    "1. Show All Deliveries\n"
    "2. Add New Delivery\n"
    "3. Search Delivery\n"
    "4. Update Delivery Data\n"
    "5. Remove Delivery\n"
    "6. Calculate Delivery Statistics\n"
    "7. Analyze Delivery Performance\n"
    "8. Sort Deliveries\n"
    "9. Filter Deliveries\n"
    "10. Analyze Data Using Pandas\n"
    "11. Exit\n"
    )

    try :
        choice = int(input("Enter choice number :"))
    except ValueError :
        print("Please enter choice number !")
        continue

    if choice == 1 :
        if not customers :
            print("No customers found !")
        else :
            for number,customer in enumerate(customers,1) :
                print(
                    f"{number}.Delivery id :{delivery_ids[number-1]} -Customer :{customer} -city :{cities[number-1]} -Delivery fee :{delivery_fees[number-1]} -Delivery time :{delivery_times[number-1]} -Distance :{distances[number-1]} -Statuses :{statuses[number-1]}"
                )  

    elif choice == 2 :
        try :
            delivery_id = int(input("Enter delivery id :"))
        except ValueError :
            print("Plrase enter delivery id !")
            continue
        for i in range(len(delivery_ids)) :
            if delivery_ids[i] == delivery_id :
                print("The delivery id old equal new delivery id !")
                continue
        if 0 >= delivery_id :
            print("The delivery id must be equal zero !")
        else :
            customer = input("Enter customer name :").strip()
            if not customer :
                print("Please emter customer name !")
                continue
            city = input("Enter city name :").strip()
            if not city :
                print("Please enter city name !")
                continue
            try :
                delivery_fee = int(input("Enter delivery fees :"))
            except ValueError :
                print("Please enter delivery fees !")
                continue
            if 0 >= delivery_fee :
                print("The delivery fee must be equal zero !")
            else :
                try :
                    delivery_time = int(input("Enter delivery time :"))
                except ValueError :
                    print("Please enter delivery time !")
                    continue
                if 0 >= delivery_time :
                    print("The delivery time must be equal zero !")
                else :
                    try :
                        distance = int(input("Enter distances :"))
                    except ValueError :
                        print("Please enter distance !")
                        continue
                    if 0 >= distance :
                        print("The distance must be equal zero !")
                    else :
                        print("The status can be Delivered, Pending, or Cancelled.")
                        statuse = input("Enter statuse :").strip()
                        if not statuse :
                            print("Please enter statuse !")
                            continue
                        stat = ["delivered","pending","cancelled"]
                        if statuse.lower() in stat :
                            delivery_ids.append(delivery_id)
                            customers.append(customer)
                            cities.append(city)
                            delivery_fees.append(delivery_fee)
                            delivery_times.append(delivery_time)
                            distances.append(distance)
                            statuses.append(statuse)
                            print("\n Add New Delivery Successful\n")
                        else :
                            print("The status can be Delivered, Pending, or Cancelled.")

    elif choice == 3 :
        try :
            delivery_id = int(input("Enter delivery id shear :"))
        except ValueError :
            print("Please enter delivery id !")
            continue
        for i in range(len(delivery_ids)) :
            if delivery_ids[i] == delivery_id :
                print(f"\nDelivery id :{delivery_ids[i]}\nCustomer :{customers[i]}\ncity :{cities[i]}\nDelivery fee :{delivery_fees[i]}\nDelivery time :{delivery_times[i]}\nDistance :{distances[i]}\nStatuses :{statuses[i]}")

    elif choice == 4 :
        try :
            delivery_id = int(input("Enter delivery id updata :"))
        except ValueError :
            print("Please enter delivery id !")
            continue
        if delivery_id in delivery_ids :
            index = delivery_ids.index(delivery_id)
            print("\n----- Update Delivery Data -----\n")
            while True :
                print(
                    "1. Customer Name\n"
                    "2. City\n"
                    "3. Delivery Fee\n"
                    "4. Delivery Time\n"
                    "5. Distance\n"
                    "6. Status\n"
                )
                try :
                    choice = int(input("Emter choice number :"))
                except ValueError :
                    print("Please enter choice number !")
                    continue
                if choice == 1 :
                    customer = input("Enter new customer Name :").strip()
                    if not customer :
                        print("Please enter Customer Name !")
                        continue
                    lower_customer = [name.lower() for name in customers]
                    if customer.lower() in lower_customer :
                        print("New customer name equal old customer name !")
                    else :
                        customers[index] = customer
                        print("\nSuccessful updata\n")
                        break
                elif choice == 2 :
                    city = input("Enter new city Name :").strip()
                    if not city :
                        print("Please enter city Name !")
                        continue
                    lower_city = [name.lower() for name in cities]
                    if city.lower() in lower_city :
                        print("New city name equal old city name !")
                    else :
                        cities[index] = city
                        print("\nSuccessful updata\n")
                        break
                elif choice == 3 :
                    try :
                        delivery_fee = int(input("Emter new delivery fee :"))
                    except ValueError :
                        print("Please enter new delivery fee !")
                        continue
                    if delivery_fee == delivery_fees[index] :
                        print("The old delivery fee equal new delivery fee !")
                    elif 0 >= delivery_fee :
                        print("The delivery fee must be equal zero !")
                    else :
                        delivery_fees[index] = delivery_fee
                        print("\nsuccessful updata\n")
                        break
                elif choice == 4 :
                    try :
                        delivery_time = int(input("Emter new delivery time :"))
                    except ValueError :
                        print("Please enter new delivery time !")
                        continue
                    if delivery_time == delivery_times[index] :
                        print("The old delivery time equal new delivery time !")
                    elif 0 >= delivery_time :
                        print("The delivery time must be equal zero !")
                    else :
                        delivery_times[index] = delivery_time
                        print("\nsuccessful updata\n")
                        break
                elif choice == 5 :
                    try :
                        distance = int(input("Emter new distance  :"))
                    except ValueError :
                        print("Please enter new distance  !")
                        continue
                    if distance == distances[index] :
                        print("The old distance  equal new distance  !")
                    elif 0 >= distance :
                        print("The distance  must be equal zero !")
                    else :
                        distances[index] = distance
                        print("\nsuccessful updata\n")
                        break
                elif choice == 6 :
                    print("\nThe status can be Delivered, Pending, or Cancelled.")
                    statuse = input("\nEnter statuse :").strip()
                    if not statuse :
                        print("\nPlease enter statuse !")
                        continue
                    stat = ["\ndelivered","pending","cancelled"]
                    lower_statuse = [name.lower() for name in statuses]
                    if statuse.lower() == lower_statuse[index] : 
                        print("\nThe old statuse equal new statuse !")
                    elif statuse.lower() in stat :
                        statuses[index] = statuse
                        print("\nSuccessful updata\n")
                        break
                    else :
                        print("\nPlease enter statuse !")

    elif choice == 5 :
        try :
            delivery_id = int(input("\nEnter delivery id delet :"))
        except ValueError :
            print("\nPlease enter delivery id delet !")
            continue
        if delivery_id in delivery_ids :
            index = delivery_ids.index(delivery_id)
            sure = input("\nAre you sure about the deletion process? yes/no :")
            if sure == "yes" :
                delivery_ids.pop(index)
                print("\nDelet successful\n")
            elif sure == "no" :
                print("The deletion has been reversed.")
            else :
                print("Please enter yes/no !")
        else :
            print("No deivery id found !")

    