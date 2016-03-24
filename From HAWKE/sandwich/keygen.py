import sys
import random


def genkey():
	int_param_1 = random.randint(1000,2000)
	int_param_2 = random.randint(1000,2000)
	int_param_3 = random.randint(1000,10000)

	int_sum = int_param_1+int_param_2
	print "[+]sum of param1+param2:",int_sum
	int_sum = int_sum>>2
	print "[+]sum do sar esi,0x2",int_sum
	int_param_4 = 0x19c5-int_sum



	print "[+]key:%04d-%04d-%04d-%04d"%(int_param_1,int_param_2,int_param_3,int_param_4)

if __name__ == "__main__":
	genkey()
