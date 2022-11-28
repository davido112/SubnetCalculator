from defines import *

data = int(input("Hány részre kell osztani a hálózatot? "))
if data == "":
    print_d("Hiba: A részekre osztás nem kihagyható!")

ip = input("Add meg az IP címet: ")
ips = ip.split(".")
if ip == "":
    print_d("Hiba: Az IP Cím nem lehet üres!")

if ips[0] > "0" and ips[0] <= "127":
    print_d("a")
elif ips[0] >= "128" and ips[0] <= "191":
    print_d("b")
elif ips[0] >= "192" and ips[0] <= "223":
    print_d("c")
mnnum = []
prefl = []
subnetmask = []
for i in range(data):

    host = int(input("Mennyi host fog kelleni? "))+2
    if host == "":
        print_d("Hiba: A hostok száma nem lehet üres!")

    hosts = ["2", "4", "8", "16", "32", "64", "128"]
    h = 1
    for i in hosts:
        if host <= int(i):
            break
        h += 1
    mn = 2**h
    mnnum.append(mn)
    prefl.append(32-h)
for pref in prefl:
    subnet = ""
    for counter in range(int(pref), 1, -8):
                if counter <= 9 or counter == 9 or counter == 8:
                    ln = counter
                    if counter == 9:
                        ln = 1
                    elif counter == 8:
                        ln = 0
                    else:
                        break
                subnet = "255."+subnet
    if subnet[-1] == ".":
        subnet = subnet+base[str(ln)]
        subnetmask.append(subnet)
    test = subnet.split(".")
    while len(test) < 4:    
        subnet = subnet+"."+base["0"]
        test = subnet.split(".")
    ipbin = ""
    for i in ips:
        i = DecimalToBinary(int(i))
        ipbin = ipbin+i
    subnetbin = ""
    sm = 0
    for i in test:
        if sm < 3 or i != "255":
            i = DecimalToBinary(int(i))
            subnetbin = subnetbin+i
            sm += 1

NetList = anding(ipbin, subnetbin)

NetID1 = BinaryToDecimal(int(NetList[0]))
NetID2 = BinaryToDecimal(int(NetList[1]))
NetID3 = BinaryToDecimal(int(NetList[2]))
NetID4 = BinaryToDecimal(int(NetList[3]))

s = 0
asd = 0
for i in mnnum:
    asd += i
if asd < 255:
    for i in mnnum:
        NetID = NetID1+"."+NetID2+"."+NetID3+"."+str(NetID4)
        print(str(s)+".adat: NetID: "+NetID+"/"+str(prefl[s]))
        print("Subnetmask: "+subnetmask[s])
        NetID = NetID1+"."+NetID2+"."+NetID3+"."+str(int(NetID4)+1)
        print("Első IP: "+NetID)
        save = NetID4
        NetID4 = int(NetID4)+int(i)
        NetID = NetID1+"."+NetID2+"."+NetID3+"."+str(NetID4-2)
        print("Utolsó IP: "+NetID)
        NetID4 = save
        NetID4 = int(NetID4)+int(i)
        NetID = NetID1+"."+NetID2+"."+NetID3+"."+str(NetID4-1)
        print("Broadcast: "+NetID, end="\n\n")
        s += 1
else:
    print("Hiba: Nem lépheted át az octet határt. Válassz másik osztálybeli címet!")