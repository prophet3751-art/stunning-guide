def say_love_food(food_list):
    phrases= []
    for food in food_list:
        phrases.append("Do You like" + food +"?")
    return phrases

foods = ["Суп","Каша", "Мясо"]
result =say_love_food
for phrases in result:
    print(phrases)