import hashlib
import time

word = input('Enter what you want hashed in sha512 here: ')

enc = word.encode('utf-8')

hash1 = hashlib.sha3_512(enc.strip()).hexdigest()

print('The sha512 hashed result is: ' + str(hash1))

time.sleep(10)

quit()