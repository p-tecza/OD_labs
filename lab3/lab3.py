from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

file_name="test.txt"
password=b"topsecretpass"


testdata=b'asdfasdfasdfasdfasdfasdfasdfasdf' # n * 16 bajtow

key=PBKDF2(password,b"costam")
f=open(file_name,"rb")

data=f.read()

ready_data=bytearray(data)

if len(data)%16!=0:
    bytes_to_append=16-len(data)%16
    data_to_append=get_random_bytes(bytes_to_append)
    ready_data+=data_to_append

ready_data=bytes(ready_data)

#print(type(ready_data))
#print(len(ready_data))

iv=get_random_bytes(16)
new_crypt=AES.new(key,AES.MODE_CBC,iv)
encrypted_data=new_crypt.encrypt(ready_data)

print(encrypted_data)



des = DES.new(b"key12345",DES.MODE_CBC)
iv = get_random_bytes(8)
des = DES.new(b"key12345",DES.MODE_CBC, iv)
encrypted = des.encrypt(b"secret12")
iv = get_random_bytes(16)
aes = AES.new(b"key4567890123456", AES.MODE_CFB, iv)
encrypted = aes.encrypt(b"test")