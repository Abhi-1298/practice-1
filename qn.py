'''Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) for a meal, 
find and print the meal's total cost. Round the result to the nearest integer.
'''

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):

    tip=(tip_percent/100)*meal_cost

    tax=(tax_percent/100)*meal_cost

    total_cost=round(meal_cost+tax+tip)

    print(total_cost)

if __name__ == '__main__':   
    
    meal_cost = float(input('enter meal_cost').strip())

    tip_percent = int(input('enter tip_percent').strip())

    tax_percent = int(input('enter tip_percent').strip())

    solve(meal_cost, tip_percent, tax_percent)
