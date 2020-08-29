import hashlib
import time

word = input('Enter what you want hashed in sha256 here: ')

enc = word.encode('utf-8')

hash1 = hashlib.sha3_256(enc.strip()).hexdigest()

print('The sha256 hashed result is: ' + str(hash1))

time.sleep(10)

quit()