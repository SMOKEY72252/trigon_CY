import os
import socket
import random
import subprocess
subprocess.run(['clear'])

RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
print('''\033[32m
             _______   _____
          __-      -_-      -__
      ___-                     -____
      \      \033[36m    cybar218    \033[32m      /
       \      ddos atrack 02      /
        \                        /
         \     web site ipv6    /
          \    web site scan   /
           \      sqltool     /
            \      niktoT    /
             \      Nmap    /
              \____________/

''')

import subprocess
print('''
================================================
''')
print("        \033[35m        1.ddos", end=' ')
print("       2.sqlmap")
print('''
''')
print("                3. nikto", end=' ')
print("     4.nmap")
print('''
''')
print("                5.hydra", end=' ')
print("      6.metasploit")
print('''
\033[32m================================================
''')
choice = input("\033[36msel\033[34mect: ")

if choice == '1':
    result = subprocess.run(['git', 'clone', 'https://github.com/cyweb/hammer'], capture_output=True, text=True)
    print(result.stdout)
if choice == '2':
    result = subprocess.run(['git', 'clone', 'https://github.com/sqlmapproject/sqlmap.git'], capture_output=True, text=True)
    print(result.stdout)
if choice == '3':
    result = subprocess.run(['git', 'clone', 'https://github.com/sullo/nikto'], capture_output=True, text=True)
    print(result.stdout)
if choice == '4':
    result = subprocess.run(['pkg', 'install', 'nmap'], capture_output=True, text=True)
    print(result.stdout)
if choice == '5':
    result = subprocess.run(['git', 'clone', 'https://github.com/isuruwa/T-HYDRA'], capture_output=True, text=True)
    print(result.stdout)
if choice == '6':
    result = subprocess.run(['git', 'clone', 'https://github.com/h4ck3r0/Metasploit-termux'], capture_output=True, text=True)
    print(result.stdout)
