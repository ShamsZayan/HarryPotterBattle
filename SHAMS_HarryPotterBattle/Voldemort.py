from Common import Common


class Voldemort(Common):
    def __init__(self):
        Common.__init__(self)
        self.set_voldemort()

    # method to read voldemort's spells' name and power from the file and send them as parameters to set_element method
    def set_voldemort(self):
        with open('spells.txt') as f:
            for line in f:
                check = line.split()
                if check[0] == 'V':
                    self.set_element(check[1].lower(), int(check[2]))
