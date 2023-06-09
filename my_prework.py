# Question 1:
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function.
def hello_name(user_name):
    print("hello_" + user_name + "!\n")

# Question 2:
# Write a python function, first_odds that prints
# the odd numbers from 1-100 and returns nothing
def first_odds():
    for num in range(1,101):
        if num % 2 != 0:
            print(num, end=" ")
    print('\n')


# Question 3:
# Write a python function, max_num_in_list
# to return the max number of a given list.
def max_num_of_list(a_list):
    return max(a_list)

# Question 4:
# Write a function to return if the given year
# is a leap year. A leap year is divisible by 4,
# but not divisble by 100, unless also divisble
# by 400. The return should be Boolean.
def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False

# Question 5:
# Write a function to check to see if all numbers
# in list are consecutive numbers. For example, 
# [2,3,4,5,6,7] are consecutive, but [1,2,4,5] are
# not consecutive numbers. The return should be Boolean.
def is_consecutive(a_list):
    num = a_list[0]
    for consec in a_list:
        if consec == num:
            num += 1
            continue
        else:
            return False
    return True

