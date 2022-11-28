'''





Figyelem a lentebb látható kód az elme megbontására alkalmas.
Senkinek nem tanácsoljuk a beleolvasást! Főleg azoknak nem akik értenek is hozzá!
Amennyiben beleolvasol és maradandó agykárosodást szenvedsz a csapatunk nem vállalja érte a felelőséget.
(A kód csúnyábbik részei itt vannak elrejtve!)







'''
def print_d(data):
    import sys
    if data != "":
        sys.exit(str(data))
    else:
        sys.exit()

base = {
    "0" : "0",
    "1" : "128",
    "2" : "192",
    "3" : "224",
    "4" : "240",
    "5" : "248",
    "6" : "252",
    "7" : "254",
    "8" : "255",
}


def bsubnet_calc():
    subnet = input("Add meg az alap subnet maskot: ")
    ln = int()
    if subnet == "":
        #A közös a 1, 9, 17, 25 számokban az n+8
        pref = input("Add meg az alap subnet mask prefixét: ")
        #Ha 1 a prefix akkor 0.0.0.0 lesz mivel nem lép be a ciklusba
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
    else:
        # Ha üres a subnetmask és van prefix megadva akkor abból számolja ki a subnetmaskot
        test = subnet.split(".")
        count = test.count("255")
        if  "0" in subnet:
            test = list(filter(lambda x:x is not '0', test))
        search = dict((new_val,new_k) for new_k,new_val in base.items()).get(test[-1])
        if test[-2] == test[-1]:
            pref = 8*count
        else:
            pref = 8*count+int(search)
        #Subnet 0 értékek hozzáadása
    if subnet[-1] == ".":
        subnet = subnet+base[str(ln)]
    test = subnet.split(".")
    while len(test) < 4:
        subnet = subnet+"."+base["0"]
        test = subnet.split(".")
    return subnet, pref, ln

def subnet_calc():
    subnet = input("Add meg az subnet maskot: ")
    ln = int()
    if subnet == "":
        #A közös a 1, 9, 17, 25 számokban az n+8
        pref = input("Add meg a subnet mask prefixét: ")
        if not(pref == "" or int(pref) < 1):
            #Ha 1 a prefix akkor 0.0.0.0 lesz mivel nem lép be a ciklusba
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
        else:
            print("Hiba: A prefix nem lehet üres vagy kissebb mint 1!")
    else:
        # Ha üres a subnetmask és van prefix megadva akkor abból számolja ki a subnetmaskot
        test = subnet.split(".")
        count = test.count("255")
        if  "0" in subnet:
            test = list(filter(lambda x:x is not '0', test))
        search = dict((new_val,new_k) for new_k,new_val in base.items()).get(test[-1])
        if test[-2] == test[-1]:
            pref = 8*count
        else:
            pref = 8*count+int(search)
        #Subnet 0 értékek hozzáadása
    if subnet[-1] == ".":
        subnet = subnet+base[str(ln)]
    test = subnet.split(".")
    while len(test) < 4:
        subnet = subnet+"."+base["0"]
        test = subnet.split(".")
    return subnet, pref, ln

def anding(ipbin, subnetbin):
    ipoctet = ""
    for i in range(len(subnetbin)):
        #Éseléssel összehasonlírom a két számot és ha a subnetben van 1 akkor felszámolom!
        if subnetbin[i] == "0":
            ipoctet = ipoctet+"0"
        else:
            ipoctet = ipoctet+ipbin[i]
    n = 0
    NetList = []
    while n <= 32:
        NetList.append(ipoctet[n:n+8])
        n += 8
    return NetList
def bc(ipbin, subnetbin):
    iploctet = ""
    NetList = []
    for i in range(len(subnetbin)):
        #Éseléssel összehasonlírom a két számot és ha a subnetben van 1 akkor felszámolom!
        if subnetbin[i] == "0":
            iploctet = iploctet+"1"
        else:
            iploctet = iploctet+ipbin[i]
    
    n = 0
    NetList = []
    while n <= 32:
        NetList.append(iploctet[n:n+8])
        n += 8
    return NetList
def DecimalToBinary(num):
    bin = ""
    if num >= 128:
        num -= 128
        bin = bin+"1"
    else:
        bin = bin+"0"
    if num >= 64:
        num -= 64
        bin = bin+"1"
    else:
        bin = bin+"0"
    if num >= 32:
        num -= 32
        bin = bin+"1"
    else:
        bin = bin+"0"
    if num >= 16:
        num -= 16
        bin = bin+"1"
    else:
        bin = bin+"0"
    if num >= 8:
        num -= 8
        bin = bin+"1"
    else:
        bin = bin+"0"
    if num >= 4:
        num -= 4
        bin = bin+"1"
    else:
        bin = bin+"0"
    if num >= 2:
        num -= 2
        bin = bin+"1"
    else:
        bin = bin+"0"
    if num >= 1:
        num -= 1
        bin = bin+"1"
    else:
        bin = bin+"0"
    return bin

def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return str(decimal)
