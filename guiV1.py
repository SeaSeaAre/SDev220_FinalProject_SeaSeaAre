import os
import shutil
from tkinter import *
from tkinter import ttk

# Function to retrieve client data from text or email
def retrieve_client_data():
    # code to retrieve client data goes here
    # involve interacting with text or email APIs/services
    # Extract relevant client information, file paths, date, time, evidence, and notes
    
    # Assumed following client data
    client_data = [
        {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'phone': '1234567890',
            'files': [
                {
                    'file_path': '/path/to/file1.txt',
                    'date': '2023-07-10',
                    'time': '14:30:00',
                    'evidence': 'Evidence 1',
                    'notes': 'Notes 1'
                },
                {
                    'file_path': '/path/to/file2.pdf',
                    'date': '2023-07-11',
                    'time': '10:45:00',
                    'evidence': 'Evidence 2',
                    'notes': 'Notes 2'
                }
            ]
        },
        {
            'name': 'Jane Smith',
            'email': 'janesmith@example.com',
            'phone': '9876543210',
            'files': [
                {
                    'file_path': '/path/to/file3.docx',
                    'date': '2023-07-09',
                    'time': '09:15:00',
                    'evidence': 'Evidence 3',
                    'notes': 'Notes 3'
                },
                {
                    'file_path': '/path/to/file4.png',
                    'date': '2023-07-12',
                    'time': '16:20:00',
                    'evidence': 'Evidence 4',
                    'notes': 'Notes 4'
                }
            ]
        }
    ]
    
    return client_data

# Function to handle client selection
def client_selected(event):
    # Clear the existing data
    clear_data()

    # Get the selected client from the combobox
    selected_client = client_combobox.get()

    # Find the client data based on the selected client
    for client in client_data:
        if client['name'] == selected_client:
            # Display the files received from the client
            for file_data in client['files']:
                file_path = file_data['file_path']
                date = file_data['date']
                time = file_data['time']
                evidence = file_data['evidence']
                notes = file_data['notes']

                files_text.insert(END, f"File: {file_path}\n")
                files_text.insert(END, f"Date: {date}\n")
                files_text.insert(END, f"Time: {time}\n")
                files_text.insert(END, f"Evidence: {evidence}\n")
                files_text.insert(END, f"Notes: {notes}\n\n")

# Function to clear the displayed data
def clear_data():
    files_text.delete(1.0, END)

# Retrieve client data
client_data = retrieve_client_data()

# Create the main window
root = Tk()
root.title("Client Data Management")

# Create a combobox to display client names
client_combobox = ttk.Combobox(root, values=[client['name'] for client in client_data])
client_combobox.bind("<<ComboboxSelected>>", client_selected)
client_combobox.pack=10 #Create a text widget to display the files received from the client
files_text = Text(root, height=10, width=50)
files_text.pack()

# Run the main event loop
root.mainloop()
