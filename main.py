# Check what kind of GPA to be calculated
type_of_gpa = input("Which GPA would you like to calculate? \n"
                    "\t1. Sessional\n"
                    "\t2. Cumulative\n").casefold()

# If input is invalid keep asking until valid
while type_of_gpa != "sessional" and type_of_gpa != "cumulative" and \
        type_of_gpa != "1" and type_of_gpa != "2":
    print("Sorry invalid input")
    type_of_gpa = input("Which GPA would you like to calculate? \n"
                        "\t1. Sessional\n"
                        "\t2. Cumulative\n").casefold()

# If type is sessional GPA
if type_of_gpa == "sessional" or type_of_gpa == "1":
    # The sessional GPA is calculated as follows:
    # 1. Multiply Grade Point X Unit Value for each course = Course Points
    # 2. Divide Total Course Points ÷ Total Unit Value = Sessional GPA

    # Initialize num of courses
    num_of_courses = 0

    # Get number of courses
    check = False
    while not check:
        try:
            num_of_courses = int(input("For how many courses do you "
                                       "want the GPA of?\n"))
            check = True
        except ValueError:
            print("Sorry Invalid")
            check = False

    # Initialize total_course_points and total_unit_value
    # The reason why they're being initialized up here is because I
    # need to have them as global variables and need to use them
    # outside the loop

    total_course_points = 0
    total_unit_value = 0

    # Loop until program has asked for info for each course
    i = 1
    while i <= num_of_courses:
        grade_point = 0
        unit_value = 0

        try:
            # Get grade point
            grade_point = int(input("Enter Grade point for course"
                                    " {}:".format(i)))

            # If grade point is greater than 9 it is invalid
            if grade_point > 9:
                raise ValueError

            # Get unit value
            unit_value = float(input("Enter unit value "
                                     "(number of credits) for course "
                                     "{}:".format(i)))

            # Only increment i (move on to next course) if input is valid
            i += 1
        except ValueError:
            # If not valid go back to beginning of loop without moving
            # on to next course
            print("Sorry invalid")
            continue

        # Add the current course's unit value to the
        # total unit value count
        total_unit_value += unit_value

        # Add the current course's points to the
        # total course points count
        total_course_points += (grade_point * unit_value)

    # After info from all courses is collected, calculate gpa
    sessional_GPA = total_course_points / total_unit_value

    # Print GPA to 2 decimal places
    print("Your sessional GPA is {:.2f}".format(sessional_GPA))

# If type is Cumulative GPA
else:
    # Cumulative GPA calculation: Total course points ÷ Total units

    # Initialize num of semesters
    num_of_semesters = 0

    # Get number of semesters
    check = False
    while not check:
        try:
            num_of_semesters = int(input("For how many semesters do you"
                                         " want to calculate"
                                         " the GPA of?\n"))
            check = True
        except ValueError:
            print("Sorry Invalid")
            check = False

    # Initialize total_GPA_for_all_sem and
    # total_unit_value _for_all_sem
    # The reason why they're being initialized up here is because I
    # need to have them as global variables and need to use them
    # outside the loop

    total_GPA_for_all_sem = 0
    total_unit_values_for_all_sem = 0

    # Loop until program has asked for info for each semester
    i = 1
    while i <= num_of_semesters:
        sem_gpa = 0
        sem_credits = 0

        try:
            # Get the current semesters GPA
            sem_gpa = float(input("Enter the GPA for semester"
                                  " {}:".format(i)))

            # If GPA is greater than 9 it is invalid
            if sem_gpa > 9.0:
                raise ValueError

            # Get the current semesters total unit values (credits)
            sem_credits = float(input("Enter total credits for semester"
                                      " {}:".format(i)))

            # Only increment i (move on to next semester) if input is valid
            i += 1
        except ValueError:
            # If not valid go back to beginning of loop without moving
            # on to next semester
            print("Sorry invalid")
            continue

        # Add the current semester's total credits to the
        # total credits count
        total_unit_values_for_all_sem += sem_credits

        # Add the current semester's GPA to the
        # total GPA count
        total_GPA_for_all_sem += (sem_gpa * sem_credits)

    # After info from all semesters is collected, calculate gpa
    cumulative_GPA = total_GPA_for_all_sem / total_unit_values_for_all_sem

    # Print GPA to 2 decimal places
    print("Your cumulative GPA is {:.2f}".format(cumulative_GPA))
