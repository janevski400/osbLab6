import subprocess

def aesTest(password):
    output = subprocess.run(['sudo','openssl','enc','-d','-aes-128-ecb','-pbkdf2','-iter','10000','-in','test.aes','-out','output.txt','-p','-nosalt', '-k', password], text=True, capture_output=True)
    tempStderr = output.stderr
    tempStderr = tempStderr.rstrip('\n')
    if tempStderr.find('bad decrypt'):
        return 0
    else:
        return 1

password_file = open('password.txt','r')    #otvoranje na fajl password.txt za chitanje koj gi sodrzi najkoristenite 10 000 lozinki
for line in password_file:
    if aesTest(line.rstrip('\n'))==1:    #povikuvanje na funkcija aesTest kade kako argument se isprakja sekoja linija od fajlot so izbrishan \n na krajot (eden password od listata)
        print("Passwordot e: "+line.rstrip('\n'))
        exit()       
    else:
        print(line.rstrip('\n') +" ne e tochniot password.")

print("Ne e pronajden tochen password.")
