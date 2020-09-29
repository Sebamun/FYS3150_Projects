import subprocess

ns = [10, 50, 100]
for n in ns:
    subprocess.run(['./Tridiag.x', str(n), 'hei'])