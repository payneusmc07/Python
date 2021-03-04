#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("--i", "--interface", dest="interface", help="Interface to change")
    parser.add_option("--m", "--mac", dest="new_mac", help="New Mac Address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        # code to handle error
        parser.error("Please specify an interface, use --help for more information.")

    elif not options.new_mac:
        # response to error
        parser.error("Please specify a new MAC Address, use --help for more information.")
    return options


def change_mac(interface, new_mac):
    print("Changing the MAC Address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print(" [-] Could not read MAC Address.")


options = get_arguments()

current_mac = get_current_mac(options.interface)

print("Current MAC = " + current_mac)

change_mac(options.interface, options.new_mac)

print("The MAC Address of " + options.interface + " was changed to " + options.new_mac)





