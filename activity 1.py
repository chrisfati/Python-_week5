
# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self._storage = storage  # Encapsulated attribute (protected)

    def call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, Storage: {self._storage}GB")

    def upgrade_storage(self, additional_storage):
        self._storage += additional_storage
        print(f"Storage upgraded. New storage: {self._storage}GB")


# Derived class: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, storage, gpu, cooling_system):
        super().__init__(brand, model, price, storage)
        self.gpu = gpu
        self.cooling_system = cooling_system

    def display_info(self):
        # Polymorphism: Overriding the display_info method
        super().display_info()
        print(f"GPU: {self.gpu}, Cooling System: {self.cooling_system}")

    def play_game(self, game_name):
        print(f"Launching {game_name} on {self.model} with GPU {self.gpu} and cooling system {self.cooling_system}...")


# Usage example
def main():
    # Creating a regular smartphone
    phone1 = Smartphone("Apple", "iPhone 14", 999, 128)
    phone1.display_info()
    phone1.call("+123456789")
    phone1.upgrade_storage(64)

    print("\n")

    # Creating a gaming smartphone
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 1199, 256, "Adreno 730", "Advanced Vapor Chamber")
    gaming_phone.display_info()
    gaming_phone.play_game("Genshin Impact")
    gaming_phone.send_message("+987654321", "Let's play some games!")

if __name__ == "__main__":
    main()
