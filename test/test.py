import sys

sys.stdout.write('Welcome!!!!')
sys.stdout.flush()
while True:
    name = sys.stdout.write('what\'s your name: ')
    sys.stdout.flush()
    name = sys.stdin.readline().strip()
    sys.stdout.write(f'Hello {name}')
    sys.stdout.flush()