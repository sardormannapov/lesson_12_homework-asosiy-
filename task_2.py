#Создайте функцию, которая принимает список словарей и возвращает сумму бюджетов людей.

get_budgets = [
  { "name": "John", "age": "21", "budget": 23000 },
  { "name": "Steve",  "age": "32", "budget": 40000 },
  { "name": "Martin",  "age": "16", "budget": 2700 }
]
result = 0

def find_budget(list, list2):
    for x in list:
        for value in x.values():
            if type(value) == int:
                list2 += value
    print(list2)


find_budget(list=get_budgets, list2=result)


# second way
get_budgets = [
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]
result = 0

def budget(lst, lst2):
    for x in lst:
        lst2 += x["budget"]
    print(lst2)


budget(lst=get_budgets, lst2=result)
