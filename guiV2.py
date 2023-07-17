import os
import shutil
from tkinter import *
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

    # Clear the entry fields
    name_entry.delete(0, END)
    address_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)

    # Update the client list in the main window
    update_client_list()

# Function to update the client list in the main window
def update_client_list():
    client_listbox.delete(0, END)
    for client in client_data:
        client_listbox.insert(END, client['name'])

# Function to display the selected client's data
def display_client_data(event):
    # Clear the existing data
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
            file_label = Label(files_frame, text=file_path)
            file_label.pack(anchor=W)

        # Display the notes taken
        for note in selected_client['notes']:
            note_label = Label(notes_frame, text=note)
            note_label.pack(anchor=W)

        # Display the encounters with the assigned admin
        for encounter in selected_client['encounters']:
            encounter_label = Label(encounters_frame, text=encounter)
            encounter_label.pack(anchor=W)

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

# Initialize the client data list
client_data = []

# Create the main window
root = Tk()
root.title("Client Dashboard")

# Create a frame for client creation
creation_frame = LabelFrame(root, text="Create New Client")
creation_frame.pack(pady=10)

# Create labels and entry fields for client information
name_label = Label(creation_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
name_entry = Entry(creation_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

address_label = Label(creation_frame, text="Address:")
address_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
address_entry = Entry(creation_frame)
address_entry.grid(row=1, column=1, padx=5, pady=5)

phone_label = Label(creation_frame, text="Phone:")
phone_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
phone_entry = Entry(creation_frame)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

email_label = Label(creation_frame, text="Email:")
email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
email_entry = Entry(creation_frame)
email_entry.grid(row=3, column=1, padx=5, pady=5)

create_button = Button(creation_frame, text="Create Client", command=create_client)
create_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create a frame for the main window
main_frame = Frame(root)
main_frame.pack(pady=10)

# Create a listbox to display the client names
client_listbox = Listbox(main_frame, selectmode=SINGLE)
client_listbox.pack(side=LEFT, fill=Y)
client_listbox.bind("<<ListboxSelect>>", display_client_data)

# Create a scrollbar for the client listbox
scrollbar = Scrollbar(main_frame)
scrollbar.pack(side=LEFT, fill=Y)

# Configure the scrollbar
client_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=client_listbox.yview)

# Create a frame for client data display
data_frame = Frame(main_frame)
data_frame.pack(side=LEFT, padx=10)

# Create labels to display the client data
name_label = Label(data_frame, text="Name:")
name_label.pack(anchor=W)
name_value_label = Label(data_frame, text='')
name_value_label.pack(anchor=W)

address_label = Label(data_frame, text="Address:")
address_label.pack(anchor=W)
address_value_label = Label(data_frame, text='')
address_value_label.pack(anchor=W)

phone_label = Label(data_frame, text="Phone:")
phone_label.pack(anchor=W)
phone_value_label = Label(data_frame, text='')
phone_value_label.pack(anchor=W)

email_label = Label(data_frame, text="Email:")
email_label.pack(anchor=W)
email_value_label = Label(data_frame, text='')
email_value_label.pack(anchor=W)

# Create a notebook widget for tabbed data display
notebook = ttk.Notebook(data_frame)
notebook.pack(fill=BOTH, expand=True)

# Create frames for different tabs
files_frame = Frame(notebook)
notes_frame = Frame(notebook)
encounters_frame = Frame(notebook)

# Add the frames to the notebook
notebook.add(files_frame, text='Files Uploaded')
notebook.add(notes_frame, text='Notes Taken')
notebook.add(encounters_frame, text='Encounters')

# Run the main event loop
root.mainloop()
