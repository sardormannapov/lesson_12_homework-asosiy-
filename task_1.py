#У Люка Скайуокера есть семья и друзья. Помогите ему напомнить им, кто есть кто.
# Учитывая строку с именем, верните отношение этого человека к Люку.

inp = input("Enter name: ")
person = {
    "Darth Vader": "father",
    "Leia": "sister",
    "Han": "brother in law",
    "R2D2": "droid"
}

def luke_family(inpt, lst):
    for people in person.keys():
        if inpt == people:
            print(f"Luke i'm your {lst[people]}")
            break
    else:
        print("Nope")


luke_family(inpt=inp, lst=person)