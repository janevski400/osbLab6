import subprocess

userHash = "64cc504a93c31c8ef88999b63c5442f50cd3f156dd0ece551006996a7a1f499f" # tuka se vnesuva hash vrednost koja sakame da ja dobieme

def sha256test(password):   #funkcija koja proveruva dali passwordot odgovara na dadenata hash vrednost dobiena od fajlot poraka.txt
    output = subprocess.run(['sudo', 'openssl', 'dgst' , '-sha256','-hmac', password, 'poraka.txt'], capture_output=True, text=True)
    sha256_value = output.stdout[25:]   #brishenje na nepotrebnite karakteri za da se dobie samo hashot
    sha256_value = sha256_value.rstrip('\n')    #brishenje na \n na krajot na hashot
    if sha256_value==userHash:
        return 1
    else:
        return 0

password_file = open('password.txt','r')    #otvoranje na fajl password.txt za chitanje
for line in password_file:
    if sha256test(line.rstrip('\n'))==1:    #povikuvanje na funkcija sha256 kade kako argument se isprakja sekoja linija od fajlot so izbrishan \n na krajot
        print("Passwordot e: "+line)
        exit()       
    else:
        print(line.rstrip('\n') +" ne e tochniot password.")
        
print("Ne e pronajden tochen password.")

#za predvremeno zapiranje na skriptata pritisnete ctrl+z
