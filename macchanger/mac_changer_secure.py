#!/usr/bin/env python
import subprocess

interface = input ("interface: ")
new_mac = input("New MAC: ")

print("Changing the MAC Address of " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print(new_mac + " has been assigned to " + interface)