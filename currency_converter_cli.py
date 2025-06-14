exchange_rates = {
    'USD': {'INR': 83.3, 'EUR': 0.92},
    'INR': {'USD': 0.012, 'EUR': 0.011},
    'EUR': {'USD': 1.09, 'INR': 90.5},
}

def convert_currency(amount, from_curr, to_curr):
    try:
        rate = exchange_rates[from_curr][to_curr]
        return amount * rate
    except KeyError:
        print("Conversion rate not available.")
        return None

def main():
    print("Currency Converter")
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (e.g., USD, INR, EUR): ").upper()
    to_curr = input("To currency (e.g., USD, INR, EUR): ").upper()

    converted = convert_currency(amount, from_curr, to_curr)
    if converted is not None:
        print(f"{amount} {from_curr} = {converted:.2f} {to_curr}")

if __name__ == "__main__":
    main()
