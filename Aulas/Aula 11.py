from time import sleep

nome = str(input('Digite seu nome para analisarmos:')).strip().upper()

sleep(3)

if nome == "ANGELO":
	vac = str(input('Olá Ângelo, como vai você?')).lower().strip()

else:
	print('Que nombre horrible.')
	

if vac == 'bem':
	print('Que bom, até uma próxima.')
	
else:
	print('Então ta bom!')
	
