import tkinter as tk
from tkinter import ttk

exchange_rates = {
    'USD': {'INR': 83.3, 'EUR': 0.92},
    'INR': {'USD': 0.012, 'EUR': 0.011},
    'EUR': {'USD': 1.09, 'INR': 90.5},
}

def convert():
    try:
        amount = float(entry_amount.get())
        from_curr = combo_from.get()
        to_curr = combo_to.get()
        rate = exchange_rates[from_curr][to_curr]
        result = amount * rate
        label_result.config(text=f"{amount} {from_curr} = {result:.2f} {to_curr}")
    except:
        label_result.config(text="Invalid input or conversion not supported")

root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount:").grid(row=0, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

tk.Label(root, text="From:").grid(row=1, column=0)
combo_from = ttk.Combobox(root, values=list(exchange_rates.keys()))
combo_from.grid(row=1, column=1)

tk.Label(root, text="To:").grid(row=2, column=0)
combo_to = ttk.Combobox(root, values=list(exchange_rates.keys()))
combo_to.grid(row=2, column=1)

btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="Result will appear here")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()
