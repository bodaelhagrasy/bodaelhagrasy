# نظام اداره طلبات متجر الكتروني

customers = ["Ahmed", "Mona", "Ali", "Omar"]
products = ["Laptop", "Phone", "Headphones", "Keyboard"]
prices = [25000, 12000, 1500, 800]
quantities = [1, 2, 3, 2]
statuses = ["Pending", "Delivered", "Cancelled", "Pending"]

while True :
    print(
        "========== E-Commerce Order Management ==========\n\n"
        "1. Show All Orders\n"
        "2. Add New Order\n"
        "3. Search Order\n"
        "4. Update Order\n"
        "5. Remove Order\n"
        "6. Calculate Order Total\n"
        "7. Sales Statistics\n"
        "8. Show Orders by Status\n"
        "9. Sort Orders by Total Price\n"
        "10. Search Orders by Price Range\n"
        "11. Show Customer Orders\n"
        "12. Exit\n"
    )
    try :
# ادخال الاختيار
        choice = int(input("Enter choice number :"))
    except ValueError :
        print("Please enter choice number !")
        continue
# عرض جميع الطلبات
    if choice == 1 :
        if not customers :
            print("No customers found !")
            continue
        for i,customer in enumerate(customers,1) :
            print(f"{i}.{customer} -Product :{products[i-1]} -Prices :{prices[i-1]} -Quantities :{quantities[i-1]} -Statuse :{statuses[i-1]}")
# اضافه طلب جديد
    elif choice == 2 :
        customer = input("Enter the new client's name :").strip()
        if not customer :
            print("Please enter client's name !")
            continue
        product = input("Enter the product name :").strip()
        if not product :
            print("Please enter product name !")
            continue
        try :
            price = int(input("Enter the product price :")) 
        except ValueError :
            print("Pleae enter the product price 1")
            continue
        if 0 >= price :
            print("The price must be greater than zero !")
            continue
        try :
            quant = int(input("Enmter the product quantite :"))
        except ValueError :
            print("Please enter the product quantite !")
            continue
        if 0 >= quant :
            print("The quantites must be greater than zero !")
            continue
        print("Select from these statuses: Pending, Delivered, and Cancelled.")
        statuse = input("Enter the product statuse :").strip()
        if not statuse :
            print("Please enter product atatuse !")
            continue
        if statuse.lower() in ["pending","delivered","cancelled"] :
            customers.append(customer)
            products.append(product)
            quantities.append(quant)
            prices.append(price)
            statuses.append(statuse)
            print("The request has been added.")
        else :
            print("Please enter the correct order status !")
# البحث عن طلب
    elif choice == 3 :
        customer = input("Enter the new client's name :").strip().lower()
        if not customer :
            print("Please enter client's name !")
            continue
        if customer in [name.lower() for name in customers] :
            index = [name.lower() for name in customers].index(customer)
            print(f"Customer :{customers[index]} -Product :{products[index]} -Prices :{prices[index]} -Quantities :{quantities[index]} -Statuse :{statuses[index]}")
        else :
            print("No costomer found !")
# تعديل علي طلب موجود
    elif choice == 4 :
        customer = input("Enter the new client's name :").strip().lower()
        if not customer :
            print("Please enter client's name !")
            continue
        if customer in [name.lower() for name in customers] :
            index = [name.lower() for name in customers].index(customer)
            try :
                price = int(input("Enter the product price update :"))
            except ValueError :
                print("Please enter the product price update !")
                continue
            if price == prices[index] :
                print("The old price is equal to the new price !")
                continue
            elif 0 >= price :
                print("The price must be greater than zero !")
                continue
            else :
                try :
                    quant = int(input("Enmter the product quantite :"))
                except ValueError :
                    print("Please enter the product quantite !")
                    continue
                if 0 >= quant :
                    print("The quantites must be greater than zero !")
                    continue
                elif quant == quantities[index] :
                    print("The old quantitie is equal to the new quantitie !")
                    continue
                else :
                    statuse = input("Enter the product statuse :").strip()
                    if not statuse :
                        print("Please enter product atatuse !")
                        continue
                    if statuse.lower() in ["pending","delivered","cancelled"] :
                        prices[index] = price
                        quantities[index] = quant
                        statuses[index] = statuse
                        print("The product has been modified.")
                    else :
                        print("Please enter the correct order status !")
# حذف طلب
    elif choice == 5 :
        customer = input("Enter the new client's name :").strip().lower()
        if not customer :
            print("Please enter client's name !")
            continue
        if customer in [name.lower() for name in customers] :
            index = [name.lower() for name in customers].index(customer)
            print(f"Customer :{customers[index]} -Product :{products[index]} -Prices :{prices[index]} -Quantities :{quantities[index]} -Statuse :{statuses[index]}")
            confirm = input("Do you really want to delete it? yes/no").strip().lower()
            if not confirm :
                print("Please enter yes/no !")
                continue
            if confirm == "yes" :
                customers.pop(index)  
                products.pop(index)
                quantities.pop(index)
                prices.pop(index)
                statuses.pop(index)
                print("The client has been deleted.")
            elif confirm == "no" :
                print("The deletion has been reversed.")
            else :
                print(f"This choice {confirm} mistake !")
        else :
            print(f"No {customer} found")
# اجمالي طلب العميل
    elif choice == 6 :
        customer = input("Enter the new client's name :").strip().lower()
        if not customer :
            print("Please enter client's name !")
            continue
        if customer in [name.lower() for name in customers] :
            index = [name.lower() for name in customers].index(customer)
            order_price = prices[index]*quantities[index]
            descond = 0
            if order_price > 15000 :
                descond += order_price * .10 
            elif 5000<= order_price <= 15000 :
                descond += order_price * .05
            total_price = order_price - descond 
            print(f"Customer :{customers[index]}\nProduct :{products[index]}\nPrice :{prices[index]}\nQuantities :{quantities[index]}\nOrder price :{order_price}\nDiscond :{descond} Total price :{total_price}")
        else :
            print(f"No {customer} found !")
# عرض احصائيات الطلبات
    elif choice == 7 :
        total_order = len(customers)
        delivered_count = 0
        pending_count = 0
        cancelled_count = 0
        total_sales = 0
        for index in range(len(statuses)) :
            statuse = statuses[index].lower()
        if statuse == "delivered" :
            delivered_count += 1
            total_sales += prices[index] * quantities[index]
        elif statuse == "pending" :
            pending_count += 1
        elif statuse == "cancelled" :
            cancelled_count += 1
        if delivered_count > 0 :
            averge_order = total_sales / delivered_count
        else :
            averge_order = 0
        print(
            f"Total orders :{total_order}\n"
            f"Delivered orders :{delivered_count}\n"
            f"Pending orders :{pending_count}\n"
            f"Cancelled oreders :{cancelled_count}\n"
            f"Average Dalivered order :{averge_order}\n"
        )
# عرض الطلبات من خلال حاله البيع
    elif choice == 8 :
        statuse = input("Enter the product statuse :").strip().lower()
        if not statuse :
                print("Please enter product atatuse !")
                continue
        if statuse in ["pending","delivered","cancelled"] :
            found = False
            for index in range(len(statuses)) :
                if statuse == statuses[index].lower() :
                    print(
                        f"Customre :{customers[index]}\n"
                        f"Product :{products[index]}"
                        f"Price :{prices[index]}\n"
                        f"Quantitie :{quantities[index]}\n"
                    )
                    found = True
            if not found :
                print("No order found !")
        else :
            print("Please enter the statuse name !")
# عرض ترتيب الاسعار
    elif choice == 9 :
        if not customers :
            print("No order found !")
            continue
        sorted_price = sorted(prices)
        print("-----Ascending order-----")
        for price in sorted_price :
            index = prices.index(price)
            print(f"Custmer : {customers[index]} -Price : {prices[index]}")
        print("-----Descending order-----")
        sorted_price = sorted(prices, reverse=True)
        for price in sorted_price :
            index = prices.index(price)
            print(
                f"Customer : {customers[index]}"
                f"Price : {prices[index]}"
            )
# البحث عن طلبات من خلال رينج السعر
    elif choice == 10 :
        try :
            min_price = int(input("Enter minmum price :"))
            max_price = int(input("Enter maxmum price :"))
        except ValueError :
            print("Please enter valid price !")
        if min_price >= max_price : 
            print("Invalid range ! minimum price cannot exced maximum price !")
            continue
        found =False
        for i in range(len(prices)) :
            if min_price <= prices[i] <= max_price :
                print(
                    f"Customers : {customers[i]}\n"
                    f"Product : {products[i]}\n"
                    f"Price : {prices[i]}\n"
                    f"Quantites : {quantities[i]}\n"
                    f"Statuses : {statuses[i]}"
                    )
                found = True
        if not found :
            print("No order found !")
# عرض جميع طلبات عميل معين باستخدام الاسم
    elif choice == 11 :
        customer = input("Enter customer name :").strip().lower()
        if not customer :
            print("Please enter custmer name !")
            continue
        if customer in[name.lower()for name in customers] :
            found =False
            for customer in range(len(customers)) :
                index = customers.index(customer)
                print(
                    f"Customers : {customers[index]}\n"
                    f"Product : {products[index]}\n"
                    f"Price : {prices[index]}\n"
                    f"Quantites : {quantities[index]}\n"
                    f"Statuses : {statuses[index]}"
                )
                found = True
            if not found :
                print("No order found !")
# خروج
    elif choice == 12 :
        print ("Good bay")
        break
# ادخال رقم خطا
    else :
        print("Please enter choice number !")

# الحمد الله 
# 23/10/2026