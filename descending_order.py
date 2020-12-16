# Your task is to make a function that can take any non-negative integer as an 
# argument and return it with its digits in descending order. Essentially, 
# rearrange the digits to create the highest possible number.

def descending_order(num):
    stringnum = [int(x) for x in str(num)]
    stringnum.sort(reverse=True)
    result = ''.join(str(e) for e in stringnum)
    return int(result)