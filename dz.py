import tkinter as tk
import requests
import json

def fetch_data():
        post_id = int(entry.get())
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        data = response.json()
        with open("data.json", "w") as file:
            json.dump(data, file)
        result_label.config(text="Data saved successfully!")

root = tk.Tk()
root.title("JSONPlaceholder Data Fetcher")

frame = tk.Frame(root)
frame.pack()
label = tk.Label(frame, text="Enter post ID:")
label.grid(row=0, column=0)
entry = tk.Entry(frame)
entry.grid(row=0, column=1)
fetch_button = tk.Button(frame, text="Fetch Data", command=fetch_data)
fetch_button.grid(row=1)
result_label = tk.Label(frame, text="")
result_label.grid(row=2)

root.mainloop()
