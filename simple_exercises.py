# Write your average function here:
def average(num1, num2):
    return (num1 + num2) / 2


# Uncomment these function calls to test your average function:
# print(average(1, 100))
# The average of 1 and 100 is 50.5
# print(average(1, -1))
# The average of 1 and -1 is 0

####################

# Write your tenth_power function here:
def tenth_power(num):
    return num**10

# Uncomment these function calls to test your tenth_power function:
# print(tenth_power(1))
# 1 to the 10th power is 1
# print(tenth_power(0))
# 0 to the 10th power is 0
# print(tenth_power(2))
# 2 to the 10th power is 1024

####################

# Write your introduction function here:


def introduction(first_name, last_name):
    return last_name + ', ' + first_name + ' ' + last_name
# Uncomment these function calls to test your introduction function:
# print(introduction("James", "Bond"))
# should print Bond, James Bond
# print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

####################

# Write your square_root function here:


def square_root(num):
    return num**0.5
# Uncomment these function calls to test your square_root function:
# print(square_root(16))
# should print 4
# print(square_root(100))
# should print 10

####################

# Write your tip function here:


def tip(total, percentage):
    return percentage / 100 * total
# Uncomment these function calls to test your tip function:
# print(tip(10, 25))
# should print 2.5
# print(tip(0, 100))
# should print 0.0

####################

# Write your win_percentage function here:


def win_percentage(wins, losses):
    return wins / (wins + losses) * 100
# Uncomment these function calls to test your win_percentage function:
# print(win_percentage(5, 5))
# should print 50
# print(win_percentage(10, 0))
# should print 100

####################

# Write your first_three_multiples function here:


def first_three_multiples(num):
    print(num, num*2, num*3)
    return num*3
# Uncomment these function calls to test your first_three_multiples function:
# first_three_multiples(10)
# should print 10, 20, 30, and return 30
# first_three_multiples(0)
# should print 0, 0, 0, and return 0

####################

# Write your dog_years function here:


def dog_years(name, age):
    return name + ", you are " + str(age*7) + " years old in dog years"
# Uncomment these function calls to test your dog_years function:
# print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
# print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

####################

# Write your remainder function here:


def remainder(num1, num2):
    return (num1*2) % (num2/2)
# Uncomment these function calls to test your remainder function:
# print(remainder(15, 14))
# should print 2
# print(remainder(9, 6))
# should print 0

####################

# Write your lots_of_math function here:


def lots_of_math(a, b, c, d):
    sum = a+b
    dif = c-d
    print(sum)
    print((dif))
    print(sum*dif)
    return sum*dif % a
# Uncomment these function calls to test your lots_of_math function:
# print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
# print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

####################

# Write your in_range function here:


def in_range(num, lower, upper):
    if upper >= num >= lower:
        return True
    else:
        return False

# Uncomment these function calls to test your in_range function:
# print(in_range(10, 10, 10))
# should print True
# print(in_range(5, 10, 20))
# should print False

####################

# Create a function named movie_review() that has one parameter named rating.
# If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"

# Write your movie_review function here:


def movie_review(rating):
    if rating <= 5:
        return 'Avoid at all costs!'
    elif 5 < rating < 9:
        return 'This one was fun.'
    else:
        return 'Outstanding!'

# Uncomment these function calls to test your movie_review function:
# print(movie_review(9))
# should print "Outstanding!"
# print(movie_review(4))
# should print "Avoid at all costs!"
# print(movie_review(6))
# should print "This one was fun."

####################

# Write your twice_as_large function here:


def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False
# Uncomment these function calls to test your twice_as_large function:
# print(twice_as_large(10, 5))
# should print False
# print(twice_as_large(11, 5))
# should print True

####################

# Write your large_power function here:


def large_power(base, exponent):
    pow = True if base**exponent > 5000 else False
    return pow


# Uncomment these function calls to test your large_power function:
# print(large_power(2, 13))
# should print True
# print(large_power(2, 12))
# should print False

####################

# Write your divisible_by_ten function here:
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

# Uncomment these function calls to test your divisible_by_ten function:
# print(divisible_by_ten(20))
# should print True
# print(divisible_by_ten(25))
# should print False

####################

# Write your max_num function here:


def max_num(num1, num2, num3):
    if num1 < num2 or num1 < num3:
        if num2 > num3:
            return num2
        elif num2 == num3:
            return 'It\'s a tie!'
        else:
            return num3
    elif num1 > num2 and num1 > num3:
        return num1
    else:
        return 'It\'s a tie!'

# Uncomment these function calls to test your max_num function:
# print(max_num(-10, 0, 10))
# should print 10
# print(max_num(-10, 5, -30))
# should print 5
# print(max_num(-5, -10, -10))
# should print -5
# print(max_num(2, 3, 3))
# should print "It's a tie!"

####################

# Write your always_false function here:


def always_false(num):
    if num == num:
        return False

# Uncomment these function calls to test your always_false function:
# print(always_false(-1))
# should print False

####################

# Write your same_name function here:


def same_name(your_name, my_name):
    if str(your_name) == str(my_name):
        return True
    else:
        return False


# Uncomment these function calls to test your same_name function:
# print(same_name("Colby", "Colby"))
# should print True
# print(same_name("Tina", "Amber"))
# should print False

####################


####################


####################
