from oop import PartyAnimal

class CriketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points += 6
        self.party()
        print(self.name, "points:", self.points)

t = PartyAnimal("Tiago")
t.party()
j = CriketFan("Jim")
j.party()
j.six()
print(dir(j))
