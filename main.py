def encode(s):
    if type(s) is str:
        new_s = ''
        for i in s:
            num = int(i)
            num += 3
            new_s += str(num)
        return new_s


x = encode("12345555")
print(x)
