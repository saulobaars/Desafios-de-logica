import tkinter as tk

janela = tk.Tk()
janela.geometry('600x400')
janela.title("Olá, Mundo!")

texto = tk.Label(janela, text="Olá,Mundo!")
texto.pack()
frame = tk.Frame(janela,bg="lightblue",width=1000,height=1000,bd=3)
frame.pack()
# campo_email = tk.Entry(janela, width=40)
# campo_email.pack (pady=10)

# campo_senha = tk.Entry(janela,show="*")
# campo_senha.pack(pady=10)



janela.mainloop()
