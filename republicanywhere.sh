#!/bin/bash
brand="Republic Anywhere"
response="RESPONSE"
forumurl="https://forums.republicwireless.com/t/beta-member-support-only-how-to-install-republic-anywhere-on-linux/"

greeting="Welcome, this script will install $brand on Ubuntu and Debian distributions as well as it's dependencies. APT Warnings can be ignored.

outputfile="republicscriptoutput.txt"

The following actions will be performed:
 * Check for libgconf-2-4.
 * Install libgconf-2-4 if necessary.
 * Fetch the $brand .deb package.
 * Add the $brand key to your keys.
 * Refresh the apt package list.
 * Install $brand."

if [ "$UID" -ne 0 ]
	then
		echo "Script not running as root, password required."
		exec sudo bash "$0" "$@"
	fi

echo "$greeting"

republicanywherepresent=$(apt -qq --installed list republicanywhere)
if [ ! -z "$republicanywherepresent" ]
then
	echo "$brand is already installed, terminating script."
	exit 0
fi

read -r -p "Would you like to continue? (Y/N):" response

if [[ "$response" == [yY]* ]]
then
	libgconfpresent=$(apt -qq --installed list libgconf-2-4)
	
	if [ ! -n "$libgconfpresent" ]
	then
		echo "libgconf-2-4 found, install not necessary."
	else
		echo "libgconf-2-4 is missing and will be installed."
		echo "Installing libgconf-2-4..."
		exec -c sudo apt-get install -y libgconf-2-4 &> /dev/null
	fi
	
	echo "Fetching $brand .deb package..."
	exec -c echo "deb [arch=amd64] https://s3.amazonaws.com/files.republicwireless.com/public/apps/anywhere/debian main main" | tee /etc/apt/sources.list.d/republicanywhere.list
	
	echo "Adding $brand key to your keys..."
	exec -c wget -O - https://s3.amazonaws.com/files.republicwireless.com/public/apps/anywhere/debian/key/public | sudo apt-key add - &> /dev/null
	
	echo "Updating package list..."
	exec -c sudo apt-get update &> /dev/null
	
	echo "Installing $brand..."
	exec -c sudo apt-get install -y republicanywhere &> /dev/null
	echo "Install completed..." "If $brand does not appear in your app menu restart your computer." "Exiting..."
	exit 0
else
	echo "Permission not granted terminating script."
	exit 0
fi
echo "End of file reached, the script did not run correctly.
exit 0
	
	
