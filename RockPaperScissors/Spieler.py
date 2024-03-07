class Player:
    def __init__(self, name):
        self.name= name

    def option(self):
        try:
            incorrectinsert=True
            while incorrectinsert:
                option=int(input("Choose Option( (1)Schere, (2)Stein, (3)Papier, (4)Echse, (5)Spock:):"))
                if option in range(0,6):
                    return option
                else:
                    print("Eingabe ungültig")
        except ValueError:
            print(ValueError)