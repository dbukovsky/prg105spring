class Auto:
    def __init__(self, make, model, color):
        self.__make = make
        self.__model = model
        self.__color = color

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_color(self, color):
        self.__color = color

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color


def main():
    car1 = Auto("Honda", "Civic", "Red")
    car2 = Auto("Volkswagen", "Jetta", "Gray")
    car3 = Auto("Ford", "Excursion", "Silver")

    print("\n\nCar one:  " + car1.get_make() + "\n" + car1.get_model() + "\n" + car1.get_color())
    print("\n\nCar two:  " + car2.get_make() + "\n" + car2.get_model() + "\n" + car2.get_color())
    print("\n\nCar three:  " + car3.get_make() + "\n" + car3.get_model() + "\n" + car3.get_color())


main()
