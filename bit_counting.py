def countBits(n):
    bits = bin(n)
    bits = str(bits[2:])
    ones = bits.count("1")
    return ones