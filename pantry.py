pantry ={
    "tomatoes": 200,
    "garlic": 10,
    "olive oil": 30
}

recipe= {
    "pasta": 500,
    "tomatoes": 400,
    "garlic": 15,
    "basil": 20,
    "olive oil": 30,
    "salt": 5
}

shopping_list = []
shopping_dictionaries = {}

print("==== PANTRY REPORT ====")


for item,qty in recipe.items():
    if item not in pantry:
        print(item, ":", "Missing")
        shopping_list.append(item)         # Adding element in list( not key- value pair but single element)
        shopping_dictionaries[item]= qty  # Adding key- vlaue pair in dictionary
    else:
        if qty > pantry[item]:
            sub = qty - pantry[item]
            print(item, ":", "Need", sub, "gram", "more")
            shopping_list.append(item)         # Adding element in list( not key- value pair but single element)
            shopping_dictionaries[item]= sub       # Adding key- vlaue pair in dictionary
        else:
            print(item,":","Enough ")


print("==== SHOPPING LIST ====")

print(shopping_list)
print(shopping_dictionaries)
