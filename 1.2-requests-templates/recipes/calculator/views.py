from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def dish_view(request, dish):
    template_name = 'calculator/index.html'
    ingredients_list = DATA[dish].items()
    servings = int(request.GET.get("servings", 1))

    for _, amount in ingredients_list:
        amount *= servings

    ingredients_dict = {}
    for key, value in ingredients_list:
        ingredients_dict[key] = servings * value
    context = {"recipe": ingredients_dict}

    return render(request, template_name, context)