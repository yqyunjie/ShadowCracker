#!/usr/bin/env python

import string
import passlib
import time
import sys
from passlib.hash import sha512_crypt
from itertools import product
from time import sleep

chars_choice = None
chars_options = True
while chars_options:
	print("""
	1. Use lowercase letters 'abcdefghijklmnopqrstuvwxyz'.
	2. Use uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
	3. Use numbers '0123456789'.
	4. Use hexdigits '0123456789abcdefABCDEF'.
	5. Use octal numeral digits '01234567'.
	6. String of ASCII characters which are considered punctuation characters in the C locale.
	7. Concatenation of 1 and 2.
	8. This is a combination of 3, 6, 7, and spaces. 
	""")
	chars_options = raw_input('What characters do you want to use ? ')
	if chars_options == '1':
		chars_choice = string.ascii_lowercase
		print ('\nYou choose lowercase letters\n')
		break
	elif chars_options == '2':
		chars_choice = string.ascii_uppercase
		print ('\nYou choose uppercase letters\n')
		break
	elif chars_options == '3':
		chars_choice = string.digits
		print ('\nYou choose numbers\n')
		break
	elif chars_options == '4':
		chars_choice = string.hexdigits
		print ('\nYou choose hexdigits\n')
		break
	elif chars_options == '5':
		chars_choice = string.octdigits
		print ('\nYou choose Octal\n')
		break
	elif chars_options == '6':
		chars_choice = string.punctuation
		print ('\nYou choose punctuation string\n')
		break
	elif chars_options == '7':
		chars_choice = string.ascii_letters
		print ('\nYou choose mix of 1 and 2\n')
		break
	elif chars_options == '8':
		chars_choice = string.printable
		print ('\nYou choose all possible characters\n')
		break
	else:
		print('\nNot Valid Choice Try Again\n')

chars = chars_choice

length_question = raw_input("Number of characters for permutations: ")

length = int(length_question)

user = raw_input("\nAdd the username (cat /etc/shadow --> username:hash): \n")

hash = raw_input("\nPaste FULL HASH here from /etc/shadow (user:FULL HASH:xxxxx:x:xxxxx:x:::): \n")

password = (''.join(item) for item in product(*[chars], repeat=length))

for password in password:
	result = sha512_crypt.verify(str(password), hash)
	if result:
		print 'For user', user 
		print 'The password is', password
		quit()
	else:
		print 'Password not found. Tested --> ', password
		