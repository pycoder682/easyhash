import hashlib
import time

word = input('Enter what you want hashed in md5 here: ')

enc = word.encode('utf-8')

hash1 = hashlib.md5(enc.strip()).hexdigest()

print('The md5 hashed result is: ' + str(hash1))

time.sleep(10)

quit()