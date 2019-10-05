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

egg = Ingredient('egg')
bellpepper = Ingredient('bellpepper')

q_eggs = Quantity(2, 'gr')
q_bellpepper = Quantity(1)

wonderful_Berwout_breakfast = Meal('wonderful Berwout breakfast',[(egg,q_eggs),(bellpepper,q_bellpepper)])
print(wonderful_Berwout_breakfast.describe())