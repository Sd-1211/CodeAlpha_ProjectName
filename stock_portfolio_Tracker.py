stock_price = {
    "TCS": 3540,
    "INFY": 1550,
    "WIPRO": 480,
    "HDFC": 1620,
    "ICICI": 960,
    "AXIS": 1080,
    "SBIN": 600,
    "RELIANCE": 2800,
    "ADANIPORTS": 1260,
    "ADANIGREEN": 910,
    "BAJAJFIN": 7200,
    "ITC": 440,
    "MARUTI": 10200,
    "HUL": 2500,
    "SUNPHARMA": 1350,
    "ONGC": 195,
    "COALINDIA": 360,
    "NTPC": 345,
    "POWERGRID": 270,
    "TITAN": 3450
}
print("-"*15)
print(f"{'Stock':<12}{'Price':10}")
print("-"*15)
for stock,price in stock_price.items():
    print(f"{stock:<12}{price:<10}")
while True:
    print("*"*25)
    print("Stock Portfolio Tracker")
    print("*"*25)
    print("\n1.Available Stock Details:")
    print("\n2.Buying Single Stock")
    print("\n3.Buying Multiple Stocks")
    print("\n4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("-"*15)
        print(f"{'Stock':<8}{'Price'}")
        print("-"*15)
        for stock,price in stock_price.items():
            print(f"{stock:<8}{price}")
    elif choice==2:
        portfolio=[]
        stock_name=input("Enter the Stock Name:").upper()
        if stock_name not in stock_price:
            print("Stock Not Found")
        else:
            try:
                quantity = int(input(f"Enter Quantity for the Stock {stock_name}:"))
                result = stock_price[stock_name] * quantity
                portfolio.append((stock_name, quantity, stock_price[stock_name], result))
                print("\n====== Your Portfolio ======")
                print(f"{'Stock':<8}{'Quantity':<10}{'Price':<10}{'Value'}")
                print("-" * 40)
                for stock, qty, price, value in portfolio:
                    print(f"{stock.upper():<8}{qty:<10}{price:<10}{value}")
                print("-" * 40)
                print(f"{'Total Portfolio Value:':<28}{result}")
            except ValueError:
                print("Invalid input. Enter a Number..!")
        with open("portfolio.txt","w")as f:
            f.write(f"{'stock':<8}{'Quantity':<10}{'Price':<10}{value}\n")
            f.write("-" * 40+"\n")
            for stock,quantity,price,value in portfolio:
                f.write(f"{stock:<8}{quantity:<10}{price:<10}{value}\n")
            f.write("-" * 40+"\n")
            f.write(f"{'Total Portfolio Value:':<28}{result}\n")
    elif choice==3:
        stock_details=[]
        print("If You want to Stop Adding the Stocks...Type EXIT")
        while True:
            stock_name=input("Enter Stock Name:").upper()
            if stock_name == "EXIT":
                break
            if stock_name not in stock_price:
                print("Stock Not Found")
                continue
            try:
                quantity=int(input(f"Enter Quantity for the Stock {stock_name}:"))
            except ValueError:
                print("Invalid input.Enter a NUmber..!")
                continue
            stock_details.append((stock_name,quantity,stock_price[stock_name]))
        total_value=0
        print("\nYour Portfolio:")
        print(f"{'Stock':<8}{'Quantity':<10}{'Price':<10}{'Value'}")
        print("-" * 40)
        for stock, qty, price in stock_details:
            value = qty * price
            total_value += value
            print(f"{stock:<8}{qty:<10}{price:<10}{value}")
        print("-" * 40)
        print(f"{'Total Portfolio Value:':<28}{total_value}")
        with open("stock_details.txt","w")as f:
            f.write(f"{'Stock':<8}{'Quantity':<10}{'Price':<10}{'Value'}\n")
            f.write("-"*40+'\n')
            total_value=0
            for stock,quantity,price in stock_details:
                value = quantity * price
                total_value += value
                f.write(f"{stock:<8}{quantity:<10}{price:<10}{value}\n")
            f.write("-"*40+"\n")
            f.write(f"{'Total Portfolio Value:':<28}{total_value}\n")
    elif choice == 4:
        print("Existing Portfolio Tracer..!!")
        break

    else:
        print("Please Enter Valid Choice.")
        