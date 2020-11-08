
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

def check_root_access():
    is_root = os.geteuid() == 0
    return is_root

def get_apt_cache():
    cache = apt.cache.Cache()
    cache.update()
    cache.open()
    return cache

def close_apt_cache(cache):
    cache.close()
    return

def commit_apt_changes(cache):
    try:
        cache.commit()
    except Exception as arg:
        print >> sys.stderr, 'Sorry, package instillation failed. Error: [{err}]'.format(err=str(arg))
    return

def check_if_anywhere_installed():
    cache = get_apt_cache()
    package_name = 'republicanywhere'
    try:
        package = cache[package_name]
        results = package.is_installed()
        return results
    except KeyError:
        return False



def install_libgconf(cache):
    package_name = 'libgconf-2-4'
    package = cache[package_name]

    print('Checking for {package_name}'.format(package_name = package_name))

    if package.is_installed:
        print('{package_name} is already installed, skipping this step.'.format(package_name = package_name))
    else:
        print('{package_name} not found and will be installed.'.format(package_name = package_name))
        package.mark_install()
    return

def create_apt_source_file():
    apt_source_contents = 'deb [arch=amd64] https://s3.amazonaws.com/files.republicwireless.com/public/apps/anywhere/debian main main'
    file_location = '/etc/apt/sources.list.d/republicanywhere.list'
    with open(file_location, 'w') as republic_apt_source:
        republic_apt_source.write(apt_source_contents)
    return

def add_apt_key():
    command_text = "sudo apt-key adv --fetch-keys https://s3.amazonaws.com/files.republicwireless.com/public/apps/anywhere/debian/key/public"
    command_text_list = command_text.split(' ')
    subprocess.run(command_text_list, stdout=subprocess.DEVNULL)
    return

def install_republic_anywhere(cache):
    package_name = 'republicanywhere'
    package = cache[package_name]

    if package.is_installed:
        print('{package_name} is already installed, skipping this step.'.format(package_name = package_name))
    else:
        print('Installing {package_name}...'.format(package_name = package_name))
        package.mark_install()
    return

def finalize_install():
    cache = get_apt_cache()
    install_libgconf(cache)
    install_republic_anywhere(cache)
    commit_apt_changes(cache)
    close_apt_cache(cache)
    return

def print_greeting():
    greeting = """Welcome, this program will install Republic Anywhere on Ubuntu and Debian distributions as well as it's dependencies.

The following actions will be performed:
 * Fetch the Republic Anywhere .deb package.
 * Add the Republic Anywhere key to your keys.
 * Refresh the apt package list.
 * Check for libgconf-2-4.
 * Install libgconf-2-4 if necessary.
 * Install Republic Anywhere"""
    print(greeting)
    return

def print_exit_message():
    exit_message = """Republic Anywhere was sucessfully installed on your system.
    If you have any issues you can find help by going to:
    https://forums.republicwireless.com/t/beta-member-support-only-how-to-install-republic-anywhere-on-linux/"""
    print(exit_message)
    return

def print_whitespace():
    whitespace = """

    """
    print(whitespace)
    return

def get_user_permission():
    user_input = input('Would you like to continue? (yes/no):')
    lower_case_input = user_input.lower()
    is_permission_granted = (lower_case_input == 'yes' or lower_case_input == 'y')
    return is_permission_granted
    

def main():
    is_installed = check_if_anywhere_installed()
    if is_installed:
        print('Republic Anywhere is already present on your system, aborting install.')
        exit(0)
    
    print_greeting()
    print_whitespace()

    is_permission_granted = get_user_permission()
    if not is_permission_granted:
        print('Permission not granted, aborting install.')
        exit(0)
    
    print_whitespace()
    print('Creating apt source file for Republic Anywhere.')
    create_apt_source_file()

    print('Fetching and adding apt key for Republic Anywhere.')
    add_apt_key()

    print_whitespace()
    finalize_install()

    print_whitespace()
    print_exit_message()
    return

if __name__ == '__main__':
    main()
