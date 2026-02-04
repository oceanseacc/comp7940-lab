# Write a program to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

# your code here
def print_factor(x):
    # your code here
    for i in range(2, x):
        if x % i == 0:
            print(i)



for i in l:
    print_factor(i)
    print("-" * 10)
