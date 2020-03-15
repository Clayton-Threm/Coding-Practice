#Project Euler Question 59
#XOR decryption

import itertools
cipher_file = open(r"C:\Users\Clayton\Documents\Python Other Files\p059_cipher.txt")
content = cipher_file.read()
content = content.split(",")

cipher_list = list(itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3))
ascii_value_list = {i for i in range(32, 94)}
more_values = {i for i in range(97, 123)}
ascii_value_list.update(more_values)


for cipher in cipher_list:
    new_code = []
    index = 0
    for bit in content:
        new_bit = (int(bit) ^ ord(cipher[index]))
        if new_bit not in ascii_value_list:
            break
        new_code.append(chr(new_bit))
        index += 1
        if index > 2:
            index = 0
    else:
        sum_code = sum(ord(i) for i in new_code)
        pass

print (sum_code)

cipher_file.close()