def validate_input(prompt, value_type):
    while True:
        user_input = input(prompt)
        try:
            if value_type == 'float':
                value = float(user_input)
            elif value_type == 'int':
                value = int(user_input)
            if value > 0:
                return value
            else:
                print("Value must be greater than zero.")
        except ValueError:
            print("Invalid input. Please try again.")


def book_shop_transaction():
    keep_shopping = 'Y'

    while keep_shopping.upper() == 'Y':
        total_amount = 0
        book_entry = 'Y'

        while book_entry.upper() == 'Y':
            # Asking for book price and quantity with validation
            price = validate_input("Enter the book price: ", 'float')
            quantity = validate_input("Enter the quantity: ", 'int')

            # Updating the total price
            total_amount += price * quantity

            # Ask if user wants to enter another book
            book_entry = input("Would you like to add another book? (Y/N): ")

        # Showing the total to be paid
        print(f"\nTotal Amount: ${total_amount:.2f}")
        
        payment_choice = input("Choose a payment method - Credit Card (CC), Cash (C), or Cancel (X): ").upper()

        if payment_choice == 'CC':
            print_receipt(total_amount, 0, total_amount)

        elif payment_choice == 'C':
            cash_amount = validate_input("Enter the cash tendered: ", 'float')

            if cash_amount >= total_amount:
                change_due = cash_amount - total_amount
                print_receipt(total_amount, cash_amount, 0, change_due)
            else:
                outstanding = total_amount - cash_amount
                print(f"Insufficient cash. Outstanding balance: ${outstanding:.2f}")
                secondary_choice = input("Pay the remaining amount with Credit Card (CC) or Cancel (X): ").upper()

                if secondary_choice == 'CC':
                    print_receipt(total_amount, cash_amount, outstanding)
                elif secondary_choice == 'X':
                    print("Transaction canceled.")
                else:
                    print("Invalid payment option.")
        elif payment_choice == 'X':
            print("Transaction canceled.")
        else:
            print("Invalid payment option.")

        # Ask if another customer wants to process a transaction
        keep_shopping = input("\nProcess another transaction? (Y/N): ")


def print_receipt(total, cash_paid=0, credit_paid=0, change=0):
    print("\nPurchase Summary")
    print("=" * 40)
    print(f"Total Due: ${total:.2f}")
    if cash_paid > 0:
        print(f"Cash Payment: ${cash_paid:.2f}")
    if credit_paid > 0:
        print(f"Credit Card Payment: ${credit_paid:.2f}")
    if change > 0:
        print(f"Change Given: ${change:.2f}")
    print("=" * 40)


if __name__ == "__main__":
    book_shop_transaction()
