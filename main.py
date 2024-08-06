import tkinter as tk
from PIL import Image,ImageTk

# Main program
root = tk.Tk()

data_base= []

# Icons
#home icon
original_home_icon = Image.open("home.png")
resized_home_icon = original_home_icon.resize((25, 25), Image.ANTIALIAS)  # İkonu yeniden boyutlandır
home_icon = ImageTk.PhotoImage(resized_home_icon)
#profile icon
original_profile_icon = Image.open("profile.png")
resized_profile_icon = original_profile_icon.resize((60,60), Image.ANTIALIAS)  # İkonu yeniden boyutlandır
profile_icon = ImageTk.PhotoImage(resized_profile_icon)

# Paddings
def pad(number):
    return number

#new window
def new_screen():
    # Mevcut pencerenin içeriğini temizle
    for widget in root.winfo_children():
        widget.destroy()

    #root
    root.configure(bg="black")
    root.title("Giriş Yap")
    root.geometry("600x600")
    root.minsize(300,600)
    root.maxsize(600,600)

    # labels
    label_name = tk.Label(root, text="İsim Soyisim",width=20)
    label_adress = tk.Label(root,text="Adres",width=20)

    #entries
    name=tk.Entry(root,
                width=50,
                bd=0.5,
                bg="white")#isim

    adress = tk.Entry(root,
                      width=50,
                      bd=0.5,
                      bg="white")#adres


    # buttons
    back_button = tk.Button(root, text="   Geri Dön",image=home_icon, compound="left", font=("Arial" ,15), cursor="hand2", command=main_screen)
    back_button.image= home_icon

    submit_button = tk.Button(root, text="KAYDET",command=)

    #grids
    label_name.grid(row=0, column=0,pady=(pad(50),pad(10)), padx=10)
    name.grid(row=0,column=1, pady=(pad(50),pad(10)),padx=(pad(5),pad(20)))
    label_adress.grid(row=1,column=0, pady=(pad(10),pad(15)), padx=10)
    adress.grid(row=1,column=1, pady=10,padx=(pad(5),pad(20)))
    back_button.grid(row=2,column=1, pady=10)


def add_entry():
    x = name.get()

# Main window
def main_screen():
    # Pencereyi temizle
    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("600x600")
    root.configure(bg="black")
    root.minsize(300,600)
    root.maxsize(600,600)

    root.title("Su Tasarrufu Projesi")
    # Label
    label1 = tk.Label(root, text="SU TASARRUFU PROJESİ")
    label1.pack(pady=(pad(50),pad(10)))
    label1.configure(fg="white", bg="black", font=("Arial", 15))

    label2 = tk.Label(root, text="Üye Kaydı", image=profile_icon,compound="top")
    label2.configure(fg="white", bg="black", font=("Arial", 15))
    label2.pack(pady=5)


    # Button
    start_button = tk.Button(root, text="GİRİŞ YAP", cursor="hand2", command=new_screen)
    start_button.pack(pady=(pad(20), pad(10)))

    quit_button = tk.Button(root, text="ÇIKIŞ YAP", cursor="hand2", command=root.destroy)
    quit_button.pack(pady=(pad(10), pad(10)))


#new_screen()
main_screen()
root.mainloop()
