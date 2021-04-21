import subprocess

def aesTest(password):
    subprocess.run(['sudo','openssl','enc','-d','-aes-128-ecb','-in','poraka.aes','-out','output.txt','-nosalt', '-k', password], text=True, capture_output=True)
    try:
        tempVar = open('output.txt', encoding='utf-8', mode='r').read()
        if tempVar:
            return 1
        else:
            return 0
    except:
        return 0    

password_file = open('password.txt','r')
for line in password_file:
    if aesTest(line.rstrip('\n'))==1:   
        print("Passwordot e: "+line.rstrip('\n'))
        exit()       
    else:
        print(line.rstrip('\n') +" ne e tochniot password.")
        subprocess.run('rm output.txt')

print("Ne e pronajden tochen password.")
