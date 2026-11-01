products = ["Laptop", "Phone", "Headphones", "Keyboard", "Mouse", "Monitor", "Tablet"]
categories = ["Computer", "Mobile", "Accessories", "Accessories", "Accessories", "Computer", "Mobile"]
prices = [25000, 12000, 1500, 800, 500, 7000, 9000]
quantities_sold = [12, 25, 40, 35, 50, 15, 18]
costs = [20000, 9000, 900, 450, 250, 5500, 6500]

while True :
    print(
        "\n===== Sales & Business Data Analyzer =====\n\n"
        "1. Show All Products\n"
        "2. Add New Product\n"
        "3. Search Product\n"
        "4. Update Product Data\n"
        "5. Remove Product\n"
        "6. Calculate Sales Statistics\n"
        "7. Analyze Profits\n"
        "8. Sort Products\n"
        "9. Filter Products\n"
        "10. Analyze Data Using Pandas\n"
        "11. Exit\n"
    )
    try :
        choice = int(input("Enter choice number :"))
    except ValueError :
        print("Please enter choice number")
        continue
# Show All Products
    if choice == 1 :
        if not products :
            print("No products found !")
            continue
        if products :
            for number,product in enumerate(products,1) :
                print(f"Product :{product} -Categorie :{categories[number-1]} -Prices :{prices[number-1]} -Quantities sold :{quantities_sold[number-1]} -Costs :{costs[number-1]}")
# Add New Product
    elif choice == 2 :
        product = input("Enter product name add :").strip()
        if not product :
            print("Please enter product name !")
            continue
        if product.lower() in [name.lower() for name in products] :
            print("The  product exsist !")
            continue
        categorie = input("Enter the categorie product :").strip()
        if not categorie :
            print("Please enter categorie product !")
            continue
        try :
            price = int(input("Enter product price :"))
        except ValueError :
            print("Please enter product price !")
            continue
        if 0 >= price :
            print("The price must be than equl zero ")
            continue
        else :
            try :
                quantitie_sold = int(input("Enter quantities sold :"))
            except ValueError :
                print("Please enter quantities sold !")
                continue
            if 0 >= quantitie_sold :
                print("The quantities sold must be than equl zero !")
                continue
            else :
                try :
                    cost = int(input("Enter cost :"))
                except ValueError :
                    print("Please enter the cost !")
                    continue
                if 0 >= cost :
                    print("The cost must be than equl zero !")
                else :
                        products.append(product)
                        categories.append(categorie)
                        prices.append(price)
                        quantities_sold.append(quantitie_sold)
                        costs.append(cost)
                        print("Product added successful ")
# Search Product
    elif choice == 3 :
        product = input("Enter product name sheaer :").strip().lower()
        if not product :
            print("Please enter product name ")
            continue
        if product in [name.lower() for name in products] :
            index = [name.lower() for name in products].index(product)
            print(f"Product :{product}\nCategorie :{categories[index]}\nPrice :{prices[index]}\nQuantities sold :{quantities_sold[index]}\nCost :{costs[index]}")
        else :
            print("No product foud !")
# Update Product Data
    elif choice == 4 :
        product = input("Enter product name updata :").strip().lower()
        if not product :
            print("Please enter product name ")
            continue
        if product in [name.lower() for name in products] :
            index = [name.lower() for name in products].index(product)
            while True :
                print(
                    "\n-----choice number updata product-----\n\n"
                    "1.updata price\n"
                    "2.updata quantities sold\n"
                    "3.costs\n"
                    "4.categories"
                )
                try :
                    choic = int(input("Enter choice number :"))
                except ValueError :
                    print("Please enter choice number !")
                    continue
                if choic == 1 :
                    try :
                        price = int(input("enter price updata :"))
                    except ValueError :
                        print("Please enter price number !")
                        continue
                    if price == prices[index] :
                        print("The old value cannot be equal to the new one.")
                        continue
                    elif 0 >= price :
                        print("The price must be than equl zero !")
                        continue
                    else :
                        prices[index] = price
                        print("Updata successful")
                        break
                elif choic == 2 :
                    try :
                        quantitie = int(input("enter quantitie updata :"))
                    except ValueError :
                        print("Please enter quantitie number !")
                        continue
                    if quantitie == quantities_sold[index] :
                        print("The old value cannot be equal to the new one.")
                        continue
                    elif 0 >= quantitie :
                        print("The quantitie must be than equl zero !")
                        continue
                    else :
                        quantities_sold[index] = quantitie
                        print("Updata successful")
                        break
                elif choic == 3 :
                    try :
                        cost = int(input("enter cost updata :"))
                    except ValueError :
                        print("Please enter cost number !")
                        continue
                    if cost == costs[index] :
                        print("The old value cannot be equal to the new one.")
                        continue
                    elif 0 >= cost :
                        print("The cost must be than equl zero !")
                        continue
                    else :
                        costs[index] = cost
                        print("Updata successful")
                        break
                elif choic == 4 :
                    
                    categorie = (input("enter categorie updata :")).strip()
                    if not categorie :
                        print("Please enter categorie number !")
                        continue
                    categories[index] = categorie
                    print("Updata successful")
                    break
                else :
                    print("Please enter choice number !")
# Remove Product
    elif choice == 5 :
        product = input("Enter product name delet :").strip().lower()
        if not product :
            print("Please enter product name ")
            continue
        if product in [name.lower() for name in products] :
            index = [name.lower() for name in products].index(product)
            conferm = input("Do you really want to delete? yes/no").strip().lower()
            if not conferm :
                print("Please enter yes/no :")
                continue
            if conferm == "yes" :
                products.pop(index)
                categories.pop(index)
                prices.pop(index)
                costs.pop(index)
                quantities_sold.pop(index)
                print("Product removed successful ")
            elif conferm == "no" :
                print("The deletion has been reversed.")
            else :
                print("Please ente yes/no")
# Calculate Sales Statistics
    elif choice == 6 :
        index = quantities_sold.index(max(quantities_sold))
        print(
            f"number products :{len(products)}\n"
            f"Number quantities sold : {len(quantities_sold)}\n"
            f"Cocts :{sum(costs)}\n"
            f"Average prices :{sum(prices)/len(prices)}\n"
            f"high price :{max(prices)}\n"
            f"loow price :{min(prices)}\n"
            f"high quantites sold product name :{products[index]}"
        )
#  Analyze Profits
    elif choice == 7:
        if not products :
            print("No product found")
            continue
        for i,product in enumerate(products) :
            total_sold = prices[i] * quantities_sold[i]
            total_cost = costs[i] * quantities_sold[i]
            gross_profit = total_sold - total_cost
            print(f"product :{product} -Total sold prodect :{total_sold} -Total cost :{total_cost} -Gross Profit : {gross_profit}")
# Sort Products
    elif choice == 8 :
        if not products :
            print("No products found !")
            continue
        sorted_price = sorted(zip(prices,products))[::-1]
        print("-----Arranging items from largest to smallest-----\n")
        for price,product in sorted_price :
            print(f"Product :{product} -Price :{price}")
        print("\n-----Sort the quantity sold from largest to smallest.-----\n")
        sorted_quant = sorted(zip(quantities_sold,products))[::-1]
        for quant,product in sorted_quant :
            print(f"Product :{product} -Quantiten :{quant}")
        profits = []
        for i,product in enumerate(products) :
            total_sold = prices[i] * quantities_sold[i]
            total_cost = costs[i] * quantities_sold[i]
            gross_profit = total_sold - total_cost
            profits.append(gross_profit)
        sorted_profits = sorted(zip(profits,products))[::-1]
        print("\n-----Ranking profit from highest to lowest-----\n")
        for profit,product in sorted_profits :
            print(f"Product :{product} -Profits :{profit}")
# Filter Products
    elif choice == 9 :
        while True :
            print(
                "-----Choose how to search for the product-----\n\n"
                "1. Selling price is higher than\n"
                "2. Sales volume is greater than\n"
                "3. Profit margin higher than\n"
                "4. Products belonging to a specific category."
            )
            try :
                choic = int(input("Enter choice number :"))
            except ValueError :
                print("Please enter choice number !")
                continue
            if choic == 1 :
                try :
                    high_price = int(input("Enter Selling price is higher than :"))
                except ValueError :
                    print("Please enter price !")
                    continue
                found = False
                if 0 >= high_price :
                    print("The price must be than equl zero !")
                    continue
                else :
                    for i in range(len(prices)) :
                        if high_price <= prices[i] :
                            print(f"Product {products[i]} -Price :{prices[i]}")
                            found =True
                    if found == True :
                        break
                    elif not found :
                        print("No product found !")
                        break
            elif choic == 2 :
                try :
                    quant = int(input("Enter Sales volume is greater than :"))
                except ValueError :
                    print("Please enter Sales volume is greater than")
                    continue
                found = False
                if 0 >= quant :
                    print("The quantities must be equl zero !")
                    continue
                for i in range(len(quantities_sold)) :
                    if quant <= quantities_sold[i] :
                        print(f"Product :{product} -Quantities :{quantities_sold[i]}")
                        found =True
                    if found == True :
                        break
                    elif not found :
                        print("No product found !")
                        break
            elif choic == 3 :
                profits = []
                for i,product in enumerate(products) :
                    total_sold = prices[i] * quantities_sold[i]
                    total_cost = costs[i] * quantities_sold[i]
                    gross_profit = total_sold - total_cost
                    profits.append(gross_profit)
                try :
                    profit = int(input("Enter Profit margin higher than :"))
                except ValueError :
                    print("Please enter profit number !")
                    continue
                if 0 >= profit :
                    print("The profit must be than equl zero !")
                    continue
                else :
                    found = False
                    for i in range(len(profits)) :
                        if profit <= profits[i] :
                            print(f"Product :{products[i]} -Profit :{profits[i]}")
                            found= True
                    if found == True :
                        break
                    else :
                        print("No products found !")
                        break
            elif choic == 4 :
                category = input("Products belonging to a specific category :").strip()
                if not category :
                    print("Pleasee enter category !")
                    continue
                found = False
                if category.lower() in[name.lower() for name in categories] :
                    for i in range(len(categories)) :
                        if category.lower() ==  categories[i].lower() :
                            print(f"product :{products[i]} -Category :{categories[i]}")
                            found = True
                    if found == True :
                        break
                    else :
                        print("No product found !")
                        break
            else :
                print("Please enter choice number !")
# Analyze Data Using Pandas
    elif choice == 10 :
        import pandas as pd
        data = {
            "Products" : products ,
            "Category" : categories ,
            "Price" : prices ,
            "Quantites" : quantities_sold ,
            "Costs" : costs
        }
        df = pd.DataFrame(data)
        print(df)
        print("\n-----Average selling price-----\n")
        print(df["Price"].mean())
        print("\n-----Total quantities sold-----\n")
        print(df.sum(df["Quantities"]))
        print("\n-----Products with a price greater than or equal to 5000.-----\n")
        high_price = df[df["Price"] >= 5000 ]
        print(high_price)
        print("\n-----Products with a sales quantity greater than or equal to 20.-----\n")
        quant = df[df["Quantities"] >= 20]
# Exit
    elif choice == 11 :
        print("Goodbay")
        break

    else :
        print("Please enter choice number !")


# 1/11/2026
