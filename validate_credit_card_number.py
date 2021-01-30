# In this Kata, you will implement the Luhn Algorithm, which is used to help validate credit card numbers.
# Given a positive integer of up to 16 digits, return true if it is a valid credit card number, and false if it is not.

# Here is the algorithm:
# Double every other digit, scanning from right to left, starting from the second digit (from the right).
# Another way to think about it is: if there are an even number of digits, double every other digit starting with the first; 
# if there are an odd number of digits, double every other digit starting with the second:

# If a resulting number is greater than 9, replace it with the sum of its own digits (which is the same as subtracting 9 from it):

# Sum all of the final digits:

# Finally, take that sum and divide it by 10. If the remainder equals zero, the original credit card number is valid.

def validate(n):
    num_list = [int(x) for x in str(n)]
    if len(num_list) % 2 == 0:
        # print("even")
        i = 0
    elif len(num_list) % 2 == 1:
        # print("odd")
        i = 1
    doubled_list = []
    for num in num_list:
        if i % 2 == 0:
            num = num*2
        if num > 9:
            num = num - 9
        doubled_list.append(num)
        i+=1
    summed_list = sum(doubled_list)
    # print(doubled_list)
    if summed_list % 10 == 0:
        return True
    return False

print(validate(123))
print(validate(1))
print(validate(2121))
print(validate(1230))
