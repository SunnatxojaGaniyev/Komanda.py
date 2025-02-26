import json
import os

class ShoppingCart:
    def __init__(self):
        self.cart = {}
        self.load_cart()
        pass



 def add_product(self, name, price, quantity=1):
        if name in self.cart:
            self.cart[name]['quantity'] += quantity
        else:
            self.cart[name] = {'price': price, 'quantity': quantity}
        print(f"{quantity} ta {name} savatga qo'shildi.")
        self.save_cart()
    def remove_product(self, name):
        if name in self.cart:
            del self.cart[name]
            print(f"{name} savatdan olib tashlandi.")
            self.save_cart() 
        else:
            print(f"{name} savatda yo'q!")

    def view_cart(self):
        if not self.cart:
            print("\n🛒 Savat bo'sh.")
        else:
            print("\n📌 Savat tarkibi:")
            for name, details in self.cart.items():
                print(f"{name} - {details['quantity']} dona - {details['price']} $")
            print(f"💰 Jami: {self.total_price()} $\n")




    def total_price(self):
        return sum(details['price'] * details['quantity'] for details in self.cart.values())

    def save_cart(self):
        """Savatni JSON faylga saqlaydi"""
        with open("cart.json", "w") as file:
            json.dump(self.cart, file)
    
    def load_cart(self):
        """Dastur ishga tushganda savatni fayldan yuklaydi"""
        if os.path.exists("cart.json"):
            with open("cart.json", "r") as file:
                try:
                    self.cart = json.load(file)
                except json.JSONDecodeError:
                    self.cart = {}

def main():
    cart = ShoppingCart()

    while True:
        print("\n1️⃣ Mahsulot qo'shish")
        print("2️⃣ Savatni ko'rish")
        print("3️⃣ Mahsulotni olib tashlash")
        print("4️⃣ Chiqish")
        choice = input("Tanlang (1-4): ")

        if choice == "1":
            name = input("Mahsulot nomi: ")
            price = int(input("Narxi: "))
            quantity = int(input("Soni: "))
            cart.add_product(name, price, quantity)

        elif choice == "2":
            cart.view_cart()

        elif choice == "3":
            name = input("Olib tashlamoqchi bo'lgan mahsulot nomi: ")
            cart.remove_product(name)

        elif choice == "4":
            print("Savat saqlandi. ✅ Dastur tugatildi.")
            break

        else:
            print("❌ Noto‘g‘ri tanlov! Qaytadan urinib ko‘ring.")

if __name__ == "__main__":
    main()
