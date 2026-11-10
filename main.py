# StardewCity

# Variáveis
day = 1
season = 'PRIMAVERA'
year = 1
mun_treasure = 1_000
num_citizens = 10
housing_cap = 12
housing_pct = (num_citizens * 100) / housing_cap
businesses = ['🛒  Mercado', '⚒️  Carpintaria']
num_business = len(businesses)
lvl_satisfaction = 72
diagnosis = []

# Menu de opções
options_menu = {
    1: 'Analisar negócios locais',
    2: 'Avançar para o próximo dia'
}

# Funções
def get_valid_int(msg):
    while True:
        try: 
            return int(input(msg))
        except ValueError:
            print("Escolha uma opção válida!")

def generate_diagnosis() -> str:
    if housing_pct >= 90:
        diagnosis.append('Moradias insuficientes ⛔')
    if lvl_satisfaction <= 40:
        diagnosis.append('Insatisfação popular ⛔')
    if mun_treasure <= 300:
        diagnosis.append('Alerta financeiro ⛔')
    if not diagnosis:
        diagnosis.append('Cidade estável ✅')
    return diagnosis

def show_menu():
    for key, value in options_menu.items():
        print(f'[{key}] {value}')

# Terminal
print('-=' * 10, "STARDEW CITY", '-=' * 10)
print(f'\n· DIA {day} · {season} · ANO {year}\n')
print(f'· 💰 Tesouro Municipal: ${mun_treasure:.2f}')
print(f'· 👤 Número de habitantes: {num_citizens}')
print(f'· 🏠 Capacidade Habitacional: {num_citizens}/{housing_cap} [{housing_pct:.0f}%]')
print(f'· 🏪 Número de negócios locais: {num_business}')
print(f'· 🙂 Nível de satisfação geral: {lvl_satisfaction}%')

print(f'\n· 📊 Diagnóstico atual: {' | '.join(generate_diagnosis())}\n')

show_menu()
user_choice = get_valid_int("· Selecione uma opção: ")

if user_choice == 1:
    print('\nNegócios locais:')
    print(' | '.join(businesses))
elif user_choice == 2:
    ...