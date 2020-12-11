# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a 
# single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    odds = 0
    evens = 0
    answer = []
    for num in integers:
        if num % 2 != 0:
            odds += 1
        elif num % 2 == 0:
            evens +=1
    if odds > evens:
        answer = [num for num in integers if num % 2 == 0]
    elif evens > odds:
        answer = [num for num in integers if num % 2 != 0]
    return answer[0]

# print(find_outlier([2, 4, 6, 8, 10, 3]))
# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))