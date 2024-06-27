import requests
import tkinter as tk
from tkinter import messagebox

def send_message(webhook_url, message):
    headers = {'Content-Type': 'application/json'}
    payload = {'content': message}
    response = requests.post(webhook_url, headers=headers, json=payload)

def send_button_clicked():
    webhook_url = webhook_url_entry.get()
    message = message_entry.get()
    send_message(webhook_url, message)

root = tk.Tk()
root.title("Discord Webhook App")
root.geometry("400x200")

webhook_url_label = tk.Label(root, text="Webhook URL:")
webhook_url_label.pack()

webhook_url_entry = tk.Entry(root)
webhook_url_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()

message_entry = tk.Entry(root)
message_entry.pack()

send_button = tk.Button(root, text="Send", command=send_button_clicked)
send_button.pack()

root.mainloop()
