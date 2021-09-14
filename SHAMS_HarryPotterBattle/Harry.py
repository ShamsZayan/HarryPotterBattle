from Common import Common


class Harry(Common):
    # define sub class constructor and invoking super class constructor inside it
    def __init__(self):
        Common.__init__(self)
        self.set_harry()

    # method to read harry's spells' name and power from the file and send them as parameters to set_element method
    def set_harry(self):
        with open('spells.txt') as f:
            for line in f:
                check = line.split()
                if check[0] == 'H':
                    self.set_element(check[1].lower(), int(check[2]))
