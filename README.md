# Republic Anywhere Install Script
A python3 installer script for Republic Anywhere that simplifies common issues with instillation. This script will **ONLY** work on *Ubuntu or Debian* based distributions.

This script is **not** intended for MacOS or Windows systems, or Linux systems lacking APT.
This script is not affiliated with or endored by Republic Wireless in *any* way. 
Always be aware of the dangers of using unfamiliar scripts and programs.

## Usage
* Download the python script found under releases.
* Open the terminal (Super+T shortcut on most desktops.)
* Navigate to the directory you downlaoded the script to. For example for Downloads simply do [ cd ~/Downloads/ ].
* Run the script using python3 like so. [ sudo python3 ./republic_anywhere_installer.py ].
* Input your password and accept to install Republic Anywhere.

## Common Issues
If the apt package manager is being used by any other programs there will be a lock on it.
A lock on apt means that other programs cannot use apt till the other tasks finish.
If you get a apt-lock error when running the script simply wait for whatever process is using it to finish.

Other errors such as unhandled exceptions can be reported here:
https://forums.republicwireless.com/t/beta-member-support-only-how-to-install-republic-anywhere-on-linux/