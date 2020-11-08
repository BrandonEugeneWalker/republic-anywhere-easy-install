
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
import apt

def build_messages():
    return

def check_root_access():
    is_root = os.geteuid() == 0
    return is_root

def get_apt_cache():
    cache = apt.cache.Cache()
    update_apt_cache(cache)
    cache.open()
    return cache

def update_apt_cache(cache):
    cache.update()
    return

def open_apt_cache(cache):
    cache.open()
    return

def close_apt_cache(cache):
    cache.close()
    return

def commit_apt_changes(cache):
    try:
        cache.commit()
    except Exception as arg:
        print >> sys.stderr, 'Sorry, package instillation failed. Error: [{err}]'.format(err=str(arg))

def install_libgconf(cache):
    package_name = 'libgconf-2-4'
    package = cache[package_name]
    if package.is_installed:
        print('{package_name} is already installed, skipping this step.'.format(package_name = package_name))
    else:
        package.mark_install()

    return

def create_apt_source_file():
    apt_source_contents = 'deb [arch=amd64] https://s3.amazonaws.com/files.republicwireless.com/public/apps/anywhere/debian main main'
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
