import requests

import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.GREEN + '''
 /$$   /$$ /$$           /$$                                                   /$$$$$$$$ /$$                 /$$                    
| $$$ | $$|__/          | $$                                                  | $$_____/|__/                | $$                    
| $$$$| $$ /$$  /$$$$$$$| $$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$/$$$$   /$$$$$$ | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$ $$ $$| $$ /$$_____/| $$  /$$/| $$__  $$ |____  $$| $$_  $$_  $$ /$$__  $$| $$$$$   | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$  $$$$| $$| $$      | $$$$$$/ | $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$| $$__/   | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/
| $$\  $$$| $$| $$      | $$_  $$ | $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/| $$      | $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$ \  $$| $$|  $$$$$$$| $$ \  $$| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      
|__/  \__/|__/ \_______/|__/  \__/|__/  |__/ \_______/|__/ |__/ |__/ \_______/|__/      |__/|__/  |__/ \_______/ \_______/|__/      

''')
print('''..........................................................................................coded by https://github.com/restanse

''')
                                                                             
nick = input("enter nickname: ")






def osint(list):
	file = open(list) 


	for line in file:
		name = line.split(' ')[0]
		site = line.split(' ')[1]
		
		
		
		site = site.rstrip("\n")
		url = site + nick
		
		
		
		try:
			r = requests.get(url)
	
			if r.status_code == 200:

				print(Fore.GREEN + "found " + name + ": " + url)
			else:
				print(Fore.RED + name + " not found")
		except:
			print(Fore.YELLOW + "request error for " + name)

	file.close()

print(Fore.WHITE + "social networks and messangers:")
osint("snm.txt")

print(Fore.WHITE + "videohostings:")
osint("vh.txt")

print(Fore.WHITE + "games:")
osint("games.txt")


print(Fore.WHITE + "forums: ")
osint("forums.txt")

print(Fore.WHITE + "money: ")
osint("money.txt")

print(Fore.WHITE + "other sites: ")
osint("other.txt")