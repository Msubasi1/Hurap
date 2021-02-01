# Fall 2017 - Starter Code
import sys
from src.FileReading import Hurapread, convertHex
from src.Mission00 import encrypted, key_decryption, decrypted
from src.Mission01 import convertVirus
from src.Mission10 import decrypted_virus, hexofdecrypted, binofdecrypted

'''
This program will save the human race if done properly, 
so please do your best to get 100 from this assignment. 
You can do it! :)
'''
# work as $python hurap.py hurap.txt schuckscii.txt virus_codes.txt

# Opening the input files

hurap_file = open(sys.argv[1], "r")

schuckscii_file = open(sys.argv[2], "r")

virus_codes_file = open(sys.argv[3], "r")

binary_result = []
hex_result = []
encryption_result = []
decryption_result = []
changed = []
key = []
shift_amount = 0

# Mission 00: Decrypting the HuRAP

print("""*********************
     Mission 00 
*********************""", end="\n\n")

print("""--- hex of encrypted code ---
-----------------------------""", end="\n\n")

# Your code which calculates and prints out the hexadecimal representation
# of HuRAP goes here

Hurapread(hurap_file, binary_result)
convertHex(binary_result, hex_result, key)

for line in hex_result:
    print(line)

print("""\n--- encrypted code ----
-----------------------""", end="\n\n")

# Your code which calculates and prints the encrypted character
# representation of HuRAP goes here

encrypted(schuckscii_file, hex_result, encryption_result)

for line in encryption_result:
    print(line)

print("""\n--- decrypted code ---
----------------------""", end="\n\n")

# Your code which decrypts and prints the
# HuRAP goes here

shift_amount = key_decryption(key)
# print(shift_amount)
decrypted(schuckscii_file, shift_amount, encryption_result, decryption_result)
for line in decryption_result:
    print(line)
# Mission 01: Coding the virus

print("""\n*********************
     Mission 01 
*********************""", end="\n\n")

# Your code which transforms the original HuRAP and prints
# the virus-infected HuRAP goes here

for elem in decryption_result:
    changed.append(elem)

convertVirus(virus_codes_file, decryption_result, changed)

for elem in changed:
    print(elem)

# Mission 10: Encrypting the virus-infected HuRAP

print("""\n*********************
     Mission 10 
*********************""", end="\n\n")


print("""--- encrypted code ---
----------------------""", end="\n\n")

# Your code which encrypts and prints the encrypted character
# representation of the virus-infected HuRAP goes here
dec_virus_result = []

decrypted_virus(schuckscii_file, shift_amount, changed, dec_virus_result)

for line in dec_virus_result:
    print(line)

print("""\n--- hex of encrypted code ---
-----------------------------""", end="\n\n")

# Your code which calculates and prints out the hexadecimal representation
# of virus-infected and encrypted HuRAP goes here
hex_virus_result = []
hexofdecrypted(schuckscii_file, dec_virus_result, hex_virus_result)

for line in hex_virus_result:
    print(line)

print("""\n--- bin of encrypted code ---
-----------------------------""", end="\n\n")

# Your code which calculates and prints out the binary representation
# of virus-infected and encrypted HuRAP goes here
bin_virus_result = []
binofdecrypted(hex_virus_result, bin_virus_result)

for line in bin_virus_result:
    print(line)

# Closing the input files

hurap_file.close()
schuckscii_file.close()
virus_codes_file.close()