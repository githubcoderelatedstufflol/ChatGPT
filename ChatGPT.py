import tkinter as tk
from uuid import uuid4

def send_message():
    message = input_box.get()
    if message.strip():
        guid = str(uuid4())
        history_box.insert(tk.END, "You: " + input_box.get() + '\n')
        history_box.insert(tk.END, "ChatGPT: " + guid + '\n')
        input_box.delete(0, tk.END)

root = tk.Tk()
root.title("Chat App")

# Create input box
input_box = tk.Entry(root, width=40)
input_box.pack(pady=10)

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Create history box
history_box = tk.Text(root, width=40, height=10)
history_box.pack(padx=10, pady=10)

root.mainloop()
