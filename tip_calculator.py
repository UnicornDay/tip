def main():
    print("=== Tip Calculator ===\n")

    try:
        total_bill = float(input("Enter total bill amount: $"))
        tip_percent = float(input("Enter tip percentage (e.g., 15, 20): "))
        num_people = int(input("Enter number of people splitting: "))

        if total_bill < 0 or tip_percent < 0 or num_people <= 0:
            print("Please enter positive values.")
            return

        tip_amount = total_bill * (tip_percent / 100)
        total_with_tip = total_bill + tip_amount
        per_person = total_with_tip / num_people

        print("\n=== Results ===")
        print(f"Bill amount:      ${total_bill:.2f}")
        print(f"Tip ({tip_percent}%):         ${tip_amount:.2f}")
        print(f"Total with tip:   ${total_with_tip:.2f}")
        print(f"Split {num_people} ways:     ${per_person:.2f} each")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    main()