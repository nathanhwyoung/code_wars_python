def disemvowel(string):
    return ''.join([char for char in string if char not in 'aeiouAEIOU'])