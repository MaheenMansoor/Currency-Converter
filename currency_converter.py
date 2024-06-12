import tkinter as tk

def currency_converter():
    exchange_rates = {
        'USD': {'INR': 74.57, 'EUR': 0.84, 'GBP': 0.73, 'PKR': 180.0},
        'INR': {'USD': 0.013, 'EUR': 0.011, 'GBP': 0.0098, 'PKR': 2.0},
        'EUR': {'USD': 1.19, 'INR': 88.39, 'GBP': 0.86, 'PKR': 160.0},
        'GBP': {'USD': 1.37, 'INR': 102.91, 'EUR': 1.17, 'PKR': 200.0},
        'PKR': {'USD': 0.006, 'INR': 0.50, 'EUR': 0.0063, 'GBP': 0.005}
    }
    
    from_currency = from_currency_var.get().upper()
    to_currency = to_currency_var.get().upper()
    amount = float(amount_var.get())

    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        conversion_rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * conversion_rate
        result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

        # Save conversion history to file
        with open("conversion_history.txt", "a") as file:
            file.write(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}\n")

    else:
        result_label.config(text="Invalid currency code or conversion not supported.")

def show_history():
    try:
        with open("conversion_history.txt", "r") as file:
            history_window = tk.Toplevel()
            history_window.title("Conversion History")

            history_text = tk.Text(history_window, height=10, width=50)
            history_text.pack()

            for line in file:
                history_text.insert(tk.END, line)

            history_text.config(state="disabled")

    except FileNotFoundError:
        result_label.config(text="No conversion history found.")

# Create GUI
root = tk.Tk()
root.title("Currency Converter")
root.configure(bg='#EAF6FF')  # Light blue background color

from_currency_var = tk.StringVar()
from_currency_label = tk.Label(root, text="Select From Currency:", font=("Arial", 14), bg='#EAF6FF')  # Light blue background color
from_currency_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

from_currency_options = ['USD', 'INR', 'EUR', 'GBP', 'PKR']
from_currency_var.set(from_currency_options[0])  # Set default option
from_currency_menu = tk.OptionMenu(root, from_currency_var, *from_currency_options)
from_currency_menu.config(font=("Arial", 14))
from_currency_menu.grid(row=0, column=1, padx=10, pady=10, sticky="w")

to_currency_var = tk.StringVar()
to_currency_label = tk.Label(root, text="Select To Currency:", font=("Arial", 14), bg='#EAF6FF')  # Light blue background color
to_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

to_currency_options = ['USD', 'INR', 'EUR', 'GBP', 'PKR']
to_currency_var.set(to_currency_options[1])  # Set default option
to_currency_menu = tk.OptionMenu(root, to_currency_var, *to_currency_options)
to_currency_menu.config(font=("Arial", 14))
to_currency_menu.grid(row=1, column=1, padx=10, pady=10, sticky="w")

amount_var = tk.StringVar()
amount_label = tk.Label(root, text="Enter Amount:", font=("Arial", 14), bg='#EAF6FF')  # Light blue background color
amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

amount_entry = tk.Entry(root, textvariable=amount_var, font=("Arial", 14))
amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

convert_button = tk.Button(root, text="Convert", command=currency_converter, font=("Arial", 14), bg='#3498DB', fg='white')  # Blue button with white text
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg='#EAF6FF')  # Light blue background color
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

history_button = tk.Button(root, text="View History", command=show_history, font=("Arial", 14), bg='#3498DB', fg='white')  # Blue button with white text
history_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Center-align widgets
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
