import subprocess
password = input('Vnesete password: ')
output = subprocess.run(['sudo', 'openssl', 'dgst' , '-sha256','-hmac', password, 'poraka.txt'], capture_output=True, text=True)
#so pomosh na shlex.split se dobiva sledniot format za argumenti ['sudo', 'openssl', 'dgst', '-sha256', '-hmac', '!!tuka password!!', 'poraka.txt']
sha256_value = output.stdout[25:]
sha256_value = sha256_value.rstrip('\n')
userPassword = input('Vnesete hash256 vrednost so koja sakate da sporedite: ')
if sha256_value==userPassword:
    print("Dvata hasha se isti")
else:
    print("Dvata hasha ne se isti")
