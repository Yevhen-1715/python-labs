class laptop: 
          
    def __init__(self, CPU = "4.50GHz", RAM = "128GB", company = "Hator", monitor = "144Hz", year = "2021"):
        self.__laptop_CPU = CPU
        self.__laptop_RAM = RAM
        self.__laptop_company = company
        self.laptop_monitor = monitor
        self.laptop_year = year

    def get_CPU(self):
        return self.__laptop_CPU
    def set_CPU(self, CPU):
        self.CPU = CPU

    def get_RAM(self):
        return self.__laptop_RAM
    def set_RAM(self, RAM):
        self.RAM = RAM
    
    def get_company(self):
        return self.__laptop_company
    def set_company(self, company):
        self.company = company
    
    def get_monitor(self):
        return self.laptop_monitor
    def set_monitor(self, monitor):
        self.monitor = monitor
    
    def get_year(self):
        return self.laptop_year
    def set_year(self, year):
        self.year = year

    def __repr__(self):
        return f"laptop(CPU = {self.__laptop_CPU}, RAM = {self.__laptop_RAM}, company = {self.__laptop_company}, monitor = {self.laptop_monitor}, year = {self.laptop_year})"

    def __str__(self):
        return f"CPU:{self.__laptop_CPU}, RAM:{self.__laptop_RAM}, company:{self.__laptop_company}, monitor:{self.laptop_monitor}, year:{self.laptop_year}"
    
    def __del__(self):
        print("laptop deleted")

def main():
    noytbook_0 = laptop()
    noytbook = laptop("3.90 GHz", "32GB", "Razer", "240Hz", "2020")
    noytbook_1 = laptop("4.10 GHz", "16GB", "MSI", "60Hz", "2019")
    noytbook_2 = laptop("5.20 GHz", "64GB", "Logitech", "360Hz", "2023")
    print(noytbook_0)
    print(noytbook)
    print(noytbook_1)
    print(repr(noytbook_2))
    
    

main()



class Laptop:
    def __init__(self, CPU, RAM, company):
        self.CPU = CPU
        self.RAM = RAM
        self.company = company

    def display(self):
        print(f"CPU: {self.CPU}, RAM: {self.RAM}, Company: {self.company}")

my_laptop = Laptop("3.90 GHz", "32GB", "Razer")

print(my_laptop.CPU)        
print(my_laptop.RAM)        
print(my_laptop.company)    


my_laptop.display()    
