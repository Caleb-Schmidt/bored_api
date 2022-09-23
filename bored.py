import requests
from colorama import Fore, Style, init

class Bored():
    def __init__(self):
        self.activity = ""
        self.price = None
        self.type = ""
        self.participants = ""
    
    def get_activity(self):
        minprice = input("What's your minimum price range? 0 - 1: ")
        maxprice = input("What's your maximum price range? 0 - 1: ")
        url = f"http://www.boredapi.com/api/activity?minprice={minprice}&maxprice={maxprice}"
        response = requests.get(url)
        data = response.json()
        if not response.ok:
            return False
        else:
            self.activity = data["activity"]
            self.price = data["price"]
            self.type = data["type"]
            self.participants = data["participants"]
            return True

    def get_info(self):
        print(Fore.BLUE, end='')
        print(self.activity)
        print(Fore.GREEN, end='')
        print(self.price)
        print(Fore.RED, end='')
        print(self.type)
        print(Fore.YELLOW, end='')
        print(self.participants)
        print(Style.RESET_ALL)

    def program(self):
        bored = Bored()
        while True:
            print(bored.get_activity())
            bored.get_info()
            anymore = input("Would you like to find another activity? Y/Quit")
            if anymore[0].lower() == "q":
                print("Have a good day!")
                break

bored = Bored()
bored.program()