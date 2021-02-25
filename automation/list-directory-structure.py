import subprocess

command = ['ls', '-lah', '.']

stdout, stderr = subprocess.Popen(
    command,
    universal_newlines=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
).communicate()

print(f'stdout:\n{stdout}')
print(f'stderr:{stderr}')
