class laptop: 
          
    def __init__(self, CPU = "4.50GHz", RAM = "128GB", company = "Hator"):
        self.laptop_CPU = CPU
        self.laptop_RAM = RAM
        self.laptop_company = company
    def get_CPU(self):
        return self.laptop_CPU
    
    def get_RAM(self):
        return self.laptop_RAM

    def get_company(self):
        return self.laptop_company

    def __repr__(self):
        return f"laptop(CPU = {self.laptop_CPU}, RAM = {self.laptop_RAM}, company = {self.laptop_company})"

    def __str__(self):
        return f"CPU:{self.laptop_CPU}, RAM:{self.laptop_RAM}, company:{self.laptop_company}"

noytbook = laptop("3.90 GHz", "32GB", "Razer")
noytbook_1 = laptop("4.10 GHz", "16GB", "Hator")
noytbook_2 = laptop("5.20 GHz", "64GB", "Logitech")
print(noytbook)
print(repr(noytbook))
print(noytbook_1)
print(repr(noytbook_1))
print(noytbook_2)
print(repr(noytbook_2))







