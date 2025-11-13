import tkinter as tk

class Kalkulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator Modern")
        self.geometry("340x520")
        self.config(bg="#0d1117")
        self.exp = ""

        # Display input
        self.display = tk.Entry(self, font=("Poppins", 28), bd=0, bg="#161b22", fg="white",
                                insertbackground="white", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=15, pady=(20, 5), ipady=15, sticky="nsew")

        # Label hasil otomatis
        self.result = tk.Label(self, text="", font=("Poppins", 18), fg="#58a6ff", bg="#0d1117", anchor="e")
        self.result.grid(row=1, column=0, columnspan=4, padx=20, pady=(0, 10), sticky="nsew")

        # Tombol-tombol kalkulator
        tombol = [
            ["C", "⌫", "/", "*"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", "(", ")"]
        ]

        # Buat tombol-tombol dengan ukuran seragam
        for r, row in enumerate(tombol, start=2):
            for c, t in enumerate(row):
                warna_bg = "#21262d"
                warna_fg = "white"
                warna_aktif = "#30363d"
                if t == "C": warna_bg = "#d32f2f"
                if t == "=": warna_bg = "#1e88e5"
                
                b = tk.Button(self, text=t, font=("Poppins", 20, "bold"), fg=warna_fg, bg=warna_bg,
                              activebackground=warna_aktif, activeforeground="#58a6ff",
                              bd=0, command=lambda x=t: self.tekan(x))
                b.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

        # Buat semua baris & kolom punya ukuran seragam
        for i in range(5):
            self.rowconfigure(i + 2, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)

    def tekan(self, t):
        if t == "C":
            self.exp = ""
        elif t == "⌫":
            self.exp = self.exp[:-1]
        elif t == "=":
            try:
                self.exp = str(eval(self.exp))
            except:
                self.exp = "Error"
        else:
            self.exp += t

        self.display.delete(0, "end")
        self.display.insert("end", self.exp)
        self.update_hasil()

    def update_hasil(self):
        try:
            if self.exp and self.exp[-1] not in "+-*/.()":
                hasil = eval(self.exp)
                self.result.config(text=f"= {hasil}")
            else:
                self.result.config(text="")
        except:
            self.result.config(text="")

if __name__ == "__main__":
    Kalkulator().mainloop()

