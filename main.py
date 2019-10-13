class Ingredient:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name

class Meal:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def describe(self):
        description = self.name + ':\n'
        for ingredient_quantity in self.contents:
            description += ingredient_quantity[1].describe() + ' '
            description += ingredient_quantity[0].describe() + '\n'
        return description

class Quantity:
    def __init__(self, amount, metric=None):
        self.amount = amount
        self.metric = metric

    def describe(self):
        description = str(self.amount)
        if (self.metric != None):
            description += ' ' + self.metric
        return description

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

for meal in meals_list:
    print(meal.describe())