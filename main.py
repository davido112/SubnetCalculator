import sys

vlsm = input("Mit szeretnél számolni a programmal?(vlsm=v, subneting=s) ")
if vlsm.lower() == 's':
    from subneting import *
elif vlsm.lower() == 'v':
    from vlsm import *
else:
    print("Hiba: A megadott szöveg nem értelmezhető!")