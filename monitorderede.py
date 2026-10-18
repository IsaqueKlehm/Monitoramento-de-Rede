import subprocess

def menu():
    print("""
        --------Monitor de Rede--------

        1 - Verificar um dispositivo
        2 - Verificar vários dispositivos
        3 - Consultar histórico
        4 - Sair
        """)
    while True:

        try:  
            escolha = int(input("Digite sua escolha: "))
            if escolha > 4 or escolha <= 0: 
                while escolha > 4 or escolha <= 0:
                    escolha = int(input("Digite uma escolha válida: "))
                return escolha
            else:
             return escolha
        except ValueError:
            print("Erro de Escolha")
escolha = menu()

def opcao1():

    ip = input("Digite seu IP\nExemplo (8.8.8.8 ou google.com): ")

    resultado = subprocess.run(
    ["ping", "-n", "1", ip],
    capture_output=True,
    text=True
)

    print(resultado.stdout)
match escolha:
    # 1 - Verificar um dispositivo
    # 2 - Verificar vários dispositivos
    # 3 - Consultar histórico
    case 1:
        opcao1()
    case 2:
        pass
    case 3:
        pass
    case 4:
        print("Saindo")
        while True:
            break
    
