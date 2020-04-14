#!!!!For start you must to start 'dep.sh'!!!!!
import colorama
import sys
from colorama import Fore, Back, Style
colorama.init()
import webbrowser
import subprocess
#-------------------------------#
on = True
#-------------------------------#
#-----Settings-code-------------#
#change it if you wnat to open links in w3m(It must be installed)
w3m = False
#-------------------------------#
Red = Fore.RED
Green = Fore.GREEN
#-------------------------------#
#-------------------------------#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def pcheck():
	if "linux" in sys.platform:
		print("Your platform is ok!")
	elif "darwin" in sys.platform:
		print("Your platform is ok!") #all is ok, but i hate Apple
	elif "win" in sys.platform:
		print("Not supported for Windows yet...")
		sys.exit(0)

def settings():
	print("1) Change webbrowser")
	print("2) exit")
	sett = input("<Settings_SePy: >_ ")
	if sett == "1":
		print("Changed to w3m")
		w3m = True
pcheck()
while on == True:
	if w3m == False:
		print(Fore.BLUE + "What do you want to use? ")
		print(Style.RESET_ALL)
		print(Green + "1) Google")
		print("2) Yandex ")
		print("3) Duckduckgo")
		print("4) Custom url")
		print("5) Download site")
		print("7) Parse site")
		print(Style.RESET_ALL)
		print(Fore.YELLOW + "99) settings")
		print(Style.RESET_ALL)
		print(Red + "6) exit")
		print(Style.RESET_ALL)
		browser = input("<SePy: >_ ")
		if browser == "1":
			print("What do you want to search? ")
			search = input("Search: ")
			a = "https://www.google.com/search?source=hp&ei=wLSRXqutAYyGjLsPur-n4As&q=" + search + "&oq=gh&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyAggAMgIIADICCAAyBQgAEIMBMgIIADIGCAAQChABMgIIADICCAAyBQgAEIMBSgsIFxIHMGc4NWc4MEoJCBgSBTBnMWcxUJwNWL8OYMkRaABwAHgAgAFFiAGIAZIBATKYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwirjZzirODoAhUMA2MBHbrfCbwQ4dUDCAY&uact=5"
			webbrowser.open(a)

		if browser == "2" :
			search = input("Search: ")
			a = "https://yandex.com/search/?oprnd=7082962673&text=" + search + "&lr=10502&redircnt=1586608372.1"
			webbrowser.open(a)

		if browser == "3":
			search = input("Search: ")
			a = "https://duckduckgo.com/?q=" + search + "&t=h_&ia=web"
			webbrowser.open(a)

		if browser == "4":
			search = input("<Url: >_ ")
			webbrowser.open("https://" + search)

		if browser == "6":
			break
			exit()

		if browser == "99":
			settings()

		if browser == "5":
			print("What site? ")
			site_d = input("SePy:>_")

			try:
				import requests	
				r = requests.get("https://" + site_d)
				file = open('SePy.html', 'w')
				file.write(r.text)
				file.close()
			except:
				import requests	
				r = requests.get("http://" + site_d)
				file = open('SePy.html', 'w')
				file.write(r.text)
				file.close()

		if browser == "7":
			print("Some error...Try to open 'parse.py' ")
	if w3m == True:
		print("What do you want to use? ")
		print("1) Google")
		print("2) Yandex ")
		print("3) Duckduckgo")
		print("4) Custom url")
		print("5) Download site")
		print("99) settings")
		print("5) exit")
		browser = input("<SePy: >_ ")
		if browser == "1":
			print("What do you want to search? ")
			search = input("Search: ")
			a = "https://www.google.com/search?source=hp&ei=wLSRXqutAYyGjLsPur-n4As&q=" + search + "&oq=gh&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyAggAMgIIADICCAAyBQgAEIMBMgIIADIGCAAQChABMgIIADICCAAyBQgAEIMBSgsIFxIHMGc4NWc4MEoJCBgSBTBnMWcxUJwNWL8OYMkRaABwAHgAgAFFiAGIAZIBATKYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwirjZzirODoAhUMA2MBHbrfCbwQ4dUDCAY&uact=5"
			code = subprocess.call(["w3m", a])

		if browser == "2" :
			search = input("Search: ")
			a = "https://yandex.com/search/?oprnd=7082962673&text=" + search + "&lr=10502&redircnt=1586608372.1"
			code = subprocess.call(["w3m", a])

		if browser == "3":
			search = input("Search: ")
			a = "https://duckduckgo.com/?q=" + search + "&t=h_&ia=web"
			code = subprocess.call(["w3m", a])

		if browser == "4":
			search = input("<Url: >_ ")
			code = subprocess.call(["w3m", search])

		if browser == "5":
			exit()

		if browser == "99":
			settings()

		if browser == "4":
			print("What site? ")
			site_d = input("SePy:>_")

			try:
				import requests	
				r = requests.get("https://" + site_d)
				file = open('SePy.html', 'w')
				file.write(r.text)
				file.close()
			except:
				import requests	
				r = requests.get("http://" + site_d)
				file = open('SePy.html', 'w')
				file.write(r.text)
				file.close()
		