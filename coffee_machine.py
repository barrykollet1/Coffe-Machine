class CoffeeMachine:

    def __init__(self):
        self.cash = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9

    def coffee_availibity(self, coffee_type):
        available = False
        if coffee_type == '1':
            if not self.water // 250:
                print("Sorry, not enough water!")
            elif not self.beans // 16:
                print("Sorry, not enough coffee beans!")
            else:
                available = True
        elif coffee_type == '2':
            if not self.water // 350:
                print("Sorry, not enough water!")
            elif not self.milk // 75:
                print("Sorry, not enough milk!")
            elif not self.beans // 20:
                print("Sorry, not enough coffee beans!")
            else:
                available = True
        elif coffee_type == '3':
            if not self.water // 200:
                print("Sorry, not enough water!")
            elif not self.milk // 100:
                print("Sorry, not enough milk!")
            elif not self.beans // 12:
                print("Sorry, not enough coffee beans!")
            else:
                available = True

        return available

    def buy(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

        if coffee_type == 'back':
            # machine_transaction()
            pass
        elif self.coffee_availibity(coffee_type):
            if coffee_type == '1':
                self.water -= 250
                self.beans -= 16
                self.cash += 4

            elif coffee_type == '2':
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cash += 7

            elif coffee_type == '3':
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cash += 6
            print("I have enough resources, making you a coffee!")
            self.cups -= 1

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print(f"I gave you ${self.cash}")
        self.cash = 0

    def machine_state(self):
        print("The coffee machine has: \n{} of water \n{} of milk \n{} of coffee beans \n{} of disposable cups \n${} of cash\n".format(self.water, self.milk, self.beans, self.cups, self.cash))

    def machine_transaction(self):
        action = input("Write action (buy, fill, take, remaining, exit): ")
        while action != 'exit':
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.machine_state()
            action = input("Write action (buy, fill, take, remaining, exit): ")


my_coffee_machine = CoffeeMachine()
my_coffee_machine.machine_transaction()
