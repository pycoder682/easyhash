import hashlib
import time

word = input('Enter what you want hashed in sha1 here: ')

enc = word.encode('utf-8')

hash1 = hashlib.sha1(enc.strip()).hexdigest()

print('The sha1 hashed result is: ' + str(hash1))

time.sleep(10)

quit()