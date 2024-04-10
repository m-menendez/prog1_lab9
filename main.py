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

def main():
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        menu_input = int(input("Please enter an option: "))
        if menu_input == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif menu_input == 2:
            decoded_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        elif menu_input == 3:
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()

