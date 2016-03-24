import sys
import random
import hashlib

def genkey():
	name = "mrh"
	_name = name+"+unicorn"
	#print "[+]name to md5:",name
	m = hashlib.md5()
	m.update(_name)
	psw = m.hexdigest()
	#print "[+]md5 name:",psw[0:20].upper()

	print "[+]name:",name
	print "[+]serial:",psw[0:20].upper()

if __name__ == "__main__":
	genkey()

