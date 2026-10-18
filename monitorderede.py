import subprocess

lista_historico = []

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

def opcao1():
    ip = input("Digite seu IP\nExemplo (8.8.8.8 ou google.com): ")

    resultado = subprocess.run(
    ["ping", "-n", "1", ip],
    capture_output=True,
    text=True
    )
    lista_historico.append(resultado)
    print(resultado.stdout)

def opcao2():
    lista_ip = []
    while True:
        try:
            quantidade = int(input("Digite a quantidade de ip que deseja verificar: "))
            while quantidade <= 0:
                quantidade = int(input("Digite uma quantidade válida: "))
            else:
                break
        except ValueError:
            print("Número inválido")

    for i in range(quantidade):
        ip = input(f"Digite o IP {i+1}: ")
        lista_ip.append(ip)

    for i in lista_ip:
        resultado = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
        )
        print(resultado.stdout)
        lista_historico.append(resultado)

def opcao3(historico):
    print("\n---------Histórico---------")
    print(f"{historico}\n")

    pass
while True:
    escolha = menu()
    match escolha:
        case 1:
            opcao1()
        case 2:
            opcao2()
        case 3:
            opcao3(lista_historico)
        case 4:
            print("Saindo")
            break
    
