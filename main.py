# Check what kind of GPA to be calculated
type = input("Which GPA would you like to calculate? \n"
      "\t1. Sessional\n"
      "\t2. Cumulative\n").casefold()

while type != "sessional" and type != "cumulative" and \
        type != "1" and type != "2":
    print("Sorry invalid input")
    type = input("Which GPA would you like to calculate? \n"
                 "\t1. Sessional\n"
                 "\t2. Cumulative\n").casefold()

#If type is sessional GPA
if type == "sessional" or type == "1":
# The sessional GPA is calculated as follows:
# 1. Multiply Grade Point X Unit Value for each course = Course Points
# 2. Divide Total Course Points ÷ Total Unit Value = Sessional GPA

    check = False
    while not check:
        try:
            num_of_courses = int(input("For how many courses do you want the GPA of?\n"))
            check = True
        except ValueError:
            print("Sorry Invalid")
            check = False

    total_course_points = 0
    total_unit_value = 0

    for i in range (1, num_of_courses + 1):
        grade_point = 0
        unit_value = 0

        try:
            grade_point = int(input("Enter Grade point for course {}:".format(i)))
            if grade_point > 9:
                raise ValueError
            unit_value = float(input("Enter unit value (number of credits) for course {}:".format(i)))
        except ValueError:
            print("Sorry invalid")
            i -= 1
            continue

        total_unit_value += unit_value
        total_course_points += (grade_point * unit_value)

    sessional_GPA = total_course_points/total_unit_value

    print("Your sessional GPA is {.2}".format(sessional_GPA))