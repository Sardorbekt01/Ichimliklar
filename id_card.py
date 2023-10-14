class SotuvMashinasi:
    def __init__(self):
        self.mashina = []

    def refillColumn(self, ustun_raqami, ichimlik_nomi, bankalar_soni):
        self.mashina.append({
            "Ustun_raqami": ustun_raqami,
            "Ichimlik_nomi": ichimlik_nomi,
            "Bankalar_soni": bankalar_soni
        })

    def availableCans(self, ichimlik_nomi):
        total_cans = 0
        for ustun in self.mashina:
            if ustun["Ichimlik_nomi"] == ichimlik_nomi:
                total_cans += ustun["Bankalar_soni"]
        return total_cans

# Mashinani yarating
mashina = SotuvMashinasi()

# Ustunlarni to'ldirish
mashina.refillColumn(1, "Coca Cola", 1)
mashina.refillColumn(2, "Suv", 10)
mashina.refillColumn(3, "Pepsi", 15)
mashina.refillColumn(4, "Suv", 20)

# Berilgan ichimlikdan nechta borligini aniqlash
ichimlik_nomi = "Suv"
borlik_soni = mashina.availableCans(ichimlik_nomi)
print(f"{ichimlik_nomi} ichimligi {borlik_soni} ta bor.")
