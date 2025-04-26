"""import os
import tkinter as tk
from tkinter import messagebox

def shutdown_app_mac(app_name: str) -> None:
    if not app_name.strip():
        messagebox.showwarning("Warning", "Please enter an application name.")
        return
    try:
        result = os.system(f"killall '{app_name}'")
        if result == 0:
            messagebox.showinfo("Success", f"{app_name} has been shut down successfully.")
        else:
            messagebox.showerror("Error", f"Could not find or close {app_name}.")
    except Exception as e:
        messagebox.showerror("Error", f"Error shutting down {app_name}: {e}")

def on_shutdown_click():
    shutdown_button.config(bg="#ff5555")  # Animation: Button color flash
    root.after(150, lambda: shutdown_button.config(bg="#ff4444"))  # Back to normal
    app_name = entry_app_name.get()
    shutdown_app_mac(app_name)

def on_enter(e):
    shutdown_button.config(bg="#ff6666")  # Lighter red on hover

def on_leave(e):
    shutdown_button.config(bg="#ff4444")  # Normal color

# Create window
root = tk.Tk()
root.title("Mac App Killer 🔥")
root.geometry("400x250")
root.configure(bg="#2e2e2e")
root.resizable(False, False)

# Label
label = tk.Label(root, text="Enter Application Name:", font=("Helvetica", 14, "bold"), bg="#2e2e2e", fg="white")
label.pack(pady=20)

# Entry
entry_app_name = tk.Entry(root, width=30, font=("Helvetica", 13), bg="#3e3e3e", fg="white", insertbackground='white', relief="flat")
entry_app_name.pack(pady=10)

# Button
shutdown_button = tk.Button(root, text="Shutdown App", font=("Helvetica", 13, "bold"),
                            bg="#ff4444", fg="white", relief="flat", padx=10, pady=5,
                            activebackground="#ff2222", activeforeground="white",
                            command=on_shutdown_click)
shutdown_button.pack(pady=30)

# Hover effect
shutdown_button.bind("<Enter>", on_enter)
shutdown_button.bind("<Leave>", on_leave)

# Run
root.mainloop()
"""

from tkinter import *
import os
from turtle import title
def restart():
    os.system("shutdown/r/t 1")

def restart_time():
    os.system("shutdown/r/t 20")

def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown/s/t 1")


st=Tk()
st,title("Shutdown App")
st.geometry("500x500")
st.config(bg="Black")

r_button=Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button=Button(st,text="Restart with Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button=Button(st,text="Log Out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

sd_button=Button(st,text="Shut Down",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="Plus",command=shutdown)
sd_button.place(x=150,y=370,height=50,width=200)


st.mainloop()