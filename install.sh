#!/bin/bash 
Green='\033[0;32m'
white='\033[0;37m'
NC='\033[0m'
clear
printf '\033]2; INSTALLER\a'
echo -e "${Green}[*] Press \e[0;33many key\e[0;32m to install OGRE..."
read -n 1 
clear

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [[ "$DIR" != "/root/Ogre" ]]
then
	echo -e "\033[0;35m[~] I will install it for you..."
	sleep 4
	if [[ -d /root/Ogre ]]
	then 
		rm -r /root/Ogre
	fi
	mkdir /root/Ogre
	cp -r "$DIR"/* /root/Ogre
	chmod +x /root/Ogre/install.sh
	#gnome-terminal -- bash -c "sudo /root/bootmiester/install.sh; exec bash"
fi
echo -e "${Green}[+] Installing OGRE..."
sleep 1
echo -e "${Green}[+] Fixing permissions..."
sleep 2
chmod +x /root/Ogre/ogre.py
clear
echo -e "${Green}[+] Copying Tool to /bin/ogre"
cd /root/Ogre
cp /root/Ogre/ogre.py /bin/ogre
clear

while true
do  
	clear
	echo -e "${Green}[*] Are you \e[0;33mu\e[0;32mpdating or \e[0;33mi\e[0;32mnstalling the script?(\e[0;33mu\e[0;32m/\e[0;33mi\e[0;32m): "
	echo -e "Only use 'i' for the first time."
	read UORI
	if [[ "$UORI" = "u" ]]
	then 
		clear 
		echo -e "This feature is currently under construction.."
		sleep 3
		exit
	elif [[ "$UORI" = "i" ]]
	then 
		clear
		BASHCHECK=$(cat ~/.bashrc | grep "/bin/ogre")
		if [[ "$BASHCHECK" != "" ]]
		then 
			echo -e "I SAID USE i ONLY ONE TIME..........."
			sleep 3
			break
		fi
		echo -e "${Green}[+] Adding OGRE to PATH so you can access it from anywhere"
		sleep 1
		export PATH=/bin/ogre:$PATH
		sleep 1
		echo "export PATH=/bin/ogre:$PATH" >> ~/.bashrc
		sleep 1
		clear
		break
	fi
done
clear
echo -e "${Green}[+] Installing Hyda.."
sudo apt install hydra
sleep 0.5
echo -e "${Green}[~] Installation is finished. Type 'ogre' to launch the tool after we exit."
sleep 0.5
echo -en "${Green}[*] Starting ogre"; sleep 0.5 ;echo -en "." ;sleep 0.5 ;echo -en "." ;sleep 0.5 ;echo -en "." ;sleep 0.5 ;echo -en "." ;
ogre

