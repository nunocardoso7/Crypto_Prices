import cbpro
import colorama
from colorama import Back, Fore, Style
import platform
import os
import sys




colorama.init(autoreset=True)


clear_command = "cls" if platform.system() == "Windows" else "clear"

os.system(clear_command)

public_client = cbpro.PublicClient()

result = public_client.get_products()

# for row in result:
#     print(row)



def Crypto_prices():


    BTC_price = public_client.get_product_ticker('BTC-EUR')
    print(Fore.YELLOW + "\nBTC:", BTC_price['price'], "€")

    ETH_price = public_client.get_product_ticker('ETH-EUR')
    print(Fore.BLUE + "ETH:", ETH_price['price'], "€")

    ADA_price = public_client.get_product_ticker('ADA-EUR')
    print(Fore.CYAN + "ADA:", ADA_price['price'], "€")

    # EGLD_price = public_client.get_product_ticker('EGLD-EUR')
    # print (Fore.BLUE + "EGLD:",EGLD_price['price'], "€")

    SOL_price = public_client.get_product_ticker('SOL-EUR')
    print(Fore.GREEN + "SOL:", SOL_price['price'], "€")

    AVAX_price = public_client.get_product_ticker('AVAX-EUR')
    print(Fore.RED + "AVAX:", AVAX_price['price'], "€")

    BCH_price = public_client.get_product_ticker('BCH-EUR')
    print(Fore.GREEN + "BCH:", BCH_price['price'], "€")

    LTC_price = public_client.get_product_ticker('LTC-EUR')
    print(Fore.LIGHTWHITE_EX + "LTC:", LTC_price['price'], "€")

    opc2 = ""
    while opc2 != "exit":

        opc2 = input("\n>_: ")

        if opc2 == "exit":
            print("A sair...")
        elif opc2 == "000":  # Secret command
            sys.exit()



def list():


    for row in result:
        print(row['id'])


    opc3 = ""
    while opc3 != "exit":

        opc3 = input("\n>_: ")

        if opc3 == "exit":
            print("A sair...")
        elif opc3 == "000":  # Secret command
            sys.exit()






def search_asset():

    x = input("Digit the name of the asset: ")

    X_price = public_client.get_currencies()

    for x in X_price:
        print(x)
    #print("BCH:", X_price['price'], "€")



def last_trades():

    y = input("Digit the pair of the asset(Ex: BTC-EUR): ")
    num_trades = int(input("Number of trades that you want to see? "))

    lasttrades = public_client.get_product_trades(y)

    print(f"\nThe last {num_trades} trades")
    for s in range(num_trades):
        print(next(lasttrades))



    opc4 = ""
    while opc4 != "exit":

        opc4 = input("\n>_: ")

        if opc4 == "exit":
            print("A sair...")
        elif opc4 == "000":  # Secret command
            sys.exit()




opc = ""
while opc != "exit":
    os.system(clear_command)


    print("\n===================================================")
    print("                     Crypto Prices")
    print("===================================================")
    print("  [1] - Show Crypto Prices")
    print("  [2] - List of assets")
    print("  [3] - Search an asset")
    print("  [4] - Last trades")
    print("  [exit]")
    print("===================================================")


    opc = input("Choose an option: ")

    if opc == "1":
        os.system(clear_command)
        print("\nCrypto Prices:")
        Crypto_prices()
    elif opc == "000": # Secret command
        os.system(clear_command)
        sys.exit()
    elif opc == "2":
        os.system(clear_command)
        print("List of Cryptos")
        list()
    elif opc == "3":
        os.system(clear_command)
        print("List of Cryptos")
        search_asset()
    elif opc == "4":
        os.system(clear_command)
        print("Last trades")
        last_trades()
    elif opc == "exit":
        print("\nA sair...")
    else:
        print(Fore.RED + "\nERROR! - INVALID OPTION!")










