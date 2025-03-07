import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("7SA_Jafeth_Daniel_Gamboa_Baas")
        self.root.geometry("400x500")
        self.centrar_ventana()

        self.windows_opened = 0
        self.windows_closed = 0
        self.ventanas_abiertas = []  # Lista para almacenar las ventanas secundarias

        # Contenedor para los botones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=20)

        # Botones principales
        self.crear_botones()

        # Cronómetro (label)
        self.cronometro_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.cronometro_label.pack(pady=10)

        # Botón de salir (Inicialmente oculto)
        self.boton_salir = tk.Button(self.root, text="Salir", command=self.cerrar_todas_las_ventanas)
        self.boton_salir.pack(pady=10)
        self.boton_salir.pack_forget()

    def centrar_ventana(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def crear_botones(self):
       
        # Botones de tipo normal
         tk.Button(self.frame_botones, text="Florería 1", command=lambda: self.abrir_ventana_secundaria("https://www.liderempresarial.com/wp-content/uploads/2019/02/Floreria-Atlantico_Photographed-by-Javier-Pierini__2018_IMG_0786-1024x683.jpg", "Florería 1")).pack(pady=5)
         tk.Button(self.frame_botones, text="Florería 2", command=lambda: self.abrir_ventana_secundaria("https://media.timeout.com/images/102419719/image.jpg", "Florería 2")).pack(pady=5)
         tk.Button(self.frame_botones, text="Florería 3", command=lambda: self.abrir_ventana_secundaria("https://th.bing.com/th/id/OIP.cyXpWGCT7hfFlFkotGtRGAHaGL?rs=1&pid=ImgDetMain", "Florería 3")).pack(pady=5)

        # Botones de tipo radio button
        # self.radio_var = tk.StringVar()
        # tk.Radiobutton(self.frame_botones, text="Florería 1", variable=self.radio_var, value="https://www.liderempresarial.com/wp-content/uploads/2019/02/Floreria-Atlantico_Photographed-by-Javier-Pierini__2018_IMG_0786-1024x683.jpg", command=lambda: self.abrir_ventana_secundaria(self.radio_var.get())).pack(pady=5)
        # tk.Radiobutton(self.frame_botones, text="Florería 2", variable=self.radio_var, value="https://media.timeout.com/images/102419719/image.jpg", command=lambda: self.abrir_ventana_secundaria(self.radio_var.get())).pack(pady=5)
        # tk.Radiobutton(self.frame_botones, text="Florería 3", variable=self.radio_var, value="https://th.bing.com/th/id/OIP.cyXpWGCT7hfFlFkotGtRGAHaGL?rs=1&pid=ImgDetMain", command=lambda: self.abrir_ventana_secundaria(self.radio_var.get())).pack(pady=5)

        # # Botones de tipo check button
        #  self.check_vars = [tk.StringVar(), tk.StringVar(), tk.StringVar()]
        #  tk.Checkbutton(self.frame_botones, text="Florería 1", variable=self.check_vars[0], onvalue="https://www.liderempresarial.com/wp-content/uploads/2019/02/Floreria-Atlantico_Photographed-by-Javier-Pierini__2018_IMG_0786-1024x683.jpg", offvalue="", command=lambda: self.abrir_ventana_secundaria(self.check_vars[0].get(), "Florería 1")).pack(pady=5)
        #  tk.Checkbutton(self.frame_botones, text="Florería 2", variable=self.check_vars[1], onvalue="https://media.timeout.com/images/102419719/image.jpg", offvalue="", command=lambda: self.abrir_ventana_secundaria(self.check_vars[1].get(), "Florería 2")).pack(pady=5)
        #  tk.Checkbutton(self.frame_botones, text="Florería 3", variable=self.check_vars[2], onvalue="https://th.bing.com/th/id/OIP.cyXpWGCT7hfFlFkotGtRGAHaGL?rs=1&pid=ImgDetMain", offvalue="", command=lambda: self.abrir_ventana_secundaria(self.check_vars[2].get(), "Florería 3")).pack(pady=5)
    def abrir_ventana_secundaria(self, image_url, title):
        new_window = tk.Toplevel(self.root)
        new_window.geometry("300x200")
        new_window.title(title)

        response = requests.get(image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((300, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)

        label = tk.Label(new_window, image=photo)
        label.image = photo
        label.pack()

        new_window.protocol("WM_DELETE_WINDOW", lambda: None)

        new_window.after(10000, lambda: self.agregar_boton_cerrar(new_window))

        self.ventanas_abiertas.append(new_window)
        self.windows_opened += 1

        if self.windows_opened == 3:
            self.iniciar_cronometro(10)

    def agregar_boton_cerrar(self, window):
        tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

    def iniciar_cronometro(self, tiempo_restante):
        if tiempo_restante >= 0:
            self.cronometro_label.config(text=f"Tiempo restante: {tiempo_restante} s")
            self.root.after(1000, self.iniciar_cronometro, tiempo_restante - 1)
        else:
            self.mostrar_boton_cerrar_principal()

    def mostrar_boton_cerrar_principal(self):
        self.boton_salir.pack(pady=10)

    def cerrar_todas_las_ventanas(self):
        for ventana in self.ventanas_abiertas:
            ventana.destroy()
        if self.windows_opened >= 3:
            self.root.destroy()
        else:
            messagebox.showwarning("Advertencia", "Debe abrir las 3 ventanas secundarias antes de cerrar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    root.protocol("WM_DELETE_WINDOW", app.cerrar_todas_las_ventanas)
    root.mainloop()
