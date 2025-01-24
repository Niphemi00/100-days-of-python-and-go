from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
drink_details = MenuItem()

expresso = drinks.find_drink("Expresso")

print(expresso)

