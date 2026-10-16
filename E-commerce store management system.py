# نظام إدارة متجر التجارة الإلكترونية
products = ["Laptop", "Phone", "Headphones", "Mouse"]
prices = [20000, 12000, 1500, 500]
stock = [5, 10, 15, 20]
cart_products = []
cart_quantities = []
total_sales = 0
total_successful = 0
while True:
    print("===== E-COMMERCE STORE =====")

    print("\n1. Show All Products")
    print("2. Add New Product")
    print("3. Search Product")
    print("4. Add Product to Cart")
    print("5. Remove Product from Cart")
    print("6. View Shopping Cart")
    print("7. Checkout")
    print("8. Store Statistics")
    print("9. Exit")

    choice = int(input("Enter your choice :")) 
# عرض المنتجات
    if choice == 1 :
        if products :
            for number,product in enumerate(products,1) :
                print(f"{number}.{product}\nPrice :{prices[number -1]}\nStock :{stock[number -1]}")
        else:
            print("No products available!")
# اضافه منتج جديد 
    if choice == 2 :
        product = input("Enter product name add :")
        if product in products :
            print("Product exsit !")
        else :
            price = int(input("Enter price :"))
            if price > 0 :
                quantitie = int(input("Enter quantite :"))
                if quantitie >= 0 :
                    products.append(product)
                    prices.append(price)
                    stock.append(quantitie)
                    print("Added successful !")
                    total_successful += 1
                else :
                    print("incorrect !")
            else :
                print("The price must be higher than zero !")
# البحث عن منتج
    if choice == 3 :
        product = input("Enter product")
        if product in products :
            index = products.index(product)
            print(f"Product :{product}\nPrice :{prices[index]}\nStock :{stock[index]}")
        else :
            print("Not found !")
# اضافه منتج الي عربيه التسوق 
    elif choice == 4 :
        product = input("Enter product name :")
        if product in products :
            index = products.index(product)
            if product in cart_products :
                quantitie = int(input("Enter quantites :"))
                if quantitie <= stock[index] :
                    index1 = cart_products.index(product)
                    cart_quantities[index1] += quantitie
                    total_successful += 1
                    print("product add cart ")
                else :
                    print("Quantity not available")
            else  :
                quantitie = int(input("Enter quantites :"))
                if quantitie <= stock[index] :
                    cart_products.append(product)
                    cart_quantities.append(quantitie)
                    stock[index] -= quantitie
                    total_successful += 1
                    print("product add cart ")
                else :
                    print("Quantity not available")
        else :
            print("Not found !")
# ازاله منتج من العربه
    elif choice == 5 :
        product = input("Enter product name removed :")
        if product in cart_products :
            index = cart_products.index(product)
            index1 = products.index(product)
            entire = input("The entire quantity : yes/no")
            if entire == "yes" :
                cart_products.remove(product)
                cart_quantities.remove(index)
                print("Product removed !")
            elif entire == "no" :
                quantitie = int(input("Specify the quantity to be scanned :"))
                if quantitie < cart_quantities[index] :
                    cart_quantities[index] -= quantitie
                    stock[index1] += quantitie
                    print("The quantity has been reduced.")
                else :
                    print("A wrong choice !")
        else :
            print("Not found !")
# عرض المنتجات التي في العربه
    elif choice == 6 :
        total_sales = 0
        if cart_products :
            for number,product in enumerate(cart_products,1) :
                price_product = prices[products.index(product)] * cart_quantities[number-1]
                print(f"{number}.{product} - Price :{prices[products.index(product)]} - Quantite :{cart_quantities[number-1]} - Total :{price_product}")
                total_sales += price_product
                print(f"Total :{total_sales}")
        else :
            print("No products in cart !")
# الدفع
    elif choice == 7:
        if cart_products:
            total_sales = 0
            for number,product in enumerate(cart_products):
                index = products.index(product)
                total_sales += prices[index] * cart_quantities[number]
            print(f"Total before discount: {total_sales} EGP")
            discount = 0
            if total_sales >= 25000:
                discount = total_sales * 0.10
            final_total  = total_sales - discount
            print(f"Discount: {discount} EGP")
            print(f"Final total: {final_total} EGP")
            payment = int(input("Enter payment: "))
            if payment >= final_total:
                change = payment - final_total
                print("Payment successful!")
                print(f"Change: {change} EGP")
                for number, product in enumerate(cart_products):
                    index = products.index(product)
                    stock[index] -= cart_quantities[number]
                total_successful += 1
                cart_products.clear()
                cart_quantities.clear()
            else:
                print("Not enough money!")
        else:
            print("Shopping cart is empty!")
# عرض احصائيات المتجر
    elif choice == 8 :
        average = sum(prices)/len(prices)
        print(f"number product :{len(prices)}"
            f"stock : {sum(stock)}"
            f"Average product prices :{average}"
            f"Highest and lowest prices :{max(prices)}-{min(prices)}"
            f"Total successful sales :{total_successful}")
# خروج
    elif choice == 9 :
        print("goodbye !")
        break
    else :
        print("Invalid choice !")