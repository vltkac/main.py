class Recipe:
    def __init__(self, name: str, ingredients: list, text: str, time: int):
        self.name = name
        self.ingredients = ingredients
        self.text = text
        self.time = time

    def __str__(self):
        return self.name

    def __contains__(self, item):
        return item in self.ingredients

    def __gt__(self, other):
        if isinstance(other, Recipe):
            return self.time > other.time
        else:
            raise TypeError('Please use Recipe object')

    def display_info(self):
        return f'Dish - {self.name}, ingredients: {". ".join(map(lambda ing: ing.lower(), 
        self.ingredients))}, time of preparation - {self.time} minutes, tutorial: {self.text}'


dishes = [
    Recipe(
        "Піца",
        ["борошно", "вода", "дріжджі", "томат", "сир"],
        "Готуємо тісто, додаємо інгредієнти та запікаємо",
        30,
    ),
    Recipe(
        "Салат",
        ["томат", "огірок", "зелень", "олія"],
        "Нарізаємо овочі, додаємо зелень та поливаємо олією",
        10,
    ),
    Recipe(
        "Суп",
        ["вода", "картопля", "морква", "м'ясо"],
        "Варимо всі інгредієнти до готовності",
        45,
    ),
]


def get_dishes_containing(dishes_data: list, target_ingredient='томат'):
    filtered_dishes = list(filter(lambda recipe: target_ingredient in recipe.ingredients, dishes_data))

    return list(map(lambda recipe: recipe.name, filtered_dishes))


print(get_dishes_containing(dishes)) # ['Піца', 'Салат']
print(get_dishes_containing(dishes, 'морква')) # ['Суп']


def get_min_max_prep_time(dishes_data: list, min_or_max='min'):
    if min_or_max == 'min':
        print(f'Minimum preparation time dish\n{min(dishes_data).display_info()}')
    elif min_or_max == 'max':
        print(f'Maximum preparation time dish\n{max(dishes_data).display_info()}')
    else:
        raise ValueError('Invalid parameter. Please use \'min\' or \'max\'')


get_min_max_prep_time(dishes)
get_min_max_prep_time(dishes, 'max')


