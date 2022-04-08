'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])
​
    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program

//its going to say list index out of range

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program

//every 6 and 1 they repeat

3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''

def print_numbers(list):
        for i in range(len(list)):
            print(list[i])

num_list = [1, 2, 3, 4, 5, 6]


def swapping_stars():
    line_str = ""
    for i in range(0, 6):
        turn = True
        for c in range(0,6):
            if turn:
                line_str+="*"
                turn = False
            else:
                line_str+="-"
                turn = True
    print(line_str)

while True:
    choice = input("would you like to: print numbers or swap stars?- ")
    if choice == 'print numbers':
        print_numbers(num_list)
    elif choice == 'swap stars':
        swapping_stars()
    else:
        print("not a choice, sadly")
