

def main(einParameter : str = "nix", einZweiterParameter : str = "aNix!" ) -> None:
    print("ein Python CHeatSheet!")

    

    meineListe : list = ["eins","zwei","drei","viele..."]

    print("Mein Parameter einParameter: ",einParameter)
    print(f"Mein Parameter einZweiterParameter:\
           {einZweiterParameter}")

    meineListe.append("noch viel mehr..")

    print(meineListe)
    print(*meineListe, sep=" - ")

    from mein_paket.meineKlasse import MeineKlasse

    einObjekt = MeineKlasse()

    print(einObjekt)

    print("Das vierte Element ist:", meineListe[3],sep="\n")

    verkehrteListe = meineListe.copy()

    verkehrteListe.reverse()
    print("Die kopierte verkehrte Liste: ", verkehrteListe)

    meineListe[3] ="vier"
    print("Die veränderte Liste: ", meineListe)

    print(f"Die Liste ist {len(meineListe)} Elemente lang")

    print(f"Wir nehmen das Element {meineListe.pop()} heraus")

    for einListenEintrag in meineListe:
        print("Ein Eintrag in der Liste", einListenEintrag, sep=": ")

    for i in range(11):
        print(f"{i}, ")

    for i in range(1,10+1,2):
        print(f"{i}, ")

if __name__ == "__main__":
    main()
    main("schon etwas!")
    main(einZweiterParameter="November",einParameter="is no None")

