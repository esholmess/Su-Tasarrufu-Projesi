import tkinter as tk
from PIL import Image,ImageTk

# Main program
root = tk.Tk()

# Icons
#home icon
original_home_icon = Image.open("home.png")
resized_home_icon = original_home_icon.resize((25, 25), Image.ANTIALIAS)  # İkonu yeniden boyutlandır
home_icon = ImageTk.PhotoImage(resized_home_icon)
#profile icon
original_profile_icon = Image.open("profile.png")
resized_profile_icon = original_profile_icon.resize((60,60), Image.ANTIALIAS)  # İkonu yeniden boyutlandır
profile_icon = ImageTk.PhotoImage(resized_profile_icon)


#new window
def new_screen():
    # Mevcut pencerenin içeriğini temizle
    for widget in root.winfo_children():
        widget.destroy()

    # labels
    label_name = tk.Label(root, text="İsim, Soyisim")
    label_name.pack(pady=20)

    #entry
    name=tk.Entry(root,
                width=50,
                bg="white")
    name.pack()


    # Bir geri dön düğmesi ekleyin
    back_button = tk.Button(root, text="   Geri Dön",image=home_icon, compound="left", font=("Arial" ,15), cursor="hand2", command=main_screen)
    back_button.image= home_icon
    back_button.pack(pady=20,padx=10)


# Main window
def main_screen():
    # Pencereyi temizle
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("500x300")
    root.configure(bg="black")
    root.title("Su Tasarrufu Projesi")
    # Label
    label1 = tk.Label(root, text="SU TASARRUFU PROJESİ")
    label1.pack(pady=10)
    label1.configure(fg="white", bg="black", font=("Arial", 15))

    label2 = tk.Label(root, text="Üye Kaydı", image=profile_icon,compound="top")
    label2.configure(fg="white", bg="black", font=("Arial", 15))
    label2.pack(pady=5)

    # Paddings
    pad_10 = 10
    pad_20 = 20

    # Button
    start_button = tk.Button(root, text="GİRİŞ YAP", cursor="hand2", command=new_screen)
    start_button.pack(pady=(pad_20, pad_10))

    quit_button = tk.Button(root, text="ÇIKIŞ YAP", cursor="hand2", command=root.destroy)
    quit_button.pack(pady=(pad_10, pad_20))



main_screen()
root.mainloop()
