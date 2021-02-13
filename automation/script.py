import subprocess

for i in range(5):
    subprocess.check_call(['python3', 'automation/example.py'])

r = subprocess.getoutput('date')
print(f'It is {r}')