def get_valid_mark(prompt):
    while True:
        try:
            mark = float(input(prompt))
            if mark > 100:
                print("Mark cannot be greater than 100. Please re-enter.")
            else:
                return mark
        except ValueError:
            print("Invalid input. Please enter a number.")

first = get_valid_mark("Enter 1st interim mark: ")
firstx = first * 0.05
mid = get_valid_mark("Enter Mid Term mark: ")
midx = mid * 0.25
sec = get_valid_mark("Enter 2nd interim mark: ")
secx = sec * 0.05
fin = get_valid_mark("Enter Final Exam mark: ")
finx = fin * 0.5

final=firstx+midx+secx+finx+15
print("Your final mark is :", final)
if final >= 80:
    print("Your grade is A+")
if 75 <=final<= 79.99:
    print("Your grade is A")
if 70 <=final<= 74.99:
    print("Your grade is A-")
if 65 <=final<= 69.99:
    print("Your grade is B+")
if 60 <=final<= 64.99:
    print("Your grade is B")
elif 60>final:
    print("Fail")
