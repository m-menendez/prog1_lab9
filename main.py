def encode(s):
    if type(s) is str:
        new_s = ''
        for i in s:
            num = int(i)
            num += 3
            new_s += str(num)
        return new_s

def decode_password(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

