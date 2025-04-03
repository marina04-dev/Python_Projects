from requests import get
from pprint import PrettyPrinter

API_KEY = "562ddaf40c95f5d58108"
BASE_URL = "https://free.currconv.com/"

printer = PrettyPrinter()
def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    data = list(data.items())
    data.sort()
    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()
    if len(data) == 0:
        print("Invalid Currencies")
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid Amount!")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()
    print("\tWelcome To The Currency Conventer!")
    print("Menu")
    print("1. List - lists the different currencies")
    print("2. Convert - convert from one currency to another")
    print("3. Rate - get the exchange rate of two currencies")
    print("0. Exit - exit of the program")

    while True:
        command = input("Enter the number of the option you want: ")
        if command.isdigit():
            command = int(command)
            if command == 1:
                print_currencies(currencies)
            elif command == 2:
                currency1 = input("Enter a base currency ID: ").upper()
                amount = input(f"Enter an amount in {currency1}: ")
                currency2 = input("Enter a currency ID to convert to: ").upper()
                if amount.isdigit():
                    amount = float(amount)
                    convert(currency1, currency2, amount)
                else:
                    print("Wrong Amount Input! Only Digits Please!")

            elif command == 3:
                currency1 = input("Enter a base currency ID: ").upper()
                currency2 = input("Enter a currency ID to convert to: ").upper()
                exchange_rate(currency1, currency2)

            elif command == 0:
                print("\tThank For Using Currency Conventer!")
                print("\tExit")
                break
            else:
                print("Wrong Number Input! Choose Only Integer Numbers from 1 to 3 or 0 to Exit")
        else:
            print("Invalid Input! Only Digits Please!")


main()
