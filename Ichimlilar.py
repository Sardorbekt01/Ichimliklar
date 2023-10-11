class Ichimlik:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

class VendingMachine:
    def __init__(self):
        self.ichimliklar = []

    def addBeverage(self, ichimlik):
        self.ichimliklar.append(ichimlik)

    def getPrice(self, nomi):
        for ichimlik in self.ichimliklar:
            if ichimlik.nomi == nomi:
                return ichimlik.narxi
        return -1.0


ichimlik1 = Ichimlik("Coca Cola", 3200)
ichimlik2 = Ichimlik("Suv", 1000)
ichimlik3 = Ichimlik("Pepsi", 2500)


avtomat = VendingMachine()


avtomat.addBeverage(ichimlik1)
avtomat.addBeverage(ichimlik2)
avtomat.addBeverage(ichimlik3)

# Ichimliklar narxini tekshiramiz
nomi = "Coca Cola"
narxi = avtomat.getPrice(nomi)
if narxi != -1.0:
    print(f"{nomi} narxi: {narxi}")
else:
    print(f"{nomi} mavjud emas")

nomi = "Pepsi"
narxi = avtomat.getPrice(nomi)
if narxi != -1.0:
    print(f"{nomi} narxi: {narxi}")
else:
    print(f"{nomi} mavjud emas")

nomi = "Sprite"
narxi = avtomat.getPrice(nomi)
if narxi != -1.0:
    print(f"{nomi} narxi: {narxi}")
else:
    print(f"{nomi} mavjud emas")
