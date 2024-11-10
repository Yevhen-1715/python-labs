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
    laptopzero = laptop()
    laptopone = laptop("3.90 GHz", "32GB", "Razer", "240Hz", "2020")
    laptopsecond = laptop("4.10 GHz", "16GB", "MSI", "60Hz", "2019")
    laptopthird = laptop("5.20 GHz", "64GB", "Logitech", "360Hz", "2023")
    print(laptopzero)
    print(laptopone)
    print(laptopsecond)
    print(repr(laptopthird))
main()
