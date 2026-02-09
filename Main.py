import tkinter as tk
import pytesseract as pyocr
import threading, time, mss, pyautogui, cv2, os

rodando = False
LARGURA = 800
ALTURA = 600
PASTA_SCREENSHOTS = "screenshots"  # Defina a pasta desejada aqui

# Criar pasta se não existir
if not os.path.exists(PASTA_SCREENSHOTS):
    os.makedirs(PASTA_SCREENSHOTS)

def macro_loop():
    global rodando
    while rodando:
        with mss.mss() as sct:
            sct.shot(output=os.path.join(PASTA_SCREENSHOTS, "screenshot.png"))
        rodando = False
        time.sleep(1)  # Ajuste o tempo de espera conforme necessário

def iniciar_macro():
    global rodando
    if not rodando:
        rodando = True
        thread = threading.Thread(target=macro_loop, daemon=True)
        thread.start()
        status_label.config(text="Status: Rodando")

def parar_macro():
    global rodando
    rodando = False
    status_label.config(text="Status: Parado")
        
        
# Interface

root = tk.Tk()
root.geometry(f"{LARGURA}x{ALTURA}")
root.resizable(False, False)
root.title("Megapoint Macro")

btn_iniciar = tk.Button(root, text="Iniciar Macro", command=iniciar_macro)
btn_iniciar.pack(pady=10)

btn_parar = tk.Button(root, text="Parar Macro", command=parar_macro)
btn_parar.pack(pady=10)

status_label = tk.Label(root, text="Status: Parado")
status_label.pack(pady=10)

root.mainloop()