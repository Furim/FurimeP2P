import os
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import flask, requests, json
import hashlib
import re
from flask import Flask, session, redirect, url_for, escape, request
import fileinput
import linecache as lc
from flask import Flask, request, render_template
from flask import Flask
import tronpy
import base64
import urllib.parse
import random
from tronpy import Tron
from flask import jsonify # <- `jsonify` instead of `json`
from tronpy.keys import PrivateKey
from pathlib import Path
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import SocketIO
import hashlib
from tronpy.keys import PrivateKey
from tronpy import Tron
import time
import smtplib
from email.mime.text import MIMEText
from tronapi import Tron as Tron1
import json
from flask_xcaptcha import XCaptcha
STATIC_DIR = os.path.abspath('static/')

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, static_folder=STATIC_DIR)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1)

### Defining name file as app
### Defining name file as app

### Different system of visiting website
limiter = Limiter(app, key_func=get_remote_address)

xcaptcha = XCaptcha(
    site_key="730d93e5-d1a8-464c-b264-9d17dc88a25a",
    secret_key="0x9Dccd726Ae8AecBdC939A21A6eCE5ad987EEEE0D",
    verify_url="https://hcaptcha.com/siteverify",
    api_url="https://hcaptcha.com/1/api.js",
    div_class="h-captcha"
)


app.secret_key = 'anyrandomstring'
@app.route("/")
def main():
    return render_template("main.html")

def findread(findstr, fileinput):
    content = open(fileinput).readlines()
    lookup = findstr
    lines = [line_num for line_num, line_content in enumerate(content) if lookup in line_content]
    list1 = lines
    str1 = ''.join(str(e) for e in list1)
    if str1 == "":
        return ""
    if str1 != "":
        line_to_read = (int(str1)) + 1
        with open(fileinput, "r") as f:
            lines = f.readlines() 
        line1 = lines[int(str1)]
        gfg = line1.replace("\n", "")
        return str(gfg)

def replace_func(datafind, datareplace, fileinput):
    fin = open(fileinput, "rt")
    data = fin.read()
    data = data.replace(datafind, datareplace)
    fin.close()
    fin = open(fileinput, "wt")
    fin.write(data)
    fin.close()
    return("Data successfully replaced")

def is_hex(s):
    hex_digits = set("0123456789abcdef")
    for char in s:
        if not (char in hex_digits):
            return False
    return True


def removelinefile(datatoremove, fileinput):
    content = open(fileinput).readlines()
    lookup = datatoremove
    lines = [line_num for line_num, line_content in enumerate(content) if lookup in line_content]
    list1 = lines
    str1 = ''.join(str(e) for e in list1)


    a_file = open(fileinput, "r")


    lines = a_file.readlines()

    a_file.close()


    del lines[int(str1)]



    new_file = open(fileinput, "w+")


    for line in lines:

        new_file.write(line)


    new_file.close()


    with open(fileinput) as reader, open(fileinput, 'r+') as writer:
        for line in reader:
            if line.strip():
                writer.write(line)
        writer.truncate()

    with open(fileinput) as f_input:
        data = f_input.read().rstrip('\n')

    with open(fileinput, 'w') as f_output:    
        f_output.write(data)


    with open(fileinput, 'r') as fr:
        lines = fr.readlines()
@app.route("/register", methods=["POST", "GET"])
def register():
   email = request.form["register_email"]
   password = request.form["register_password"]

   str_email = (str(email))
   str_password = (str(password))
   print("register email is:", str_email)
   print("password is:", str_password)
   hcaptcha = request.form.get("h-captcha-response")
   CAPTCHA_SECRET_KEY = "0x9Dccd726Ae8AecBdC939A21A6eCE5ad987EEEE0D"
   print(hcaptcha)
   print(CAPTCHA_SECRET_KEY)
   captcha = request.args.get('captcha', None)
   postdata = {'secret': CAPTCHA_SECRET_KEY,
               'response': hcaptcha}
   captcha_data = requests.post(
            'https://hcaptcha.com/siteverify', data=postdata).json()
   print(captcha_data)
   if not captcha_data["success"]:
         return ("Incorrect captcha")


   if "@" not in str_email:
      return '''Emails usually contain "@" character'''
   else:

      ###send email

      gmail_user = 'furimeservices@gmail.com'
      gmail_password = 'EMAILPASSWORDHERE'
      send_email_to = str_email


      msg_content = '<h2 style="text-align: center;">Thanks for using Furime services </h2></br> <center><img  style="width:120px;height:auto; " src="https://www.pngkey.com/png/detail/378-3789365_post-apu-pepe-thumbs-up.png"></center> <p style="text-align:center">You successfully registered on Furime services using email: {}</p> <p style="text-align: center;">What you should do next: Setup <a style="color:#b73e31">TRX</a> and <a style="color:#885d00">DUCO</a> credentials</p> <h1 style="text-align:center;">Have a nice day 🐠</h1>'.format(str_email)
      message = MIMEText(msg_content, 'html')



      message['From'] = '{}'.format(gmail_user)
      message['To'] = '{}'.format(send_email_to)

      message['Subject'] = '🦥 You successfully registered on Furime Services 🥝'

      msg_full = message.as_string()

      server = smtplib.SMTP('smtp.gmail.com:587')
      server.starttls()
      server.login(gmail_user, gmail_password)
      server.sendmail(gmail_user,
                     [send_email_to , send_email_to ],
                     msg_full)
      server.quit()


      ### already registered on that email:
      f = open("database_users.txt", "r")
      registered_check = f.read() 

      if str_email in registered_check:
         return '''Email already used'''
      ### already registered on that email:
      f = open("database_users.txt", "a")
      f.write("{},{}\n".format(str_email, str_password))
      f.close()
      #email,duco_username,duco_password,trx_private_key,trx_addr

      f = open("database_crypto.txt", "a")
      f.write("{},-,-,-,-\n".format(str_email))
      f.close()

      ##errors that can happend

      ###no @ character



      return '''Registered successfully'''

@app.route("/price")
def read():
   f = open("price.json", "r")
   price_read = json.loads(f.read())
   print(price_read)
   return jsonify(price_read)

@app.route("/user")
def user():
   session['email_var'] = request.args.get("email")

   user_email = request.args.get("email")
   user_password = request.args.get("password")
   print("Email to log in: ", user_email)
   print("Password to use:", user_password)
   filename = "database_crypto.txt"
   content = open("database_crypto.txt").readlines()
   f = open("database_users.txt", "r")
   user_database = f.read() 
   if str(user_email + "," + user_password) not in user_database:
      return '''This user does not exist in database, wrong password or email'''
   ###
   line1 = findread(user_email, "database_crypto.txt")
   line1_splitted = line1.split(",")
   #email,duco_username,duco_password,trx_private_key,trx_addr

   duco_usr = line1_splitted[1]
   duco_pass = line1_splitted[2]
   trx_private_key = line1_splitted[3]
   trx_addr = line1_splitted[4] 

   f = open("offers_sell.txt", "r")
   offers_sell = f.read()
   f.close()
   
   f = open("offers_buy.txt", "r")
   offers_buy = f.read() 
   f.close()
   
   if ((str(duco_pass)) == "-") or (str(trx_private_key) == "-"):
      return render_template("user.html", duco_usr=duco_usr, trx_addr=trx_addr, offers_sell=offers_sell, offers_buy=offers_buy)
   else:
      message = duco_pass
      message_bytes = message.encode('ascii')
      base64_bytes = base64.b64encode(message_bytes)
      base64_message = base64_bytes.decode('ascii')
      query = base64_message
      parse_url_password = urllib.parse.quote(query)
      print(base64_message)

      request_duco = requests.get("https://server.duinocoin.com/v2/auth/{}?password={}".format(duco_usr, parse_url_password)).json()
      checking = request_duco["success"]
      print("Logged in", checking)

      client = Tron()
      str_trx_addr = (str(trx_addr))
      trx_balance = client.get_account_balance(str_trx_addr)

      print("Balance TRX", trx_balance)

      offers_user = findread(user_email, "offers.txt")
      if checking == False:
         return '''Change your password to previous one.'''
      if checking == True:
         return render_template("user.html", duco_usr=duco_usr, trx_addr=trx_addr, offers_sell=offers_sell, offers_buy=offers_buy, trx_balance=trx_balance, offers_user=offers_user)


@app.route("/setup")
def setup():
   email_session_var = session['email_var']
   print(email_session_var)
   return render_template("setup.html")

@app.route("/setup_duco")
def setup_duco():
   email_session_var = session['email_var']
   username_duco = request.args.get("username_duco")
   password_duco = request.args.get("password_duco")
   print(username_duco)
   print(password_duco)

   message = password_duco
   message_bytes = message.encode('ascii')
   base64_bytes = base64.b64encode(message_bytes)
   base64_message = base64_bytes.decode('ascii')
   query = base64_message
   parse_url_password = urllib.parse.quote(query)
   print(base64_message)
   request_duco = requests.get("https://server.duinocoin.com/v2/auth/{}?password={}".format(username_duco, parse_url_password)).json()
   print(request_duco)
   checking = request_duco["success"]
   if checking == False:
      return '''Something went wrong, wrong username or password or both'''
   if checking == True:
      print("True")
      line1 = findread(email_session_var, "database_crypto.txt")
      gfg = line1
      gfg_splitted = gfg.split(",")
      trx_private_key = gfg_splitted[3] #existing one
      trx_addr = gfg_splitted[4]#existing one
      #email,duco_username,duco_password,trx_private_key,trx_addr
      before_replace = "{},{},{},{},{}".format(email_session_var, username_duco, password_duco, trx_private_key, trx_addr)
      replace_func(gfg, before_replace, "database_crypto.txt")
      return '''Done, DUCO has been sucessfully setuped'''


@app.route("/setup_trx")
def setup_trx():
   email_session_var = session['email_var']

   trx_private_key = request.args.get("trx_private_key")
   ###trx addr generating from priv key
   str_trx_private_key = (str(trx_private_key))
   lenght_private_key = len(str_trx_private_key)



   if lenght_private_key < 64:
      return '''Key should have 64 characters'''
   if lenght_private_key > 64:
      return '''Key toooo long should be 64 characters'''
   
   if is_hex(str_trx_private_key) == False:
      return '''invalid format of private key, should be HEX'''

   
   else:

      tron1 = Tron1()
      tron1.private_key = str_trx_private_key
      tron_dict =  (tron1.address.from_private_key(tron1.private_key))
      tronaddress = tron_dict['base58']
      ###trx addr generating from priv key
      gfg = findread(email_session_var, "database_crypto.txt")
      gfg_splitted = gfg.split(",")

      #      #email,duco_username,duco_password,trx_private_key,trx_addr

      duco_username = gfg_splitted[1]
      duco_pass = gfg_splitted[2]

      before_replace = "{},{},{},{},{}".format(email_session_var, duco_username, duco_pass, trx_private_key, tronaddress)


      filename = "database_crypto.txt"

      replace_func(gfg, before_replace, "database_crypto.txt")

      return '''Done, TRX has been sucessfully setuped'''


@app.route("/sell_duco")
def sell_duco():
   return render_template("sell_duco.html")

@app.route("/sell_duco_final")
def sell_duco_final():
   email_session_var = session['email_var']

   trx = request.args.get("trx")
   duco = request.args.get("duco")
   print("trx (price)", trx)
   print("duco (quantity)", duco)
   f = open("offers_buy.txt", "r") #check for simillar offer in buying section
   offers_sell = f.read() 
   print(offers_sell)
   str_duco = (str(duco))
   float_trx = (float(trx))
   offer_fixed = "{},{}".format(duco, trx)
##check for simillar offer







   #check for balance
   f = open("offers.txt", "r")
   offers_all = f.read()
   
   gfg = findread(email_session_var, "database_crypto.txt")

   gfg_splitted = gfg.split(",")
   tron_addr_usr = str(gfg_splitted[4])

   #      #email,duco_username,duco_password,trx_private_key,trx_addr
   client = Tron()

   trx_balance = client.get_account_balance(tron_addr_usr)

   print("TRX balance", trx_balance)
   request_duco = requests.get("https://server.duinocoin.com/balances/{}".format(str(gfg_splitted[1]))).json()
   balance_duco = request_duco["result"]["balance"]
   print("DUCO Balance:", balance_duco)

   if email_session_var in offers_all:
      return '''U made already one offer, remove it or wait''' 
   if (float(balance_duco)) < float(duco):
      return '''Insufficient balance [DUCO]'''

      
   else:
      if offer_fixed in offers_sell:
         gfg33 = findread(offer_fixed, "offers_buy.txt")

         gfg33_splitted = gfg33.split(",")
         hash_found1 = gfg33_splitted[2]
         trx_needed = gfg33_splitted[1]
         
         print(hash_found1)

         ### Check first if user have still funds
         gfg99 = findread(offer_fixed, "offers_buy.txt")
         print("NORMAL OFFERS", gfg99)
         gfg99_splitted = gfg99.split(",")

         email_userhavingoffer = gfg99_splitted[0]

         gfg20 = findread(email_userhavingoffer, "database_crypto.txt")

         
         gfg20_splitted = gfg20.split(",")
         trx_addr_userhavingoffer = str(gfg20_splitted[4])

         duco_usr_userhavingoffer = gfg20_splitted[1]

##
         print("TRX Needed balance", trx_needed)

         float_trx_needed = (float(trx_needed))

         client = Tron()
         trx_balance = client.get_account_balance(trx_addr_userhavingoffer)
         print(trx_balance)
         float_trx_balance = (float(trx_balance))
         if float_trx_balance < float_trx_needed:
            print("(TRX) dont have funds so i will remove offer")


            removelinefile(hash_found1, "offers_buy.txt")

            ###
            removelinefile(hash_found1, "offers.txt")
          
            to_hash = "{},{},{}".format(trx, duco, email_session_var)
            to_hash_encoded = to_hash.encode("utf-8")
            hash_of_the_offer = hashlib.sha224(to_hash_encoded).hexdigest()
            print (hash_of_the_offer)
            f = open("offers_sell.txt", "a")
            f.write("\n{},{},{}".format(duco, trx, hash_of_the_offer))
            f.close()
            f = open("offers.txt", "a")
            f.write("\n{},{},{},{}".format(email_session_var, duco, trx, hash_of_the_offer))
            f.close()

            return render_template("selling_offer_submited.html")
         else:
            gfg69 = findread(offer_fixed, "offers_buy.txt")

            gfg69_splitted = gfg69.split(",")
            hash_found = gfg69_splitted[2]


            gfg42 = findread(hash_found, "offers.txt")

            gfg42_splitted = gfg42.split(",")
            
            usr_havingoffer = str(gfg42_splitted[0])

            print("User making offer:", email_session_var)
            print("User having offer:", usr_havingoffer)
            ##part of transaction DUCO sell [find duco stuff]
            
            gfg31 = findread(email_session_var, "database_crypto.txt")

            gfg31_splitted = gfg31.split(",")
            user_usernameduco = gfg31_splitted[1]
            user_passwordduco = gfg31_splitted[2]
            user_trx_recipient = gfg31_splitted[4]

   ###get credentials where to send payment
            gfg21 = findread(usr_havingoffer, "database_crypto.txt")

            gfg21_splitted = gfg21.split(",")

            usr_havingoffer_duco_recipient = gfg21_splitted[1]
            usr_havingoffer_privatekey = gfg21_splitted[3]
            usr_havingoffer_trx_address = gfg21_splitted[4]

            time.sleep(5)
            request_payment = requests.get("https://server.duinocoin.com/transaction/?username={}&password={}&recipient={}&amount={}&memo=FurimeP2PExchange".format(user_usernameduco, user_passwordduco, usr_havingoffer_duco_recipient, str_duco)).json()
            print(request_payment)
   ##trx part seller receive TRX
            print("address TRX where to send", user_trx_recipient)
            print("TRX credentials (priv key, trx addr)", usr_havingoffer_privatekey, usr_havingoffer_trx_address)
            multiplier = (float_trx * 1000000)
            int_multiplier = (int(multiplier))
            print(multiplier)
            client = Tron()
            priv_key = PrivateKey(bytes.fromhex(usr_havingoffer_privatekey))

            txn = (
               client.trx.transfer(usr_havingoffer_trx_address, user_trx_recipient, int_multiplier)
               .memo("Furime")
               .build()
               .sign(priv_key)
            )
            
            print(txn.txid)
            print(txn.broadcast().wait())
            #file editing 3
            removelinefile(hash_found, "offers_buy.txt")
            removelinefile(hash_found, "offers.txt")

            price =  (int_trx / float(duco))
            f = open("price.json", "w")
            data = {'lastprice_trx':"{}".format(price)}
            jstr = json.dumps(data, indent=4)
            f.write(jstr)
            f.close()

            return render_template("found_simillar_offer.html")
      if offer_fixed not in offers_sell: #      if offer_fixed in offers_sell:
         to_hash = "{},{},{}".format(trx, duco, email_session_var)
         to_hash_encoded = to_hash.encode("utf-8")
         hash_of_the_offer = hashlib.sha224(to_hash_encoded).hexdigest()
         print (hash_of_the_offer)
         f = open("offers_sell.txt", "a")
         f.write("\n{},{},{}".format(duco, trx, hash_of_the_offer))
         f.close()
         f = open("offers.txt", "a")
         f.write("\n{},{},{},{}".format(email_session_var, duco, trx, hash_of_the_offer))
         f.close()
         return render_template("selling_offer_submited.html")


@app.route("/buy_duco")
def buy_duco():
   return render_template("buy_duco.html")

@app.route("/buy_duco_final")
def buy_duco_final():
   email_session_var = session['email_var']

   trx = request.args.get("trx")
   duco = request.args.get("duco")
   print("trx (price)", trx)
   print("duco (quantity)", duco)
   f = open("offers_sell.txt", "r") #check for simillar offer in buying section
   offers_sell = f.read() 
   print(offers_sell)
   str_duco = (str(duco))
   float_trx = (float(trx))
   offer_fixed = "{},{}".format(duco, trx)
   f = open("offers.txt", "r")
   offers_all = f.read()
   f.close()
##check for simillar offer

   gfg = findread(email_session_var, "database_crypto.txt")

 




   #check for balance

#here start
   gfg_splitted = gfg.split(",")
   user_trx_address = str(gfg_splitted[4])
   #      #email,duco_username,duco_password,trx_private_key,trx_addr
   client = Tron()
   str_trx_addr = (user_trx_address)
   trx_balance = client.get_account_balance(str_trx_addr)

   #check for balance
   if email_session_var in offers_all:
      return '''U made already one offer, remove it or wait''' 
   if (float(trx_balance)) < float(trx):
      return '''insufficient balance [TRX]'''
   else:
      if offer_fixed in offers_sell:
         gfg33 = findread(offer_fixed, "offers_sell.txt")

         gfg33_splitted = gfg33.split(",")
         hash_found1 = gfg33_splitted[2]
         float_duco_needed = (float(gfg33_splitted[0]))
         gfg99 = findread(hash_found1, "offers.txt")
         ### Check first if user have still funds
         gfg99_splitted = gfg99.split(",")
         usr_havingoffer = gfg99_splitted[0]
         gfg20 = findread(usr_havingoffer, "database_crypto.txt")
         
         gfg20_splitted = gfg20.split(",")

         duco_usr_userhavingoffer = gfg20_splitted[1]

         balance_check = requests.get("https://server.duinocoin.com/balances/{}".format(duco_usr_userhavingoffer)).json()


         float_balance_check = (float(balance_check["result"]["balance"]))

         print("needed duco on balance", gfg33_splitted[0])
         
##
         print("TRX Needed balance", gfg33_splitted[1])

         int_trx_needed = (float(gfg33_splitted[1]))


         if float_balance_check < float_duco_needed:
            removelinefile(hash_found1, "offers_sell.txt")
            removelinefile(hash_found1, "offers.txt")
            ###
     
            to_hash = "{},{},{}".format(trx, duco, email_session_var)
            to_hash_encoded = to_hash.encode("utf-8")
            hash_of_the_offer = hashlib.sha224(to_hash_encoded).hexdigest()
            print (hash_of_the_offer)
            f = open("offers_buy.txt", "a")
            f.write("\n{},{},{}".format(duco, trx, hash_of_the_offer))
            f.close()
            f = open("offers.txt", "a")
            f.write("\n{},{},{},{}".format(email_session_var, duco, trx, hash_of_the_offer))
            f.close()
            return render_template("buying_offer_submited.html")

         else:

         #first is duco in offers_buy

         ##duco part if user have still funds


            gfg69 = findread(offer_fixed, "offers_sell.txt")

            ###~~~~

            gfg69_splitted = gfg69.split(",")
            hash_found = gfg69_splitted[2]
            gfg42 = findread(hash_found, "offers.txt")

            ###   
            gfg42_splitted = gfg42.split(",")
            usr_havingoffer_email = gfg42_splitted[0]
            hash_found_offer = gfg42_splitted[3]
            print("User making offer:", email_session_var)
            print("User having offer:", usr_havingoffer_email)
            ##part of transaction DUCO sell [find duco stuff]
            gfg31 = findread(email_session_var, "database_crypto.txt")

            gfg31_splitted = gfg31.split(",")
            usr_havingoffer_ducousername = gfg31_splitted[1]
            usr_havingoffer_ducopassword = gfg31_splitted[2]
            usr_trx_privatekey = gfg31_splitted[3]
            usr_trx_addr = gfg31_splitted[4]

            print("DUCO credentials(usr,pass) ", usr_havingoffer_ducousername, usr_havingoffer_ducopassword)

   ###get credentials where to send payment
            gfg21 = findread(usr_havingoffer_email, "database_crypto.txt")

            gfg21_splitted = gfg21.split(",")

            user_ducousername = gfg21_splitted[1]
            user_ducopassword = gfg21_splitted[2]
            user_trx_addr = gfg21_splitted[4]
            time.sleep(5)
            ###
            print(gfg31_splitted[1])
            request_payment = requests.get("https://server.duinocoin.com/transaction/?username={}&password={}&recipient={}&amount={}&memo=FurimeP2PExchange".format(username_duco, user_ducopassword, usr_havingoffer_ducousername, str_duco )).json()
   ##trx part seller receive TRX
            print("address TRX where to send", user_trx_addr)
            print("TRX credentials (priv key, trx addr)", usr_trx_privatekey, usr_trx_addr)
            multiplier = (float_trx * 1000000)
            print(multiplier)
            int_multiplier = int(multiplier)
            client = Tron()
            priv_key = PrivateKey(bytes.fromhex(usr_trx_privatekey))

            txn = (
               client.trx.transfer( usr_trx_addr, user_trx_addr, int_multiplier)
               .memo("Furime")
               .build()
               .sign(priv_key)
            )
            print(txn.txid)
            print(txn.broadcast().wait())
            #file editing 3

            removelinefile(hash_found_offer, "offers_sell.txt")
            removelinefile(hash_found_offer, "offers.txt")

            price =  (float_trx / float(duco))
            f = open("price.json", "w")
            data = {'lastprice_trx':"{}".format(price)}
            jstr = json.dumps(data, indent=4)
            f.write(jstr)
            print(jstr)
            f.close()

            return render_template("found_simillar_offer.html")
      if offer_fixed not in offers_sell: #      if offer_fixed in offers_sell:
         to_hash = "{},{},{}".format(trx, duco, email_session_var)
         to_hash_encoded = to_hash.encode("utf-8")
         hash_of_the_offer = hashlib.sha224(to_hash_encoded).hexdigest()
         print (hash_of_the_offer)
         f = open("offers_buy.txt", "a")
         f.write("\n{},{},{}".format(duco, trx, hash_of_the_offer))
         f.close()
         f = open("offers.txt", "a")
         f.write("\n{},{},{},{}".format(email_session_var, duco, trx, hash_of_the_offer))
         f.close()
         return render_template("buying_offer_submited.html")


@app.route("/remove_offer")
def remove_offer():
   hash_of_offer = request.args.get("hash")
   email_session_var = session['email_var']
   print(email_session_var)
   print(hash_of_offer)
   f = open("offers_sell.txt", "r")
   offers_sell_read = f.read()
   f = open("offers_buy.txt", "r")
   offers_buy_read = f.read()
   content = open("offers.txt").readlines()
   lookup = (str(hash_of_offer))
   lines = [line_num for line_num, line_content in enumerate(content) if lookup in line_content]
   print(lines)
   list1 = lines
   str1 = ''.join(str(e) for e in list1)
   print(str1)
   line_to_read = (int(str1)) + 1
   print(line_to_read)
   with open("offers.txt", "r") as f:
      lines = f.readlines() 
   line1 = lines[int(str1)]
   gfg = line1.replace("\n", "")
   print("OFFERS HERE ", gfg)
   find_email = gfg.split(",")
   print("EMAIL TO EQUAL TOO", find_email[0])

   if (str(email_session_var)) == (str(find_email[0])):
      ###
      with open("offers.txt", "r") as infile:
         lines = infile.readlines()

      with open("offers.txt", "w") as outfile:
         for pos, line in enumerate(lines):
            if pos != (int(str1)):
                  outfile.write(line)
      ##remove from  sell
      if hash_of_offer in offers_sell_read:
         print("hash of offer found in SELL")
         content2 = open("offers_sell.txt").readlines()
         lookup2 = (str(hash_of_offer))
         lines2 = [line_num for line_num, line_content in enumerate(content2) if lookup2 in line_content]
         print(lines2)
         list2 = lines2
         str2 = ''.join(str(e) for e in list2)
         print("LINE SELL HERE", str2)

         with open("offers_sell.txt", "r") as infile:
            lines = infile.readlines()

         with open("offers_sell.txt", "w") as outfile:
            for pos, line in enumerate(lines):
               if pos != (int(str2)):
                     outfile.write(line)
         return '''removed offer'''
           
   ##offer buy 
      if hash_of_offer in offers_buy_read:
         print("hash of offer found in BUY")
         content3 = open("offers_buy.txt").readlines()
         lookup3 = (str(hash_of_offer))
         lines3 = [line_num for line_num, line_content in enumerate(content3) if lookup3 in line_content]
         print(lines3)
         list3 = lines3
         str3 = ''.join(str(e) for e in list3)
         print("LINE BUY HERE", str3)

         with open("offers_buy.txt", "r") as infile:
            lines = infile.readlines()

         with open("offers_buy.txt", "w") as outfile:
            for pos, line in enumerate(lines):
               if pos != (int(str3)):
                     outfile.write(line)
         return '''removed offer'''

if __name__=='__main__':
   app.run()

if __name__ == "__main__":
   app.run(host='0.0.0.0',port=2727)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    app.run(host=ip, port=port, ssl_contest="adhoc")


if __name__ == '__main__':
    socketio.run(app)
