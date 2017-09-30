#!/usr/bin/python3
import sys, requests
##-FUNCTIONS
def exploit(trg,lsd):
	print('[+] Loading wordlist')
	lista = open(''+lsd,'r')
	#full=(lista.read())
	#print(full)
	print('[+] Starting Attack')
	for i in lista:
		try:
			con = requests.get('http://'+ str(trg)+'/'+ str(i))
		except Exception as error:
			print('[-] Failed: ', error)
		if con.status_code == 200:
			print('[+] Hit http://'+ str(trg)+'/'+str(i))
		
##-MAIN
target = sys.argv[1]
listx  = sys.argv[2]

exploit(target,listx)
