import subprocess
output = subprocess.run(['sudo','openssl','dgst','-md5','poraka.txt'], capture_output=True, text=True)
md5_value = output.stdout[17:]
md5_value = md5_value.rstrip('\n')
userMD5 = input("Vnesete MD5 hesh vrednost: ")
if userMD5==md5_value:
    print("MD5 vrednostite se isti")
else:
    print("MD5 vrednostite ne se isti")
