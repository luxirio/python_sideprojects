MENU = {'bat': 12,  'crepe': 15, 'suco': 8, 'tapioca': 10}

def restaurant():
    total = 0
    while True:
        order = input("Qual o seu pedido senhor(a): ").strip()

        if bool(order) == 0:
            break

        if order in MENU:
            price = MENU[order]
            total += price
            print(f"Seu pedido é:{order}, o preco é {price}, o total é {total}")
        else:
            print(f'Seu pedido de {order} nao consta no menu, krl')
    print(f"Seu total é de {total}, obg volte sempre")

# restaurant()

# Beyond exercise (1)

LOGIN_PASS = {"monica": "panicat123", "allef": "anaopaladino", "victor":"onepiece"}

def login():
    while True:
        user = input("Digite seu login:").strip()
        if bool(user) == 0:
            break
        senha = input("Digite sua senha:").strip()

        if user in LOGIN_PASS:
            if senha != LOGIN_PASS[user]:
                print("Senha erradamm tente novamente!")
            else:
                print("Login com sucesso!")
login()






