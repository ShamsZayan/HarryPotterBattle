class Common:
    # set  default values for instance attributes (health ,energy and shields) inside the super class constructor
    def __init__(self):
        self.__health = 100
        self.__energy = 500
        self.__shield = 3
        self.__comm = {}
        self.set_comm()

    # defining setters and getters for private instance attributes

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_energy(self):
        return self.__energy

    def set_energy(self, energy):
        self.__energy = energy

    def get_shield(self):
        return self.__shield

    def set_shield(self, shield):
        self.__shield = shield

    def get_comm(self):
        return self.__comm

    # method to add new elements to the dictionary as it is private instance attributes
    def set_element(self, key, value):
        self.__comm[key] = value

    # method to read the common spells' name and power from the file and add them to dictionary
    def set_comm(self):
        with open('spells.txt') as f:
            for line in f:
                check = line.split()
                if check[0] == 'A':
                    self.__comm[check[1].lower()] = int(check[2])
