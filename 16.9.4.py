class Volunteer:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def getName(self):
        return self.name

    def getCity(self):
        return self.city

    def getStatus(self):
        return self.status


part1 = Volunteer("Spartak Maratovich", "Moskow", "mentor")
part2 = Volunteer("Никола Тесла", "NY", "sientist")

print(part1.getName(), part1.getCity(), " статус ", part1.getStatus())
print(part2.getName(), part2.getCity(), "статус ", part2.getStatus())