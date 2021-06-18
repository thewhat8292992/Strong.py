from colorama import Fore, Back, Style
import json
import nmap3
import requests
import os
import argparse
import random 




print(Fore.RED + """
                                                                                          
                                                                                          
              ___                                                                         
            ,--.'|_                                                  ,-.----.             
            |  | :,'   __  ,-.   ,---.        ,---,                  \    /  \            
  .--.--.   :  : ' : ,' ,'/ /|  '   ,'\   ,-+-. /  |  ,----._,.      |   :    |           
 /  /    '.;__,'  /  '  | |' | /   /   | ,--.'|'   | /   /  ' /      |   | .\ :     .--,  
|  :  /`./|  |   |   |  |   ,'.   ; ,. :|   |  ,"' ||   :     |      .   : |: |   /_ ./|  
|  :  ;_  :__,'| :   '  :  /  '   | |: :|   | /  | ||   | .\  .      |   |  \ :, ' , ' :  
 \  \    `. '  : |__ |  | '   '   | .; :|   | |  | |.   ; ';  |      |   : .  /___/ \: |  
  `----.   \|  | '.'|;  : |   |   :    ||   | |  |/ '   .   . |      :     |`-'.  \  ' |  
 /  /`--'  /;  :    ;|  , ;    \   \  / |   | |--'   `---`-'| | ___  :   : :    \  ;   :  
'--'.     / |  ,   /  ---'      `----'  |   |/       .'__/\_: |/  .\ |   | :     \  \  ;  
  `--'---'   ---`-'                     '---'        |   :    :\  ; |`---'.|      :  \  \ 
                                                      \   \  /  `--"   `---`       \  ' ; 
                                                       `--`-'                       `--`  
""")


ip = input("enter private ip:")
url = input("enter target url:")
path = input("enter  admin panel file.:")


nmap = nmap3.Nmap()
ports = nmap.scan_top_ports(url)
os = nmap.nmap_os_detection(url)
sub = nmap.nmap_subnet_scan(url)





you = nmap3.NmapScanTechniques()
fin = you.nmap_fin_scan(ip)
idle =  you.nmap_idle_scan(ip)
ping = you.nmap_ping_scan(ip)
tcp = you.nmap_tcp_scan(ip)
udp = you.nmap_udp_scan(ip)



with open('tcp.json', 'w', encoding='utf-8') as tc:
    json.dump(tcp , tc, ensure_ascii=False, indent=4)


with open('fin.json', 'w', encoding='utf-8') as pi:
    json.dump(fin , pi, ensure_ascii=False, indent=4)
    

with open('os.json', 'w', encoding='utf-8') as k:
    json.dump(os , k, ensure_ascii=False, indent=4)    

with open('udp.json', 'w', encoding='utf-8') as f:
    json.dump(udp , f, ensure_ascii=False, indent=4)        
    

with open('tcp.json', 'w', encoding='utf-8') as h:
    json.dump(tcp , h, ensure_ascii=False, indent=4)    
            
with open('idlescan.json', 'w', encoding='utf-8') as c:
    json.dump(idle , c, ensure_ascii=False, indent=4)            
    

    
with open('ports.json', 'w', encoding='utf-8') as ci:
    json.dump(ports, ci, ensure_ascii=False, indent=4)                        
    
    
with open('sub.json', 'w', encoding='utf-8') as cli:
    json.dump(sub, cli, ensure_ascii=False, indent=4)                         
    
    
q = requests.get("https://dns.google/resolve?name="+url+"&type=A")
r = q.json()    


with open('ip.json', 'w', encoding='utf-8') as clpi:
    json.dump(r, clpi, ensure_ascii=False, indent=4)                         
    
qee = "http://"
while True:
	lines = open(path).read().splitlines()
	admin =random.choice(lines)
	time.sleep(5)
	r = requests.get(qee + url  + admin)
	b = r.status_code
	if b == 404:
			print(Fore.RED + url + admin,"is an invaild panel")
			if b == 200:
				print(Fore.GREEN + url + admin,"is a vaild panel")


    
