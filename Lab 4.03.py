'''
###########
Lab 4.03
###########

Instructions
In this lab we will be drawing images using nested for loops.

For each of the following problems, you will write a function that will draw the desired output. You may use an extra function if you find it helpful.

1.  Write a function, draw_7, to draw the 7x7 square (shown below)

    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
2.  Write a function stars_and_stripes, that will draw a 3 sets of rows. 1st a row of 7 stars followed by a row of 7 dashes (shown below)

    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
3.  Write a function, increasing_triangle that will print out the following:

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4 5 6
    1 2 3 4 5 6 7

4. Write a function, vertical_stars_and_stripes that will print out the following:

    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -

5.  Use a function to create your own pattern or drawing. Some possible pattern ideas:

    Write a function that will print a border around a 7x7 square (shown below)

        * * * * * * * *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * * * * * * * *
    Write a function that will print the following balanced_triangle.

        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
        1 2 3 4 5 6 7
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    Write a function that will print the following triangle.

        *
        ***
        *****
    
'''
# Write the code for your custom function below:
def draw_seven(y, x):
    for _ in range(y):
        stline = ''
        for _ in range(x):
            stline += ' * '
        print(stline)
draw_seven(7, 7)

def stars_and_stripes(y, x):
    turn = 1
    for _ in range(y):
        stdsline = ''
        if turn > 0:
            for _ in range(x):
                stdsline += ' * '
            turn *= -1
        else:
            for _ in range(x):
                stdsline += ' - '
            turn *= -1
        print(stdsline)

stars_and_stripes(6, 6)

def increasing_triangle(length):
    dist = 1
    for i in range(0, length):
        dist = 1
        for c in range(0, i+1):
            print(dist, end=' ')
            dist += 1
        print("\r")
        
increasing_triangle(7)

def vertical_stars_and_stripes(y, x):
    for _ in range(y):
        turn = 1
        for _ in range(x):
            if turn > 0:
                print('-', end=' ')
                turn *= -1
            else:
                print('*', end=' ')
                turn *= -1
        print("\r")

vertical_stars_and_stripes(7, 7)

def bordered_square(y, x):
    bord_length = x+2
    print('* '*bord_length)
    for _ in range(y):
        print('*', end=' ')
        for _ in range(x):
            print('-', end=' ')
        print('*', end=' ')
        print('\r')
    print('* '*bord_length)
    
bordered_square(7, 7)