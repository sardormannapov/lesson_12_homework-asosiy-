
inp = int(input("enter number please: "))
calc_diff = {
    "skate": 10,
    "painting": 20,

}
result = 0

for value in calc_diff.values():
    result = result + value
    rezultat = result - inp

print(rezultat)
