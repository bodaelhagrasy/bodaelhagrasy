products = ["Laptop", "Mouse", "Keyboard", "Headphones"]
prices = [15000, 500, 800, 1500]
quantities = [5, 20, 12, 8]
sold = [0, 0, 0, 0]
categories = ["Computer", "Accessories", "Accessories", "Accessories"]


while True :
    print("INVENTORY & SALES MANAGEMENT\n")
    print("1. Show All Products")
    print("2. Add New Product")
    print("3. Search Product")
    print("4. Sell Product")
    print("5. Restock Product")
    print("6. Inventory & Sales Statistics")
    print("7. Sort Prices")
    print("8. Count Products by Category")
    print("9. Exit")

    try :
        choice = int(input("Enter choice :"))
    except ValueError :
        print("Please enter numper choice !")
        continue
# عرض المنتجات كلها
    if choice == 1 :
        if products :
            for number,product in enumerate(products,1) :
                print(f"{number}.{product} - Price :{prices[number-1]} -Quantities :{quantities[number-1]} -Sold :{sold[number-1]}")
        else :
            print("Not found !")
# اضافة منتج جديد
    elif choice == 2 :
        product = input("Enter product add :").strip()
        if not product :
            print("Please enter name product !")
            continue
        if product.lower() in [name.lower() for name in products] :
            print("Product exsit !")
            continue
        try :
            price = int(input("Enter price product :"))
        except ValueError :
            print("Please enter number price !")
            continue
        if price <= 0 :
            print("The price must be greater than zero !")#احنا هنهزر يبني
            continue
        try :
            quant = int(input('Enter quantites product :'))
        except ValueError :
            print("Please enter number quanites !")
            continue
        if quant < 0 :
            print("The quantity must be greater than zero !")
            continue
        num_sold = 0
        products.append(product)
        prices.append(price)
        quantities.append(quant)
        sold.append(num_sold)
        print("product added successful !")
# البحث عن منتج
    elif choice == 3 :
        product = input("Enter prodect name :").strip()
        if not product :
            print("Please enter name product !")
            continue
        if product.lower() in [name.lower() for name in products] :
            index = [name.lower()for name in products].index(product.lower())
            print(f"Product :{product.lower()}\nPrice :{prices[index]}\nQuantities :{quantities[index]}\nSold{sold[index]}")
        else :
            print("Not found productes !")
# البيع عيزين فلوس مش في البرنامج في الحقيقه
    elif choice == 4 :
        product = input("Enter prodect nember :").strip()
        if not product :
            print("Please enter product name !")
            continue
        if product.lower() in [name.lower() for name in products] :
            index = [name.lower() for name in products].index(product.lower())
            print(f"Product found\nProduct :{product} -Price :{prices[index]} -Quantities :{quantities[index]}")
            try :
                quant = int(input("Enter Order the required quantity :"))
            except ValueError :
                print("Please enter number quantities !")
                continue
            if quant > 0 :
                if quant <= quantities[index] :
                    try :
                        payment = int(input("Enter the payment amount :"))
                    except ValueError :
                        print("Please enter payment")
                        continue
                    total_price = prices[index] * quant
                    if payment >0 :
                        if payment >= total_price :
                            change =  payment - total_price
                            quantities[index] -= quant
                            sold[index] += quant
                            print(f"successful\nProduct :{product}\nQuantites :{quant}\nTotal price :{total_price}\nChange :{change}")
                        else :
                            print("There isn't enough money !")
                    else :
                        print("No enough money")
                else :
                    print("The quantity is insufficient !")
            else :
                print("The quantity must be greater than zero !")
# زياده مخزون منتج معين
    elif choice == 5 :
        product = input("Enter product name :").strip()
        if not product :
            print("please enter name product !")
            continue
        if product.lower() in[name.lower() for name in products] :
            index = [name.lower() for name in products].index(product.lower())
            print("Product founde !")
            try :
                quant =int(input("Enter the stock quantity :"))
            except ValueError :
                print("Pleae enter the stock quantity !")
                continue
            if quant > 0 :
                quantities[index] += quant
                print("The inventory has been increased !")
            else :
                print("That won't work.")
        else :
            print("Print not found !")
# عرض عدد المنتجات واجمالي الكميه المتاحه والمباعه وقيمه المخزون ومتوسط الاسعار واعلي سعر واقل سعر 
# انا بكتب تعبير ايه الشغلانه دي
    elif choice == 6 :
        if not products :
            print("No products")
            continue
        
        print(f"Number of products :{len(products)}\nTotal available quantities :{sum(quantities)}\nTotal quantities sold :{sum(sold)}\nHigt prices :{max(prices)}\nLow prices :{min(prices)}\nAverage prices :{round(sum(prices)/len(prices))}")
# عرض الاسعار من الاصغر للاكبر والعكس
    elif choice == 7 :
        print(f"Prices from lowest to highest :{sorted(prices)}")
        print(f"Prices from highest to lowest :{sorted(prices, reverse=True)}")
# دي الصراحه كانت جديده ولجات لمساعه هنا  علي الامر 
# انشاء قائمه تحتوي علي تصنيف المنتجات
    elif choice == 8 :
        category = input("Enter category: ").strip()
        if not category :
            print("Please enter category !")
            continue
        if category.lower() in [categ.lower() for categ in categories] :
            categor =[categ.lower() for categ in categories].count(category.lower())
            print(f"category :{category}\nNumber :{categor}")
        else :
            print("Category not found !")
# الخروج 
    elif choice == 9 :
        print("Good bay")
        break
    else :
        print("Plese enter number choice !")
#الحمد الله خلصت  