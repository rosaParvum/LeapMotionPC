import bluetooth
from sys import exit

wiimoteN = "Nintendo RVL-CNT-01"
wiimoteA = None

print "Starting search..."
nearby_devices = bluetooth.discover_devices(lookup_names=True)

print("Search over, scanning for wiimote.\n")
if len(nearby_devices) > 0:
    for address in nearby_devices:
        if bluetooth.lookup_name(address[0]) == wiimoteN:
            wiimoteA = address[0]
            break

if wiimoteA:
    print wiimoteN
    print wiimoteA
else:
    print("Wiimote not found.")
    exit(0)

print("Wiimote found, continuing")

print bluetooth.read_local_bdaddr()[0]
reva = bluetooth.read_local_bdaddr()[0].split(":")
print reva
reva.reverse()
print reva
reva  = "".join(reva)
print reva

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)
