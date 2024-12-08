from src.hardware.brewer import BrewerInterface
from src.hardware.creditcard import CreditCardInterface, CardHandleInterface

class Brewer(BrewerInterface):
    def make_a_coffee(self) -> bool:
        # Implementation of making a coffee
        print("Brewing coffee...")
        return True
    
    def try_pull_water(self) -> bool:
        # Implementation to pull water
        return True

    def pour_milk(self) -> bool:
        # Implementation to pour milk
        return True

    def pour_water(self) -> bool:
        # Implementation to pour water
        return True

    def pour_sugar(self) -> bool:
        # Implementation to pour sugar
        return True

    def pour_chocolate(self) -> bool:
        # Implementation to pour chocolate
        return True

class CreditCardHandler(CardHandleInterface):
    def try_charge_amount(self, amount_in_cents: int) -> bool:
        # Implementation to charge amount
        print(f"Charging {amount_in_cents} cents to the card.")
        return True

    def refund(self, amount_in_cents: int) -> None:
        # Implementation to refund amount
        print(f"Refunding {amount_in_cents} cents to the card.")

class CreditCard(CreditCardInterface):
    def register_card_detected_callback(self, card_detected_callback: CardHandleInterface = None) -> None:
        # Implementation to register card detected callback
        if card_detected_callback:
            print("Credit card detected.")
            amount = 50  # 50 cents
            if card_detected_callback.try_charge_amount(amount):
                brewer = Brewer()
                if brewer.make_a_coffee():
                    print("Coffee brewed successfully.")
                else:
                    card_detected_callback.refund(amount)
                    print("Failed to brew coffee. Amount refunded.")
            else:
                print("Failed to charge card.")

def main():
    credit_card = CreditCard()
    card_handler = CreditCardHandler()
    credit_card.register_card_detected_callback(card_handler)

if __name__ == "__main__":
    main()