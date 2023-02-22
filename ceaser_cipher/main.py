from art import logo

print(logo)


def caesar(start_text, shift_amount, direction_t):
    cipher_text = ""
    if direction_t == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's the {direction}d result: {cipher_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    caesar(start_text=text, shift_amount=shift, direction_t=direction)

    return_statement = input("type 'yes' if you would love to continue and 'no' if you want to stop :\n")

    if return_statement == "no":
        should_continue = False
        print("yea cool catch up later friend")
