import os
import shutil
import json
import tkinter as tk
from tkinter import ttk

# Function to create a new client
def create_client():
    # Get the input values from the entry fields
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    # Add the new client to the client data
    client = {
        'name': name,
        'address': address,
        'phone': phone,
        'email': email,
        'files': [],
        'notes': [],
        'encounters': []
    }
    client_data.append(client)

    # Save the client data to a file
    save_client_data(client)

    # Clear the entry fields
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    # Update the client list in the main window
    update_client_list()

# Function to save the client data to a file
def save_client_data(client):
    filename = client['name'].replace(' ', '_') + '.json'
    filepath = os.path.join(client_folder, filename)

    with open(filepath, 'w') as file:
        json.dump(client, file)

# Function to update the client list in the main window
def update_client_list():
    client_listbox.delete(0, tk.END)
    for client in client_data:
        client_listbox.insert(tk.END, client['name'])

# Function to load the client data from files in the folder
def load_client_data():
    for filename in os.listdir(client_folder):
        filepath = os.path.join(client_folder, filename)
        with open(filepath, 'r') as file:
            client = json.load(file)
            client_data.append(client)
    # Update the client list in the main window
    update_client_list()

# Function to display the selected client's data
def display_client_data(event):
    clear_data()

    # Get the selected client from the listbox
    selected_client_index = client_listbox.curselection()
    if selected_client_index:
        selected_client = client_data[selected_client_index[0]]

        # Display the client information
        name_value_label.config(text=selected_client['name'])
        address_value_label.config(text=selected_client['address'])
        phone_value_label.config(text=selected_client['phone'])
        email_value_label.config(text=selected_client['email'])

        # Display the files uploaded
        for file_data in selected_client['files']:
            file_path = file_data['file_path']
            file_label = ttk.Label(files_frame, text=file_path)
            file_label.pack(anchor='w')

        # Display the notes taken
        for note in selected_client['notes']:
            note_label = ttk.Label(notes_frame, text=note)
            note_label.pack(anchor='w')

        # Display the encounters with the assigned admin
        for encounter in selected_client['encounters']:
            encounter_label = ttk.Label(encounters_frame, text=encounter)
            encounter_label.pack(anchor='w')

# Function to clear the displayed data
def clear_data():
    name_value_label.config(text='')
    address_value_label.config(text='')
    phone_value_label.config(text='')
    email_value_label.config(text='')

    for widget in files_frame.winfo_children():
        widget.destroy()

    for widget in notes_frame.winfo_children():
        widget.destroy()

    for widget in encounters_frame.winfo_children():
        widget.destroy()

# Create the client data folder if it doesn't exist
client_folder = 'client_data'
if not os.path.exists(client_folder):
    os.makedirs(client_folder)

# Initialize the client data list
client_data = []

# Create the main window
root = tk.Tk()
root.title("Client Dashboard")

# Create a listbox to display the client names
client_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
client_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar for the client listbox
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

# Configure the scrollbar
client_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=client_listbox.yview)

# Create a frame for client creation
creation_frame = ttk.LabelFrame(root, text="Create New Client", padding=10)
creation_frame.pack(pady=10, fill='x')

# Create labels and entry fields for client information
name_label = ttk.Label(creation_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
name_entry = ttk.Entry(creation_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

address_label = ttk.Label(creation_frame, text="Address:")
address_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
address_entry = ttk.Entry(creation_frame)
address_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')

phone_label = ttk.Label(creation_frame, text="Phone:")
phone_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
phone_entry = ttk.Entry(creation_frame)
phone_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

email_label = ttk.Label(creation_frame, text="Email:")
email_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
email_entry = ttk.Entry(creation_frame)
email_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

create_button = ttk.Button(creation_frame, text="Create Client", command=create_client)
create_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create a frame for the main window
main_frame = ttk.Frame(root)
main_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Create a frame for client data display
data_frame = ttk.Frame(main_frame)
data_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

# Create labels to display the client data
name_label = ttk.Label(data_frame, text="Name:")
name_label.pack(anchor='w')
name_value_label = ttk.Label(data_frame, text='')
name_value_label.pack(anchor='w')

address_label = ttk.Label(data_frame, text="Address:")
address_label.pack(anchor='w')
address_value_label = ttk.Label(data_frame, text='')
address_value_label.pack(anchor='w')

phone_label = ttk.Label(data_frame, text="Phone:")
phone_label.pack(anchor='w')
phone_value_label = ttk.Label(data_frame, text='')
phone_value_label.pack(anchor='w')

email_label = ttk.Label(data_frame, text="Email:")
email_label.pack(anchor='w')
email_value_label = ttk.Label(data_frame, text='')
email_value_label.pack(anchor='w')

# Create a notebook widget for tabbed data display
notebook = ttk.Notebook(data_frame)
notebook.pack(fill=tk.BOTH, expand=True)

# Create frames for different tabs
files_frame = ttk.Frame(notebook)
notes_frame = ttk.Frame(notebook)
encounters_frame = ttk.Frame(notebook)

# Add the frames to the notebook
notebook.add(files_frame, text='Files Uploaded')
notebook.add(notes_frame, text='Notes Taken')
notebook.add(encounters_frame, text='Encounters')

# Set the weights of grid cells to make them expand and shrink with window size
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
data_frame.grid_rowconfigure(0, weight=1)
data_frame.grid_columnconfigure(0, weight=1)

# Load existing client data from files
load_client_data()

# Bind the display_client_data function to the ListboxSelect event
client_listbox.bind("<<ListboxSelect>>", display_client_data)

# Run the main event loop
root.mainloop()