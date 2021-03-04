#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("--i", "--interface", dest="interface", help="Interface to change")
    parser.add_option("--m", "--mac", dest="new_mac", help="New Mac Address")
    return parser.parse_args()


def change_mac(interface, new_mac):
    print("Changing the MAC Address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    print(options.new_mac + " has been assigned to " + options.interface)


(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
