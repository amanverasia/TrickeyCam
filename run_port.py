import os 
name = input('Input the name of the link: ')
if not name:
	name = 'random'
print(name)
os.system(f'ssh -R 80:0.0.0.0:3333 {name}@ssh.localhost.run')
