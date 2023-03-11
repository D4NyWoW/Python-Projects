from main import Shoe

low = Shoe('Reebook F1', 150)
medium = Shoe('Air Force 1', 120)
high = Shoe('Off Whites', 400)

try:
    shoe_budget = float(input('What is your shoe budget? '))
except ValueError:
    exit('Please enter a number.')

for shoes in [low, medium, high]:
    shoes.buy(shoe_budget)