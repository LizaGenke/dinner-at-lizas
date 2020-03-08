import random
from dal_models import *  
import database_service


meals_list = []
current_meal_name = None

f_meals = open('meals.txt', 'r')
for line in f_meals:
    if ':' in line:
        if current_meal_name != None:
            meals_list.append(Meal(current_meal_name, current_meal_contents))
            current_meal_name = None
            current_meal_contents = []

        current_meal_name = line.replace(':','').strip()
        current_meal_contents = []

    if '|' in line:
        ingredient_quantity_list = line.split('|')
        current_metric = None
        if (len(ingredient_quantity_list)>2):
            current_metric=ingredient_quantity_list[2].strip()

        current_meal_contents.append((Ingredient(ingredient_quantity_list[0].strip()), Quantity(ingredient_quantity_list[1].strip() ,current_metric)))

meals_list.append(Meal(current_meal_name, current_meal_contents))

random.shuffle(meals_list)

for meal in meals_list[:7]:
    print(meal.describe())
