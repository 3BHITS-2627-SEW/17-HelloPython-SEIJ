class MeineKlasse:
    def __init__(self):
        self.__name = "EineKlasse"


    def noNoneNovember(self):
        return("November!")


    def get_name(self) -> str:
        return self.__name

    def set_name(self, neuer_name : str) -> None:
        self.__name = neuer_name