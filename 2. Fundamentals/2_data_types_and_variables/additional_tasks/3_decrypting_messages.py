decrypting_key = int(input())
range_of_messages = int(input())

decryption = ""

for message in range(range_of_messages):
    new_message = input()
    decryption += chr(ord(new_message) + decrypting_key)

print(decryption)
