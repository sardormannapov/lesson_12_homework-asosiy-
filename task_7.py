count_all = "H3llo wor1d"
lst = []
lst2 = []
result = {

}

for x in count_all:
    if x.isalpha():
        lst.append(x)


    elif x.isdigit():
        lst2.append(x)


result["LETTERS"] = len(lst)
result["DIGITS"] = len(lst2)
print(result)





