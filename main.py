# StardewCity

# Variáveis
mun_treasure = 1_000
num_citizens = 10
housing_cap = 12
housing_pct = (num_citizens * 100) / housing_cap
businesses = ['🛒  Mercado', '⚒️  Carpintaria']
num_business = len(businesses)
lvl_satisfaction = 72

# Menu de opções
options_menu = {
    1: 'Analisar negócios locais',
    2: 'Avançar para o próximo dia'
}

# Funções
def get_valid_int(msg, min=None, max=None) -> int:
    while True:
        try:
            number = int(input(msg))
            if min or max: 
                if number > max or number < min:
                    print(f"Escolha uma das opções entre {min} ~ {max}")
                    continue

            return number
            
        except ValueError:
            print("Escolha uma opção válida!")

def generate_diagnosis() -> list[str]:
    """
    Gera uma lista zerada a cada chamada, a qual anota 
    os atuais diagnósticos da cidade, sendo por fim retornada.
    """

    diagnosis = []

    if housing_pct >= 90:
        diagnosis.append('Moradias insuficientes ⛔')
    if lvl_satisfaction <= 40:
        diagnosis.append('Insatisfação popular ⛔')
    if mun_treasure <= 300:
        diagnosis.append('Alerta financeiro ⛔')
    if not diagnosis:
        diagnosis.append('Cidade estável ✅')
    return diagnosis

def show_menu() -> None:
    for key, value in options_menu.items():
        print(f'[{key}] {value}')

def validate_choice(choice, current_day) -> int | None:
    if choice == 1:
        print('\nNegócios locais:')
        print(' | '.join(businesses))
    elif choice == 2:
        return current_day + 1
    return None

def game_loop() -> None:
    day = 1
    seasons = ['PRIMAVERA', 'VERÃO', 'OUTONO', 'INVERNO']
    month = 0
    year = 1
    # Terminal
    while True:
        print('-=' * 10, "STARDEW CITY", '-=' * 10)
        print(f'\n· DIA {day} · {seasons[month]} · ANO {year}\n')
        print(f'· 💰 Tesouro Municipal: ${mun_treasure:.2f}')
        print(f'· 👤 Número de habitantes: {num_citizens}')
        print(f'· 🏠 Capacidade Habitacional: {num_citizens}/{housing_cap} [{housing_pct:.0f}%]')
        print(f'· 🏪 Número de negócios locais: {num_business}')
        print(f'· 🙂 Nível de satisfação geral: {lvl_satisfaction}%')

        print(f'\n· 📊 Diagnóstico atual: {' | '.join(generate_diagnosis())}\n')

        show_menu()
        user_choice = get_valid_int("· Selecione uma opção: ", min=1, max=2)
        new_day = validate_choice(user_choice, day)
        if new_day:
            if new_day == 29:
                new_day = 1
                month += 1
                if month == 4:
                    month = 0
                    year += 1

            day = new_day

def main() -> None:
    game_loop()

if __name__ == '__main__':
    main()