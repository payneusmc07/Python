import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("--i", "--interface", dest="interface", help="Interface to change")
parser.add_option("--m", "--mac", dest="new_mac", help="New Mac Address")

(options, arguments) = parser.parse_args()

# interface = input ("interface: ")
# new_mac = input("New MAC: ")

interface = options.interface
new_mac = options.new_mac

print("Changing the MAC Address of " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print(new_mac + " has been assigned to " + interface)
