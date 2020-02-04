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

# Create a function named double_index that has two parameters, a list named lst and a single number as index.
# The function should return a new list where all elements are the same as in lst except for the element at index, which should be double the value of the element at index of lst.
# If index is not a valid index, the function should return the original list.
# For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:
# double_index([1, 2, 3, 4], 2)

# Write your function here
def double_index(lst, index):
    if index >= len(lst):
        print('not a valid index')
    else:
        # double_index = lst[index]*2
        new_lst = lst[:index]
        new_lst.append(lst[index]*2)
        new_lst += lst[index+1:]
        return new_lst

# Uncomment the line below to test your function
# print(double_index([3, 8, -10, 12], 2))

####################

# Create a function named remove_middle which has three parameters named lst, start, and end.
# The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:
# remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)

# Write your function here


def remove_middle(lst, start, end):
    if start < 0:
        print('start parameter invalid')
    elif end > len(lst):
        print('end parameter invalid')
    else:
        new_lst = lst[:start] + lst[end+1:]
        return new_lst

# Uncomment the line below when your function is done
# print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

####################

# Create a function named more_than_n that has three parameters named lst, item, and n.
# The function should return True if item appears in the list more than n times. The function should return False otherwise.

# Write your function here


def more_than_n(lst, item, n):
    counter = 0
    for i in lst:
        if i == item:
            counter += 1
    if counter > n:
        return True
    else:
        return False

# Uncomment the line below when your function is done
# print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

####################

# Write your function here


def more_frequent_item(lst, item1, item2):
    item1_counter = 0
    item2_counter = 0
    for i in lst:
        if i == item1:
            item1_counter += 1
        elif i == item2:
            item2_counter += 1
        else:
            return 'neither items appear in list'
    if item1_counter >= item2_counter:
        return item1
    else:
        return item2

# Uncomment the line below when your function is done
# print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

####################

# Create a function called middle_element that has one parameter named lst.
# If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

# Write your function here


def middle_element(lst):
    # get index om middle elem
    index = len(lst) / 2
    index = int(index)

    # check if list has odd/even num of elems
    if len(lst) % 2 == 0:
        # return avg of middle elem
        avg = (lst[index - 1] + lst[index]) / 2
        return avg
    else:
        # return middle elem
        return lst[index]


# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

####################

# Write a function named append_sum that has one parameter named lst.
# The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.
# For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

# Write your function here


def append_sum(lst):
    i = 3
    while i > 0:
        lst.append(lst[-1] + lst[-2])
        i -= 1
    return lst

# Uncomment the line below when your function is done
# print(append_sum([1, 1, 2]))

####################

# Write a function named larger_list that has two parameters named lst1 and lst2.
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

# Write your function here


def larger_list(lst1, lst2):
    if len(lst2) > len(lst1):
        return lst2[-1]
    else:
        return lst1[-1]

# Uncomment the line below when your function is done
# print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

####################

# Write a function named combine_sort that has two parameters named lst1 and lst2.
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

# Write your function here


def combine_sort(lst1, lst2):
    new_lst = lst1 + lst2
    return sorted(new_lst)

# Uncomment the line below when your function is done
# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

####################

# Create a function called append_size that has one parameter named lst.
# The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.

# Write your function here


def append_size(lst):
    lst.append(len(lst))
    return lst

# Uncomment the line below when your function is done
# print(append_size([23, 42, 108]))

####################

# Create a function called every_three_nums that has one parameter named start.
# The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.

# Write your function here


def every_three_nums(start):
    return list(range(start, 101, 3))

# Uncomment the line below when your function is done
# print(every_three_nums(91))

####################

# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.

# Write your function here


def divisible_by_ten(nums):
    count = 0
    for i in nums:
        if i % 10 == 0:
            count += 1

    return count

# Uncomment the line below when your function is done
# print(divisible_by_ten([20, 25, 30, 35, 40]))

####################

# Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.

# Write your function here


def add_greetings(names):
    greeting_lst = []
    for name in names:
        greeting_lst.append("Hello, " + name)
    return greeting_lst

# Uncomment the line below when your function is done
# print(add_greetings(["Owen", "Max", "Sophie"]))

####################

# Write a function called delete_starting_evens() that has a parameter named lst.
# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
# Make sure your function works even if every element in the list is even!

# Write your function here


def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst

# Uncomment the lines below when your function is done
# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# print(delete_starting_evens([4, 8, 10]))

####################

# Create a function named odd_indices() that has one parameter named lst.
# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

# Write your function here


def odd_indices(lst):
    new_lst = []
    for i in range(1, len(lst), 2):
        new_lst.append(lst[i])
    return new_lst

# Uncomment the line below when your function is done
# print(odd_indices([4, 3, 7, 10, 11, -2]))

####################

# Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

# Write your function here


def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for exponent in powers:
            new_lst.append(base**exponent)
    return new_lst

# Uncomment the line below when your function is done
# print(exponents([2, 3, 4], [1, 2, 3]))

####################

# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

# Write your function here


def larger_sum(lst1, lst2):
    lst1_sum = lst2_sum = 0
    for i in lst1:
        lst1_sum += i
    for i in lst2:
        lst2_sum += i
    if lst2_sum > lst1_sum:
        return lst2
    else:
        return lst1

# Uncomment the line below when your function is done
# print(larger_sum([1, 9, 5], [2, 3, 7]))

####################

# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

# Write your function here


def over_nine_thousand(lst):
    if lst == []:
        return 0
    lst_sum = 0
    for i in lst:
        lst_sum += i
        if lst_sum > 9000:
            break
    return lst_sum

# Uncomment the line below when your function is done
# print(over_nine_thousand([8000, 900, 120, 5000]))

####################

# Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums

# Write your function here


def max_num(nums):
    nums.sort()
    print('This is a way of doing it: ' + str(nums[-1]))

    max = nums[0]
    for i in nums:
        if i > max:
            max = i
    print('This is another way of doing it: ' + str(max))

# Uncomment the line below when your function is done
# max_num([50, -10, 0, 75, 20])

####################

# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.

# Write your function here


def same_values(lst1, lst2):
    index_lst = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            index_lst.append(i)
    return index_lst

# Uncomment the line below when your function is done
# print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

####################

# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

# Write your function here


def reversed_list(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[len(lst2) - 1 - i]:
            return False

    return True

# Uncomment the lines below when your function is done
# print(reversed_list([1, 2, 3], [3, 2, 1]))
# print(reversed_list([1, 5, 3], [3, 2, 1]))

####################

# Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:


def unique_english_letters(word):
    count = 0
    for letter in letters:
        if letter in word:
            count += 1
    return count
# Uncomment these function calls to test your function:
# print(unique_english_letters("mississippi"))
# should print 4
# print(unique_english_letters("Appleaa"))
# should print 4

####################

# Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.

# Write your count_char_x function here:


def count_char_x(word, x):
    count = 0
    for i in range(len(word)):
        if x in word[i]:
            count += 1
    return count

# Uncomment these function calls to test your tip function:
# print(count_char_x("mississippi", "s"))
# should print 4
# print(count_char_x("mississippi", "m"))
# should print 1

####################

# Write a function named count_multi_char_x that takes a string named word and a string named x. This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple characters long.

# Write your count_multi_char_x function here:


def count_multi_char_x(word, x):
    splits = word.split(x)
    print(splits)
    return(len(splits)-1)

# Uncomment these function calls to test your  function:
# print(count_multi_char_x("mississippi", "iss"))
# should print 2
# print(count_multi_char_x("apple", "pp"))
# should print 1

####################

# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.

# Write your substring_between_letters function here:


def substring_between_letters(word, start, end):
    if start and end in word:
        result = word[word.index(start)+1:word.index(end)]
    else:
        result = word
    return result


# Uncomment these function calls to test your function:
# print(substring_between_letters("apple", "p", "e"))
# should print "pl"
# print(substring_between_letters("apple", "p", "c"))
# should print "apple"

####################

# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.

# Write your x_length_words function here:
def x_length_words(sentance, x):
    sentance_lst = sentance.split()
    for i in range(len(sentance_lst)):
        if len(sentance_lst[i]) < x:
            return False
        else:
            return True


# Uncomment these function calls to test your tip function:
# print(x_length_words("i like apples", 2))
# should print False
# print(x_length_words("he likes apples", 2))
# should print True

####################

# Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. The function should return False otherwise.

# Write your check_for_name function here:
def check_for_name(sentance, name):
    if name.lower() in sentance.lower():
        return True
    else:
        return False

# Uncomment these function calls to test your  function:
# print(check_for_name("My name is Jamie", "Jamie"))
# should print True
# print(check_for_name("My name is jamie", "Jamie"))
# should print True
# print(check_for_name("My name is Samantha", "Jamie"))
# should print False

####################

# Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.

# Write your every_other_letter function here:


def every_other_letter(word):
    other_letters = ''
    if len(word) > 0:
        for i in range(0, len(word), 2):
            other_letters += word[i]
    return other_letters
# Uncomment these function calls to test your function:
# print(every_other_letter("Codecademy"))
# should print Cdcdm
# print(every_other_letter("Hello world!"))
# should print Hlowrd
# print(every_other_letter(""))
# should print

####################

# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

# Write your reverse_string function here:


def reverse_string(word):
    return word[::-1]

# Uncomment these function calls to test your  function:
# print(reverse_string("Codecademy"))
# should print ymedacedoC
# print(reverse_string("Hello world!"))
# should print !dlrow olleH
# print(reverse_string(""))
# should print

####################

# A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”.
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. Return the two new words as a single string separated by a space.

# Write your make_spoonerism function here:


def make_spoonerism(word1, word2):
    new_word1 = word2[0] + word1[1:]
    new_word2 = word1[0] + word2[1:]
    return new_word1 + ' ' + new_word2

# Uncomment these function calls to test your function:
# print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
# print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
# print(make_spoonerism("a", "b"))
# should print b a

####################

# Create a function named add_exclamation that has one parameter named word. This function should add exclamation points to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word.

# Write your add_exclamation function here:


def add_exclamation(word):
    for i in range(20 - len(word)):
        word += '!'
    return word
# Uncomment these function calls to test your function:
# print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
# print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

####################
