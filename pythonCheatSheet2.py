import numpy

import numpy as npy

from numpy import number as npynb

from numpy import *

from mein_paket.meineKlasse import meineKlasse

def main():
    number = numpy.sqrt(4)
    print("Die Wurzel von 4 ist: ", number)
    number2 = npy.sqrt(16)
    print("Die Wurzel von 16 ist: ", number2)


    meinObjekt = meineKlasse()
    print("Name von Objekt: ", "PRIVAT")    #meinObjekt.__name)
    print("Welcher Monat ist es? ", meinObjekt.noNoneNovember())

    meinObjekt.set_name("meinObjekt")
    print("Namen nach Aenderung:",meinObjekt.get_name())

    pass

if __name__ == "__main__":
    main()

