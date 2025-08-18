import tkinter as tk
from tkinter import font

def update_task_count():
    count = task_listbox.size()
    task_count_label.config(text=f"Tasks: {count}")

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        update_task_count()

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        update_task_count()

def clear_all_tasks():
    task_listbox.delete(0, tk.END)
    update_task_count()

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for task in f:
                task_listbox.insert(tk.END, task.strip())
        update_task_count()
    except FileNotFoundError:
        pass

# Main window setup
root = tk.Tk()
root.title("🌟 Stylish To-Do List")
root.geometry("450x600")
root.configure(bg="#ffeaa7")  # Bright pastel yellow

# Custom fonts
title_font = font.Font(family="Comic Sans MS", size=20, weight="bold")
label_font = font.Font(family="Verdana", size=12)
button_font = font.Font(family="Arial", size=10, weight="bold")

# Title
title_label = tk.Label(root, text="📝 My Tasks", font=title_font, bg="#ffeaa7", fg="#2d3436")
title_label.pack(pady=15)

# Task count label
task_count_label = tk.Label(root, text="Tasks: 0", font=label_font, bg="#ffeaa7", fg="#636e72")
task_count_label.pack()

# Frame for listbox and scrollbar
frame = tk.Frame(root, bg="#ffeaa7")
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, height=15, width=40, font=("Helvetica", 12), bd=2, relief="groove",
                          yscrollcommand=scrollbar.set, selectbackground="#74b9ff", selectforeground="black")
task_listbox.pack(side=tk.LEFT)

scrollbar.config(command=task_listbox.yview)

# Load tasks from file
load_tasks()

# Entry widget
task_entry = tk.Entry(root, font=("Helvetica", 12), width=30, bd=2, relief="ridge")
task_entry.pack(pady=10)
task_entry.bind("<Return>", lambda event: add_task())

# Button frame
button_frame = tk.Frame(root, bg="#ffeaa7")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add", command=add_task, bg="#55efc4", fg="black", font=button_font, width=10)
remove_button = tk.Button(button_frame, text="Remove", command=remove_task, bg="#ff7675", fg="white", font=button_font, width=10)
clear_button = tk.Button(button_frame, text="Clear All", command=clear_all_tasks, bg="#fab1a0", fg="black", font=button_font, width=10)
save_button = tk.Button(button_frame, text="Save", command=save_tasks, bg="#81ecec", fg="black", font=button_font, width=10)

add_button.grid(row=0, column=0, padx=5, pady=5)
remove_button.grid(row=0, column=1, padx=5, pady=5)
clear_button.grid(row=1, column=0, padx=5, pady=5)
save_button.grid(row=1, column=1, padx=5, pady=5)

# Start the main loop
root.mainloop()
