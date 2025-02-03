####imports####
import os
import time

#####variables#####
restaurants = [{
                "name": "Xis do XXXXXX",
                "category": "Xis",
                "activity": False
                },
                {
                "name": "Pizzaria XXXXX",
                "category": "Pizzaria",
                "activity": True
                },
                {
                "name": "XXXXXXX Sushi",
                "category": "Sushi",
                "activity": True
                },
                {
                "name": "XXXXXX Sushi",
                "category": "Sushi",
                "activity": False
                }]

#####functions######
def goHome():
    input("\nDigite uma tecla para voltar ao menu principal")
    main()

def closeApp():
    os.system("cls")
    print("Finalizando App")

def invalidOption():
    os.system("cls")
    print("Opção inválida!")
    goHome()
    
def showTitle():
    for i in range(3):
        time.sleep(0.2)
        os.system("cls")
        print("""
        ██████╗░█████╗░██████╗░░█████╗░██████╗░   ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
        """)
        time.sleep(0.2)
        os.system("cls")
        print("""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
        """)
def showSubtitle(subtitle):
    os.system("cls")
    line = "*" * (len(subtitle))
    print(f"{line}\n{subtitle}{line}\n")

def showLowerSubtitle(subtitle):
    line = "-" * (len(subtitle))
    print(f"{line}\n{subtitle}\n{line}\n")

def showOptions():
    print("1. Cadastrar restaurante\n2. Listar restaurante\n3. Alterar atividade do restaurante\n4. Sair")    

def selectOption():
    try:
        choosenOption = int(input("\nEscolha uma opção: "))
        print(f"Você escolheu a opção {choosenOption}")

        time.sleep(1)
        
        if choosenOption == 1:
            registerNewRestaurant()
        elif choosenOption == 2:
            listRestaurants()
        elif choosenOption == 3:
            activateRestaurants()
        elif choosenOption == 4:
            closeApp()
        else:
            invalidOption()
    except:
        raise Exception

def registerNewRestaurant():
    showSubtitle("CADASTRO DE NOVOS RESTAURANTES\n")

    restaurant_name = input("Digite o nome do restaurante que deseja registrar: ")
    restaurant_category = input(f"Digite a categoria do restaurante {restaurant_name}: ")

    restaurant_data = {"name": restaurant_name,
                       "category": restaurant_category,
                       "activity": False}
    
    restaurants.append(restaurant_data)
    print(f"O restaurante {restaurant_name} foi adicionado com sucesso!")
    goHome()

def showRestaurantsData():
    print("|nº|NOME                |CATEGORIA        |ATIVIDADE|\n")
    listsize = len(restaurants)
    if listsize == 0:
            print("Você não tem nenhum restaurante registrado")
    else:
        for i, restaurant in enumerate(restaurants):
            name = restaurant["name"]
            category = restaurant["category"]
            activity = restaurant["activity"]
            print(f"{i+1}: {name.ljust(20)} | {category.ljust(15)} | {activity}")

def listRestaurants():
    showSubtitle("LISTA DE RESTAURANTES\n")
    showLowerSubtitle("T A B E L A")
    showRestaurantsData()
    goHome()
    
def activateRestaurants():
    showSubtitle("ATIVAÇÃO/DESATIVAÇÃO DE RESTAURANTES\n")
    showRestaurantsData()

    restaurantToChange = input("\nDigite o nome do restaurante que você deseja alterar a atividade: \n(Digite 1 para ativar todos\nDigite 2 para desativar todos)")

    for restaurant in restaurants:
        if restaurantToChange == restaurant["name"]:
            restaurant["activity"] = not restaurant["activity"]
            if restaurant["activity"] == True:
                print(f"Você ativou o restaurante {restaurant["name"]} com sucesso")
            else:
                print(f"Você desativou o restaurante {restaurant["name"]} com sucesso")
        elif restaurantToChange == "1":
            restaurant["activity"] = True
            all_true = True
        elif restaurantToChange == "2":
            restaurant["activity"] = False
            all_true = False
        else:
            invalidOption()
    if all_true:
        print("\nVocê ativou todos os restaurantes com sucesso!")
    elif not all_true:
        print("\nVocê desativou todos os restaurantes com sucesso!")
    goHome()

def main():
    showTitle()
    showOptions()
    selectOption()

if __name__ == "__main__":
    main()
