import os
import sys
import json
import time
import string
import argparse
import random
from tqdm import tqdm 


namesfile = 'names.json'
combos = []

def clearvars():
	name = None
	name_extra = None 
	email_domain = None 
	email = None 


def writefile():
	with open('Email_list.txt','ab') as file:
		file.writelines(combos)
		file.close()
		del combos[:]

def mailgen():
	for _ in tqdm(range(100),unit='Emails'):
		name = random.choice(names).lower() + random.choice(surnames).lower()
		name_extra = ''.join(random.choice(string.digits) for _ in range(random.randint(1,4)))
		email_domain = email_domains+'.'+ domain_end
		email = name + name_extra + '@' + email_domain 
		combo = ('{0}'.format(email)).encode()
		combo = combo + '\n'.encode()
		combos.append(combo)
		clearvars()
	writefile()

if __name__ =='__main__':
	if os.name in ['nt','win32','dos']:
		os.system('cls')
	else:
		os.system('clear')
	msg00 ="\n\t\t\033[92m##### EMAIL GENERATOR #####\n\t\t\033[0;96m######### LETS GO!!! ##########\033[92m\n\t\t\033[92m########## EDUCATIONAL PURPOSE ONLY ##########\033[92m\n"
	for i in msg00:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.02)

	try:
		num_lines = sum(1 for i in open(namesfile))
		print('\nGot {} Names!\n'.format(num_lines))
		random.seed = (os.urandom(2048))
		email_domains = input('[+] Enter the Email domain you like to generate: >> ')
		domain_end  = input('[+] Enter the Domain End name (com/edu/org/...): >> ')
		names = json.loads(open(namesfile,encoding='utf-8').read())
		surnames = json.loads(open(namesfile,encoding='utf-8').read())
	except FileNotFoundError:
		print('\n[+] You are missing names.json in your Folder\n')
		sys.exit(0)
	except KeyboardInterrupt:
		print('\n [+] Program Interrupted Aborting....\n')
		sys.exit(0)
	print('\n Available modes: Email(email)\n')
	while True:
		mailgen()
