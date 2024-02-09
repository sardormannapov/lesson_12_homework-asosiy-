maximum_score = [
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]
result = 0

def score(lst, lst2):
  for num in lst:
    for value in num.values():
      if type(value) == int:
        lst2 += value
  print(lst2)


score(lst=maximum_score, lst2=result)