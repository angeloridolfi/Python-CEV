nome = str(input('Digite seu nome aqui:_')).capitalize()

if nome == "Angelo":
    print(f'\033[32m{nome.capitalize()} que nome maneiro, meu jovem!\033[m')
if nome in ["Pedro", "João", "Maria"]:
    print('Seu nome é bem popular no brasil!')
if nome in 'Ana Claudia Julia':
    print('Que Belo nome Feminino!')
print(f'Tenha um bom dia, {nome.capitalize()}!')