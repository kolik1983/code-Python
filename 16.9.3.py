class Kalita:
    def __init__(self, clientN, ballance):
        self.clientN = clientN
        self.ballance = ballance

    def getClient(self):
        return self.clientN

    def getBlnc(self):
        return self.ballance


client1 = Kalita('Иван Петров', 500)
client2 = Kalita("Пётр Иванов", 1222)

print("Name: ", client1.getClient(), ". ", "Ballance: ", client1.getBlnc())
print("Name: ", client2.getClient(), ". ", "Ballance: ", client2.getBlnc())
