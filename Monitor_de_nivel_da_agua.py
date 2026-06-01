from colorama import Fore, Style, init

init(autoreset=True)

# Lista de leveis da água
levels = [
    "Muito Baixo (critíco)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito Alto (alerta)"
]

# Função de input de altura da água pelo usuario
def get_water_level():
    while True:
        try:
            level = int(input("Insira a altura da água (0 - 100): "))

            if 0 <= level <= 100:
                return level
            else:
                print("Erro: Insira valor entre 0 à 100.")

        except ValueError:
            print("Erro: Insira um valor válido.")


# Função que define o status da altura da água
def water_status(water_level):

    if 0 <= water_level <= 20:
        color = Fore.RED
        status = levels[0]

    elif 21 <= water_level <= 40:
        color = Fore.YELLOW
        status = levels[1]

    elif 41 <= water_level <= 60:
        color = Fore.GREEN
        status = levels[2]

    elif 61 <= water_level <= 80:
        color = Fore.CYAN
        status = levels[3]

    else:
        color = Fore.BLUE
        status = levels[4]

    print(color + "=" * 45)
    print(color + f"Nível da Água: {water_level}%")
    print(color + f"Status do Reservatório: {status}")
    print(color + "=" * 45)
    print(Style.RESET_ALL)

water_level = get_water_level()
water_status(water_level)