import sys
from defines import *

ip = input("Enter the IP address: ")
test = ip.split(".")
if len(test) < 3:
    sys.exit("Error: IP address cannot be shorter or longer than 4 octets!")

bsubnet, bpref, bln = bsubnet_calc()

subnet, pref, ln = subnet_calc()
ketto = int(pref)-int(bpref)
negy = 32-int(pref)
ot = (2**negy)
subnetting = subnet.split(".")
subnetbin = ""
for i in subnetting:
    i = DecimalToBinary(int(i))
    subnetbin = subnetbin+str(i)
subnetting = ip.split(".")
ipbin = ""
for i in subnetting:
    i = DecimalToBinary(int(i))
    ipbin = ipbin+i

NetList = anding(ipbin, subnetbin)

NetID1 = BinaryToDecimal(int(NetList[0]))
NetID2 = BinaryToDecimal(int(NetList[1]))
NetID3 = BinaryToDecimal(int(NetList[2]))
NetID4 = BinaryToDecimal(int(NetList[3]))

NetID = NetID1+"."+NetID2+"."+NetID3+"."+NetID4

NetList = bc(ipbin, subnetbin)

NetID1s = BinaryToDecimal(int(NetList[0]))
NetID2s = BinaryToDecimal(int(NetList[1]))
NetID3s = BinaryToDecimal(int(NetList[2]))
NetID4s = BinaryToDecimal(int(NetList[3]))

NetIDs = NetID1s+"."+NetID2s+"."+NetID3s+"."+NetID4s

print(ip, end="/"+str(pref)+"\n")
print(bsubnet, end=" = "+str(bpref)+"\n")
print(subnet, end=" = "+str(pref)+"\n")
print(f"Number of subnet bits: {ketto}")
print(f"Number of subnets created: {2**ketto}")
print(f"Number of host bits per subnet: {negy}")
print(f"Number of hosts per subnet: {ot-2}")
print(f"NetID: {NetID}")
print(f"First IP: {NetID1+'.'+NetID2+'.'+NetID3+'.'+str(int(NetID4)+1)}")
print(f"Last IP: {NetID1s+'.'+NetID2s+'.'+NetID3s+'.'+str(int(NetID4s)-1)}")
print(f"Broadcast: {NetIDs}")
