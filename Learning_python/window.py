import tkinter as tk  # Pehle library import karein

name = input("Enter your name: ")
window = tk.Tk()      # Window banayein
window.title("Mehmood's App")
window.geometry("300x300")

label = tk.Label(window, text="Assalam-o-Alaikum! " + name)
label.pack(pady=20)

window.mainloop()     # Ye hamesha aakhir mein aata hai