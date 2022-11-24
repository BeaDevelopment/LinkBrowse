import requests
import time
import cloudscraper
import re
from base64 import b64decode
from urllib.parse import unquote
import os

def cls():
  if os.name=="nt":
    os.system("cls")
  else:
    os.system('clear')

def decrypt_url(code):
    a, b = '', ''
    for i in range(0, len(code)):
        if i % 2 == 0: a += code[i]
        else: b = code[i] + b
    key = list(a + b)
    i = 0
    while i < len(key):
        if key[i].isdigit():
            for j in range(i+1,len(key)):
                if key[j].isdigit():
                    u = int(key[i]) ^ int(key[j])
                    if u < 10: key[i] = str(u)
                    i = j					
                    break
        i+=1
    key = ''.join(key)
    decrypted = b64decode(key)[16:-16]
    return decrypted.decode('utf-8')

# ==========================================

def adfly(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    res = client.get(url).text
    out = {'error': False, 'src_url': url}
    try:
        ysmm = re.findall("ysmm\s+=\s+['|\"](.*?)['|\"]", res)[0]
    except:
        out['error'] = True
        return out
    url = decrypt_url(ysmm)
    if re.search(r'go\.php\?u\=', url):
        url = b64decode(re.sub(r'(.*?)u=', '', url)).decode()
    elif '&dest=' in url:
        url = unquote(re.sub(r'(.*?)dest=', '', url))
    out['bypassed_url'] = url
    return out

# ==========================================
# ==========================================

def menu():
  cls()
  print("Welcome to Bypasser. Please choose an option:")
  print("= 1) LinkVertise =")
  print("= 2) Adf.ly =")
  choice = input(">> ")

  if choice == "1":
    time.sleep(1)
    linkVertise()
  if choice == "2":
    time.sleep(1)
    ad()


def linkVertise():
  cls()
  link = "https://bypass.pm/bypass2?url="

  linkVertise = input("Please enter the LinkVertise link: ")
  print("\nDecoding link...\n")
  req = requests.get(link + linkVertise).json()
  try:
    print("Link: " + req["destination"])
  except KeyError:
    print("\nApologies, There was a error regarding your request, Please try again later.")
    time.sleep(2)
    menu()
  else:
      pass
  time.sleep(1)
  print("Thank you for choosing our services.")
  time.sleep(1)
  menu()

def ad():
  cls()
  ba = input("Please enter the AdFly link: ")
  print("\nDecoding link...\n")
  try:
    b = adfly(ba)
  except requests.exceptions.MissingSchema:
    print("Apologies, There was a error regarding your request, Please try again later.")
    time.sleep(2)
    menu()
  else:
      pass
  print("Link: " + b["bypassed_url"])
  time.sleep(2)
  print("Thank you for choosing our services.")
  time.sleep(2)
  menu()


menu()



