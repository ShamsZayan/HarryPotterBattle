
from Harry import Harry
from Voldemort import Voldemort

if __name__ == '__main__':
    # creating objects from Harry and Voldemort subclasses
    harry = Harry()
    voldemort = Voldemort()
    # checking if their health greater than 0 or not to know if the war end or not
    while harry.get_health() > 0 and voldemort.get_health() > 0:
        # reading input from console
        h_spell, v_spell = input("Enter the two spells (harry then voldemort):\n ").split()
        # turn input into lower case to match the dictionary keys
        h_spell = h_spell.lower()
        v_spell = v_spell.lower()
        # check if input spell included in the recorded spells or not and if not the user will write the input again
        while harry.get_comm().get(h_spell) is None or voldemort.get_comm().get(v_spell) is None:
            h_spell, v_spell = input("ERROR! Enter the two spells again (harry then voldemort):\n ").split()
            h_spell = h_spell.lower()
            v_spell = v_spell.lower()
        # cases to handle the changing in wizards' health and energy in each round
        # if spells' power are equal
        if harry.get_comm()[h_spell] == voldemort.get_comm()[v_spell]:
            harry.set_energy(harry.get_energy() - harry.get_comm()[h_spell])
            voldemort.set_energy(voldemort.get_energy() - voldemort.get_comm()[v_spell])
        # if harry's spell more powerful than voldemort's spell or voldemort's shields are vanished
        elif (harry.get_comm()[h_spell] > voldemort.get_comm()[v_spell] > 0) or (voldemort.get_comm()[v_spell] == 0 and voldemort.get_shield() <= 0):
            harry.set_energy(harry.get_energy() - harry.get_comm()[h_spell])
            voldemort.set_energy(voldemort.get_energy() - voldemort.get_comm()[v_spell])
            voldemort.set_health(voldemort.get_health() - (harry.get_comm()[h_spell] - voldemort.get_comm()[v_spell]))
        # if voldemort's spell more powerful than harry's spell or harry's shields are vanished
        elif (voldemort.get_comm()[v_spell] > harry.get_comm()[h_spell] > 0) or (harry.get_comm()[h_spell] == 0 and harry.get_shield() <= 0):
            harry.set_energy(harry.get_energy() - harry.get_comm()[h_spell])
            voldemort.set_energy(voldemort.get_energy() - voldemort.get_comm()[v_spell])
            harry.set_health(harry.get_health() - (voldemort.get_comm()[v_spell] - harry.get_comm()[h_spell]))
        # if harry has shields
        if harry.get_comm()[h_spell] == 0 and harry.get_shield() > 0:
            voldemort.set_energy(voldemort.get_energy() - voldemort.get_comm()[v_spell])
            harry.set_shield(harry.get_shield() - 1)
        # if voldemort has shields
        if voldemort.get_comm()[v_spell] == 0 and voldemort.get_shield() > 0:
            harry.set_energy(harry.get_energy() - harry.get_comm()[h_spell])
            voldemort.set_shield(voldemort.get_shield() - 1)
        # wizard's health couldn't be less than 0 even if the power difference bigger than the health so in these case health will be added as 0
        if harry.get_health() < 0:
            harry.set_health(0)

        if voldemort.get_health() < 0:
            voldemort.set_health(0)
        # printing the wizards' new health and energy in each round
        print("         Harry   Voldemort\n")
        print("Health : ", harry.get_health(),  voldemort.get_health(), "\n")
        print("Energy : ", harry.get_energy(),  voldemort.get_energy(), "\n")
    # printing who is the winner
    if harry.get_health() > 0 and voldemort.get_health() == 0:
        print("Harry is the winner")
    elif voldemort.get_health() > 0 and harry.get_health() == 0:
        print("Voldemort is the winner")
    elif voldemort.get_health() == 0 and harry.get_health() == 0:
        print("No winner")
