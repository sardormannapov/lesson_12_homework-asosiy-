mapping = ["p", "s"]
result = {

}
for alp in mapping:
    a = alp.casefold()
    b = alp.capitalize()
    result[a] = b
print(result)
