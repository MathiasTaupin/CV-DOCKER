import tkinter as tk
from tkinter import messagebox
import random
import threading
import time
import webbrowser
import platform
import ctypes

click_count = 0
MOUSE_PRANK = True  # True pour ralentir la souris (Windows uniquement)

# Liste des sites bidons
all_sites = [
    "https://www.pouletmignon.fr",
    "https://youtube.com/watch?v=dQw4w9WgXcQ",
    "https://lessecretsdememo.fr",
    "https://tropdrôle123.biz",
    "https://piratezone.darkweb",
    "https://tiktok.com/@mecchelou",
    "https://chat-des-enfers.io",
    "https://darkbanane.fr",
    "https://jeveuxdufromage.org",
    "https://pastèque-express.net",
    "https://hacker-coco.com",
    "https://tuto-hack-ps3.biz"
]

twitch_url = "null"

def show_history_and_countdown():
    history_win = tk.Toplevel()
    history_win.attributes("-fullscreen", True)
    history_win.configure(bg="black")

    title = tk.Label(history_win, text="Historique détecté :", font=("Arial", 30), fg="red", bg="black")
    title.pack(pady=50)

    history = random.sample(all_sites, k=random.randint(5, min(10, len(all_sites))))

    for site in history:
        link = tk.Label(history_win, text=site, font=("Courier", 20), fg="lightblue", bg="black", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e, url=twitch_url: webbrowser.open(url))

    countdown_label = tk.Label(history_win, text="Fermeture dans 60 secondes...", font=("Arial", 18), fg="white", bg="black")
    countdown_label.pack(pady=50)

    def countdown():
        for i in range(59, -1, -1):
            countdown_label.config(text=f"Fermeture dans {i} secondes...")
            time.sleep(1)
        reset_mouse_speed()
        root.destroy()

    threading.Thread(target=countdown, daemon=True).start()

def moral_message():
    global click_count
    click_count += 1
    check_for_bsod()
    messagebox.showinfo("Leçon",
        "Il ne faut jamais télécharger de fichiers sans connaître leur provenance.\n"
        "Ça peut contenir des virus ou mettre en danger ton ordinateur !\n"
        "Reste vigilant 😉")
    show_history_and_countdown()

def evade_mouse(event, button):
    new_x = random.randint(0, root.winfo_width() - 100)
    new_y = random.randint(0, root.winfo_height() - 50)
    button.place(x=new_x, y=new_y)

def create_new_non_button():
    global click_count
    click_count += 1
    check_for_bsod()
    new_button = tk.Button(root, text="Non", bg="gray", fg="white", font=("Arial", 12), cursor="pirate")
    new_button.place(x=random.randint(0, root.winfo_width() - 100), y=random.randint(0, root.winfo_height() - 50))
    new_button.bind("<Enter>", lambda e: evade_mouse(e, new_button))
    new_button.config(command=create_new_non_button)

def on_close():
    spawn_new_window()

def reset_mouse_speed():
    if platform.system() == "Windows":
        SPI_SETMOUSESPEED = 0x0071
        default_speed = 10  # valeur par défaut Windows
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETMOUSESPEED, 0, default_speed, 0)

def emergency_exit(event=None):
    reset_mouse_speed()
    root.destroy()

def spawn_new_window():
    new = tk.Tk()
    new.title("Oops...")
    new.attributes("-fullscreen", True)
    new.configure(bg="black")

    label = tk.Label(new, text="I've been hacked", font=("Arial", 40), fg="red", bg="black")
    label.pack(pady=100)

    oui = tk.Button(new, text="Oui", command=lambda: [moral_message(), new.destroy()], bg="green", fg="white", font=("Arial", 18), cursor="pirate")
    oui.place(x=500, y=400)

    non = tk.Button(new, text="Non", bg="gray", fg="white", font=("Arial", 18), cursor="pirate")
    non.place(x=800, y=400)
    non.bind("<Enter>", lambda e: evade_mouse(e, non))
    non.config(command=create_new_non_button)

    new.bind("<Control-b>", lambda e: new.destroy())
    new.protocol("WM_DELETE_WINDOW", on_close)
    new.mainloop()

def blink_background():
    current = root["bg"]
    next_color = "red" if current == "black" else "black"
    root.configure(bg=next_color)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.configure(bg=next_color)
    root.after(500, blink_background)

def shake_label():
    if hacked_label.winfo_exists():
        x = 500 + random.randint(-5, 5)
        y = 100 + random.randint(-5, 5)
        hacked_label.place(x=x, y=y)
        root.after(100, shake_label)

def check_for_bsod():
    if click_count >= 10:
        fake_bsod()

def fake_bsod():
    bsod = tk.Toplevel()
    bsod.attributes("-fullscreen", True)
    bsod.configure(bg="blue")
    bsod_text = (
        ":(\n\n"
        "Un problème est survenu et votre ordinateur doit redémarrer.\n"
        "Nous recueillons simplement des informations sur l’erreur, puis nous redémarrerons pour vous.\n\n"
        "Erreur : CRITICAL_FAKE_VIRUS_DETECTED\n\n"
        "[##########                    ] 42%"
    )
    label = tk.Label(bsod, text=bsod_text, font=("Consolas", 20), fg="white", bg="blue", justify="left")
    label.pack(pady=100)
    bsod.after(10000, lambda: bsod.destroy())  # Fermeture après 10s

def prank_mouse():
    if platform.system() == "Windows" and MOUSE_PRANK:
        SPI_SETMOUSESPEED = 0x0071
        new_speed = 1  # Lent
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETMOUSESPEED, 0, new_speed, 0)

root = tk.Tk()
root.title("Oops...")
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.protocol("WM_DELETE_WINDOW", on_close)
root.bind("<Control-b>", emergency_exit)
root.config(cursor="pirate")

prank_mouse()

hacked_label = tk.Label(root, text="I've been hacked", font=("Arial", 40), fg="red", bg="black")
hacked_label.place(x=500, y=100)

oui_button = tk.Button(root, text="Oui", command=moral_message, bg="green", fg="white", font=("Arial", 18), cursor="pirate")
oui_button.place(x=500, y=400)

non_button = tk.Button(root, text="Non", bg="gray", fg="white", font=("Arial", 18), cursor="pirate")
non_button.place(x=800, y=400)
non_button.bind("<Enter>", lambda e: evade_mouse(e, non_button))
non_button.config(command=create_new_non_button)

blink_background()
shake_label()

root.mainloop()
