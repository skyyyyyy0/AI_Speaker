 def return_change(self):
        if self.money_inserted > 0:
            print(f"Returning change is ${self.money_inserted:.2f}")
            self.money_insereted = 0.0
        else:
            print("No money inserted.")
            
def main():
    vending_machine = vendingmachine()
    
    while True:
        vending_machine.menu()
        print("\nPlease insert money or select a coffee")
        action = input("Enter money or coffee: ")
        
        try:
            amount = float(action)
            vending_machine.insert_money(amount)
        except ValueError:
            vending_machine.select_coffee(action)
        if action.lower() == "exit":
            break
    vending_machine.return_change()
    
if __name__ == "__main__":
    main()