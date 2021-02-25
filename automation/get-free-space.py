import subprocess

get_free_space = 'df -h / | awk \'NR==2 {print $4}\''

stdout, stderr = subprocess.Popen(
    get_free_space,
    universal_newlines=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
).communicate()

print(f'stdout:\n{stdout}')
print(f'stderr:{stderr}')