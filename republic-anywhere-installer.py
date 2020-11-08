
#/usr/local/bin/python3.8.6
"""
This python file will be responsible for breaking down and installing Republic Anywhere.
A variety of steps must be completed, such as:
 * Getting root access if the file is not run as root.
 * Installing libgconf-2-4 if not currently installed on the system.
 * Creating the apt-source file for Republic Anywhere.
 * Fetching and adding the apt-key for Republic Anywhere.
 * Updating package list.
 * Installing Republic Anywhere.
"""
import os
import sys
import subprocess

def build_messages():
    return

def check_root_access():
    is_root = os.geteuid() == 0
    return is_root

def check_for_libgconf():
    return

def install_libgconf():
    return

def create_apt_source_file():
    return

def add_apt_key():
    return

def update_apt_packages():
    return

def install_republic_anywhere():
    return

def verify_install():
    return

def main():
    return

if __name__ == '__main__':
    main()
