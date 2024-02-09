get_student_names = {
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}
result = []
def students(lst1, lst2):
    for value in get_student_names.values():
        print(lst1)
        result.append(value)
        result.sort()
    print(lst2)

students(lst1=get_student_names, lst2=result)


