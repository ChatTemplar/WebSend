import requests
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def send_message(webhook_url, message):
    headers = {'Content-Type': 'application/json'}
    payload = {'content': message}
    response = requests.post(webhook_url, headers=headers, json=payload)
    response.raise_for_status()

def send_button_clicked():
    webhook_url = webhook_entry.get().strip()
    message = message_box.get("1.0", "end").strip()

    if not webhook_url or not message:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        send_message(webhook_url, message)
        messagebox.showinfo("Success", "Message sent!")
        message_box.delete("1.0", "end")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main window
app = ctk.CTk()
app.title("Discord Webhook Sender")
app.geometry("460x320")
app.resizable(False, False)

# Main frame (rounded)
frame = ctk.CTkFrame(
    app,
    corner_radius=20,
    fg_color="#0f172a"  # deep blue
)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Title
title = ctk.CTkLabel(
    frame,
    text="Discord Webhook",
    font=ctk.CTkFont(size=20, weight="bold"),
    text_color="#60a5fa"
)
title.pack(pady=(10, 20))

# Webhook entry
webhook_entry = ctk.CTkEntry(
    frame,
    placeholder_text="Webhook URL",
    height=40,
    corner_radius=10,
    border_width=2,
    border_color="#1e3a8a"
)
webhook_entry.pack(fill="x", padx=20, pady=(0, 15))

# Message box
message_box = ctk.CTkTextbox(
    frame,
    height=90,
    corner_radius=10,
    border_width=2,
    border_color="#1e3a8a"
)
message_box.pack(fill="x", padx=20, pady=(0, 20))

# Send button
send_button = ctk.CTkButton(
    frame,
    text="Send Message",
    height=40,
    corner_radius=12,
    fg_color="#1d4ed8",
    hover_color="#2563eb",
    command=send_button_clicked
)
send_button.pack(padx=20, pady=(0, 15), anchor="e")

app.mainloop()
