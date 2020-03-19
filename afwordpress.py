#import module
import requests
import sys

#Ambil url parameter
url = sys.argv[1]

#open file wordlist
arq = open(sys.argv[2], 'r')
lines = arq.readlines()
arq.close

try:
	for line in lines:
		line = line.replace("\n", "")
		request1 = url + "/" +line
		#request url
		http = requests.get(request1)
		#ambil kode status
		code = http.status_code
		#check url respon
		if code != 301 and code != 404:
			if not "page not found" in http.content:
				print("[*] page found : " + request1)
			else:
				print("[-] page not found : " + request1)
		else:
			print("[-] page not found: "+ request1)
except:
	print("Koneksi terpustus!!!!")
	
print("Finish!!!")