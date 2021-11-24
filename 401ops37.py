#!/usr/bin/env python3

# Script Name                           401ops37.py
# Author                                Bill Kachersky
# Date of last revision                 11/23/2021
# Description of purpose                Cookie Capture


# Resources and Thanks
# https://github.com/codefellows/seattle-cyber-401d3/blob/main/class-37/challenges/DEMO.md
# https://www.dev2qa.com/how-to-get-set-http-headers-cookies-and-manage-sessions-use-python-requests-module/
# https://stackoverflow.com/questions/50329050/save-load-html-response-as-object-in-a-file-python



# Modules
import requests, os


# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')
    print("Target site is " + targetsite)
    print(cookie)




# Main

bringforthcookiemonster()

page = requests.get(targetsite, cookies=cookie)
page_content = page.text

with open ('/home/billkach/crumbs.html', 'w') as c:
  c.write(page_content)

os.system("firefox /home/billkach/crumbs.html")


# End