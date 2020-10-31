#!/bin/bash
brand="Republic Anywhere"
response="RESPONSE"
forumurl="https://forums.republicwireless.com/t/beta-member-support-only-how-to-install-republic-anywhere-on-linux/"

greeting="Welcome, this script will install $brand on Ubuntu and Debian distributions as well as it's dependencies. APT Warnings can be ignored.

The following actions will be performed:
 * Check for libgconf-2-4.
 * Install libgconf-2-4 if necessary.
 * Fetch the $brand .deb package.
 * Add the $brand key to your keys.
 * Refresh the apt package list.
 * Install $brand."

echo "$greeting"

republicanywherepresent=$(apt -qq --installed list republicanywhere)
if [ ! -z "$republicanywherepresent" ]
then
	echo "$brand is already installed, terminating script."
	exit 0
fi

read -p "Continue? (Y/N): " response

if ["$response" == 'YES']
then
	[ "$UID" -eq 0] || exec sudo bash "$0" "$@"
	exec clear
	libgconfpresent=$(apt -qq --installed list libgconf-2-4)
	
	if [ ! -n "$libgconfpresent" ]
	then
		echo "libgconf-2-4 found, install not necessary."
	else
		echo "libgconf-2-4 is missing and will be installed."
		echo "Installing libgconf-2-4..."
		exec sudo apt-get install -y libgconf-2-4
		exec clear
	fi
	
	echo "Fetching $brand .deb package..."
	exec sudo sh -c 'echo "deb [arch=amd64] https://s3.amazonaws.com/files.republicwireless.com/public/apps/anywhere/debian main main" > /etc/apt/sources.list.d/republicanywhere.list'
	exec clear
	
	echo "Adding $brand key to your keys..."
	exec wget -O - https://s3.amazonaws.com/files.republicwireless.com/public/apps/anywhere/debian/key/public | sudo apt-key add -
	exec clear
	
	echo "Updating package list..."
	exec sudo apt update
	exec clear
	
	echo "Installing $brand..."
	exec sudo apt-get install -y republicanywhere
	exec clear
	echo "Install completed..." "If $brand does not appear in your app menu restart your computer." "Exiting..."
	exit 0
else
	exec clear
	echo "Permission not granted terminating script."
	exit 0
fi
exit 0
	
	
