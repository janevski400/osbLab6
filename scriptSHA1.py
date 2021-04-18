import subprocess
output = subprocess.run(['sudo','openssl','dgst','-sha1','poraka.txt'], capture_output=True, text=True)
sha1_value = output.stdout[18:]
sha1_value = sha1_value.rstrip('\n')
userSHA1 = input("Vnesete SHA1 hash vrednost: ")
if userSHA1==sha1_value:
    print("SHA1 vrednostite se isti")
else:
    print("SHA1 vrednostite ne se isti")
