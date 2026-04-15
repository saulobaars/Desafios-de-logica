import tkinter as tk

janela = tk.Tk()
janela.geometry('600x400')
janela.title("Estrutura base")

frame1 = tk.Frame(janela,bg="lightblue",width=400,height=600,bd=0)
frame1.place(relx=0.0,rely=0.0,relheight=1,relwidth=0.2)


frame2 = tk.Frame(janela,bg="lightgreen",width=400,height=600,bd=0)
frame2.place(relx=0.2,rely=0.0,relheight=0.8,relwidth=0.8)

frame3 = tk.Frame(janela,bg="yellow",width=400,height=600,bd=0)
frame3.place(relx=0.2,rely=0.8,relheight=0.2,relwidth=0.8)

letra1 = tk.Label(frame1, text="Aqui",font=("Arial",10),bg="Lightblue")
letra1.place(relx=0.0,rely=0.0,relheight=0.2,relwidth=0.2)

letra2 = tk.Label(frame2, text="Este",font=("Arial",10),bg="lightgreen")
letra2.place(relx=0.2,rely=0.0,relheight=0.2,relwidth=0.3)

letra3 = tk.Label(frame3, text="Aquele",font=("Arial",10))
letra3.place(relx=0.2,rely=0.8,relheight=0.2,relwidth=0.3)

# campo_email = tk.Entry(janela, width=40)
# campo_email.pack (pady=10)

# campo_senha = tk.Entry(janela,show="*")
# campo_senha.pack(pady=10)



janela.mainloop()
