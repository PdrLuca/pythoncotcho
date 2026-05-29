import customtkinter as ctk
import webbrowser
import os

ctk.set_appearance_mode('light')

janela = ctk.CTk()
janela.geometry('300x430')
janela.title('Bomba patch 2026')

def desligar():
    os.system('shutdown /s /t 0')
    
def reiniciar():
    os.system('shutdown /r /t 0')
    
def bloquear():
    os.system('rundll32.exe user32.dll,LockWorkStation')
    
def calculadora():
    os.system('calc')
    
def google():
    webbrowser.open('https://www.google.com')
    
def naocliqueaqui():
    janela2 = ctk.CTkToplevel()
    janela2.attributes('-fullscreen', True)
    janela2.configure(fg_color='#0078D7')
    
    messagem = """
    :(

    Seu dispositivo encontrou um problema e precisa ser reiniciado. Estamos apenas coletando algumas informações de erro e, em seguida, reiniciaremos para você.

    0% concluído

    Para obter mais informações sobre esse problema e possíveis correções, visite:
    https://www.windows.com/stopcode

    Se você ligar para uma pessoa de suporte, forneça estas informações:
    Código de parada: CRITICAL_PROCESS_DIED
    """
    texto = ctk.CTkLabel(janela2, 
                     text=messagem, 
                     font=('Arial', 25), 
                     justify='left',
                     text_color='white')    
 
    texto.pack(expand=True)    
    
bt01 = ctk.CTkButton(janela, 
                     text= 'Desligar',
                     fg_color= 'darkblue',
                     text_color= 'white',
                     width= 200,
                     height= 50,
                     font= ('Verdana', 30),
                     command= desligar)
bt01.pack(pady=20)

bt02 = ctk.CTkButton(janela, 
                     text= 'Reiniciar',
                     fg_color= 'darkblue',
                     text_color= 'white',
                     width= 200,
                     height= 50,
                     font= ('Verdana', 30),
                     command= reiniciar)

bt02.pack()


bt03 = ctk.CTkButton(janela, 
                     text= 'Bloquear',
                     fg_color= 'darkblue',
                     text_color= 'white',
                     width= 200,
                     height= 50,
                     font= ('Verdana', 30),
                     command= bloquear)

bt03.pack(pady=20)

bt04 = ctk.CTkButton(janela, 
                     text= 'Calculadora',
                     fg_color= 'darkblue',
                     text_color= 'white',
                     width= 200,
                     height= 50,
                     font= ('Verdana', 30),
                     command= calculadora)

bt04.pack()

bt05 = ctk.CTkButton(janela, 
                     text= 'Google',
                     fg_color= 'darkblue',
                     text_color= 'white',
                     width= 200,
                     height= 50,
                     font= ('Verdana', 30),
                     command= google)

bt05.pack(pady=20)

bt06 = ctk.CTkButton(janela, 
                     text= 'Não Clique Aqui😁',
                     fg_color= 'darkred',
                     text_color= 'white',
                     width= 200,
                     height= 50,
                     font= ('Verdana', 30),
                     command= naocliqueaqui)

bt06.pack()



janela.mainloop()
