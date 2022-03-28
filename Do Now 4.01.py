'''
Do Now 4.01

1. In your console
Type the following Code
    single_fruit = ['apple', 'banana', 'watermelon', 'grape']
    multi_fruit = []
    multi_fruit.append(single_fruit[0] + 's')
    multi_fruit.append(single_fruit[1] + 's')
    multi_fruit.append(single_fruit[2] + 's')
    multi_fruit.append(single_fruit[3] + 's')
    print(multi_fruit)

In your notebook
Respond to the following

Briefly write down what happened. What would happen if you added 100 items to the list single_fruit? - It made all the fruits listed plural. Nothing would happen
if you added 100 items to single fruit

Write down how you would update multi_fruit.
you would have to keep appending and then adding the s, or write a basic algorithm to do everything

2. In your console
Type the following
    list_of_numbers = [3, 5, 10, 23]
    for num in list_of_numbers:
        print(f"num is " + {num})
        
Continue in your notebook
Respond to the following
Briefly write down what happened. How would this change if you added 100 items to list_of_numbers? - It gave an error because you had the braces outside of the parenthesis

3. In your console
Rewrite the code from part 1 using knowledge from part 2.
'''

single_fruit = ['apple', 'banana', 'watermelon', 'grape']
multi_fruit = []
for fruit in single_fruit:
    multi_fruit.append(fruit + 's')