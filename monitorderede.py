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
     
numero = menu()
print(numero)
