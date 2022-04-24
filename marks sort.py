input_marks = input('enters marks of students = ')
print("\n")
#making list of marks
marks_list = input_marks.split()

#converting each item to int type
for i in range(len(marks_list)):
    marks_list[i] = int(marks_list[i])

marks_list.sort()
print(marks_list)