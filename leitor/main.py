import keyboard

#teclas_numericas = ""
teclas_numericas = []
codigo_de_acesso = 0

def on_key_event(e):
    global teclas_numericas

    if e.event_type == keyboard.KEY_DOWN:
        if e.name.isdigit():  # Verifica se a tecla pressionada é um dígito
            #teclas_numericas += e.name
            teclas_numericas.append(e.name)        
    

            
    if len(teclas_numericas) == 6 and e.name == 'enter':
        codigo_de_acesso = int(''.join(teclas_numericas))
        
        print(codigo_de_acesso)
        print(type(codigo_de_acesso))

        print("cadastrado api")
        teclas_numericas = []

    else:
        pass



# Adiciona um ouvinte de eventos de teclado
print("!!!!!!!!!!!!!RODANDO!!!!!!!!!!!!!!!!!!")
keyboard.hook(on_key_event)

# try:511629

#     # Mantém o programa em execução
#     keyboard.wait('esc')
# finally:
#     # Remove o ouvinte de eventos ao encerrar o programa
#     keyboard.unhook_all()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Fim do Código")

