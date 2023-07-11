import tkinter as tk
from tkcalendar import DateEntry

# Function to update the display when a new option is selected
def update_display(*args):
    selected_option = selected_var.get()
    if selected_option == "Dashboard":
        dashboard_frame.grid()
        info_frame.grid_remove()
        transaction_frame.grid_remove()
    elif selected_option == "Address data":
        dashboard_frame.grid_remove()
        info_frame.grid()
        transaction_frame.grid_remove()
    elif selected_option == "Transaction data":
        dashboard_frame.grid_remove()
        info_frame.grid_remove()
        transaction_frame.grid()
    else:
        dashboard_frame.grid_remove()
        info_frame.grid_remove()
        transaction_frame.grid_remove()

# Function to generate a .csv report
def generate_report():
    print("Generating report...")

# Function to show transaction details
def show_tx_details():
    print("Showing transaction details...")

# Create the main window
root = tk.Tk()
root.title("Bitcoin Terminal")
root.configure(bg='black')

# Create a frame for the navigation bar
navbar_frame = tk.Frame(root, bg='black')
navbar_frame.pack(side=tk.TOP, fill=tk.X)

# Add a label to represent the logo
logo_label = tk.Label(navbar_frame, text="Bitcoin Terminal", fg='orange', bg='black', font=("Courier", 16))
logo_label.pack(side=tk.RIGHT, padx=20)

# Add a horizontal line under the navigation bar
navbar_line = tk.Frame(root, bg='orange', height=1)
navbar_line.pack(side=tk.TOP, fill=tk.X)

# Create a frame for the list box and vertical line
listbox_frame = tk.Frame(root, bg='black')
listbox_frame.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a list box for the options
options_list = tk.Listbox(listbox_frame, bg='black', fg='orange', bd=0, highlightthickness=0, font=("Courier", 14))
options_list.pack(side=tk.LEFT, fill=tk.Y)

# Add a vertical line
line = tk.Frame(listbox_frame, width=1, bg='orange')
line.pack(side=tk.LEFT, fill=tk.Y)

# Add options to the list box
options = [
    "Dashboard",
    "Address data",
    "Transaction data",
    "G/L calculator",
    "Fiat conversion",
    "Price data",
    "Network stats",
    "Volatility index"
]
for option in options:
    options_list.insert(tk.END, option)

# Create a StringVar to hold the selected option
selected_var = tk.StringVar(root)
selected_var.trace("w", update_display)

# Bind the list box selection to the selected_var
options_list.bind("<<ListboxSelect>>", lambda e: selected_var.set(options_list.get(options_list.curselection())))

# Create a frame for the display and option frames
frames_frame = tk.Frame(root, bg='black')
frames_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create a frame for the dashboard
dashboard_frame = tk.Frame(frames_frame, bg='black')
dashboard_frame.grid(column=0, row=0, sticky='nsew')
dashboard_frame.configure(pady=10)  # Add padding to the bottom

# Create labels for the dashboard
btc_price_label = tk.Label(dashboard_frame, text="Bitcoin Price:", fg='orange', bg='black', font=("Courier", 14), anchor='w', justify='left')
market_cap_label = tk.Label(dashboard_frame, text="Market Capitalization:", fg='orange', bg='black', font=("Courier", 14), anchor='w', justify='left')
block_index_label = tk.Label(dashboard_frame, text="Current Block Index:", fg='orange', bg='black', font=("Courier", 14), anchor='w', justify='left')

# Layout the labels in the dashboard frame
btc_price_label.grid(column=0, row=0, sticky='nw')
market_cap_label.grid(column=0, row=1, sticky='nw')
block_index_label.grid(column=0, row=2, sticky='nw')

# Create a frame for the address data option's widgets
info_frame = tk.Frame(frames_frame, bg='black')
info_frame.grid(column=0, row=0, sticky='nsew')
info_frame.configure(pady=10)  # Add padding to the bottom

# Create the address data option's widgets
address_label = tk.Label(info_frame, text="Search for an address:", fg='orange', bg='black', font=("Courier", 14))
address_entry = tk.Entry(info_frame, width=50)
start_date_label = tk.Label(info_frame, text="Start date:", fg='orange', bg='black', font=("Courier", 14))
start_date_entry = DateEntry(info_frame)
end_date_label = tk.Label(info_frame, text="End date:", fg='orange', bg='black', font=("Courier", 14))
end_date_entry = DateEntry(info_frame)
generate_button = tk.Button(info_frame, text="Generate .csv report", command=generate_report)

# Layout the address data option's widgets
address_label.grid(column=0, row=0, sticky='e')
address_entry.grid(column=1, row=0, columnspan=3, sticky='w')
start_date_label.grid(column=0, row=1, sticky='e')
start_date_entry.grid(column=1, row=1, sticky='w')
end_date_label.grid(column=2, row=1, sticky='e')
end_date_entry.grid(column=3, row=1, sticky='w')
generate_button.grid(column=4, row=1, sticky='w')

# Create a frame for the transaction data option's widgets
transaction_frame = tk.Frame(frames_frame, bg='black')
transaction_frame.grid(column=0, row=0, sticky='nsew')
transaction_frame.configure(pady=10)  # Add padding to the bottom

# Create the transaction data option's widgets
transaction_label = tk.Label(transaction_frame, text="Search for a transaction hash:", fg='orange', bg='black', font=("Courier", 14))
transaction_entry = tk.Entry(transaction_frame, width=50)
display_button = tk.Button(transaction_frame, text="Display details", command=show_tx_details)

# Create a spacer
spacer = tk.Label(transaction_frame, bg='black', width=1)

# Layout the transaction data option's widgets
transaction_label.grid(column=0, row=0, sticky='e')
transaction_entry.grid(column=1, row=0, sticky='w')
spacer.grid(column=2, row=0)
display_button.grid(column=3, row=0, sticky='w')

# Start the main event loop
root.mainloop()
