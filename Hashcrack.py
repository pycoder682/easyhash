from urllib.request import urlopen, hashlib
import time
hashval = input("Please input the hash to crack.\n>")
LIST_OF_COMMON_HASHES = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
for guess in LIST_OF_COMMON_HASHES.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
    if hashedGuess == hashval:
        print("The plaintext for the hash is ", str(guess))
        time.sleep(5)
        quit()
    elif hashedGuess != hashval:
        print("Hash guess ",str(guess)," does not match, trying next...")
LIST_OF_COMMON_HASHES2 = str(urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'))
for guess2 in LIST_OF_COMMON_HASHES2.split('\n'):
    hashedGuess2 = hashlib.sha1(bytes(guess2, 'utf-8')).hexdigest()
    if hashedGuess2 == hashval:
        print("The plaintext for the hash is ", str(guess2))
        time.sleep(5)
        quit()
    elif hashedGuess2 != hashval:
        print("Hash guess ",str(guess2)," does not match, trying next...")
LIST_OF_COMMON_HASHES3 = str(urlopen('https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt'))
for guess3 in LIST_OF_COMMON_HASHES3:
    hashedGuess3 = hashlib.sha1(bytes(guess3, 'utf-8')).hexdigest()
    if hashedGuess3 == hashval:
        print('The plaintext for the hash is ', str(guess3))
        time.sleep(5)
        quit()
    elif hashedGuess3 != hashval:
        print('Hash guess ', str(guess3), ' does not match, trying next...')
for guess4 in LIST_OF_COMMON_HASHES.split('\n'):
    hashedGuess4 = hashlib.sha3_224(bytes(guess4, 'utf-8')).hexdigest()
    if hashedGuess4 == hashval:
        print("The plaintext for the hash is ", str(guess4))
        time.sleep(5)
        quit()
    elif hashedGuess4 != hashval:
        print("Hash guess ",str(guess4)," does not match, trying next...")
for guess5 in LIST_OF_COMMON_HASHES2.split('\n'):
    hashedGuess5 = hashlib.sha3_224(bytes(guess5, 'utf-8')).hexdigest()
    if hashedGuess5 == hashval:
        print("The plaintext for the hash is ", str(guess5))
        time.sleep(5)
        quit()
    elif hashedGuess5 != hashval:
        print("Hash guess ",str(guess5)," does not match, trying next...")
for guess6 in LIST_OF_COMMON_HASHES3:
    hashedGuess6 = hashlib.sha3_224(bytes(guess6, 'utf-8')).hexdigest()
    if hashedGuess6 == hashval:
        print('The plaintext for the hash is ', str(guess6))
        time.sleep(5)
        quit()
    elif hashedGuess6 != hashval:
        print('Hash guess ', str(guess6), ' does not match, trying next...')
for guess7 in LIST_OF_COMMON_HASHES.split('\n'):
    hashedGuess7 = hashlib.sha3_256(bytes(guess7, 'utf-8')).hexdigest()
    if hashedGuess7 == hashval:
        print("The plaintext for the hash is ", str(guess7))
        time.sleep(5)
        quit()
    elif hashedGuess7 != hashval:
        print("Hash guess ",str(guess7)," does not match, trying next...")
for guess8 in LIST_OF_COMMON_HASHES2.split('\n'):
    hashedGuess8 = hashlib.sha3_256(bytes(guess8, 'utf-8')).hexdigest()
    if hashedGuess8 == hashval:
        print("The plaintext for the hash is ", str(guess8))
        time.sleep(5)
        quit()
    elif hashedGuess8 != hashval:
        print("Hash guess ",str(guess8)," does not match, trying next...")
for guess9 in LIST_OF_COMMON_HASHES3:
    hashedGuess9 = hashlib.sha3_256(bytes(guess9, 'utf-8')).hexdigest()
    if hashedGuess9 == hashval:
        print('The plaintext for the hash is ', str(guess9))
        time.sleep(5)
        quit()
    elif hashedGuess9 != hashval:
        print('Hash guess ', str(guess9), ' does not match, trying next...')
for guess10 in LIST_OF_COMMON_HASHES.split('\n'):
    hashedGuess10 = hashlib.sha3_384(bytes(guess10, 'utf-8')).hexdigest()
    if hashedGuess10 == hashval:
        print("The plaintext for the hash is ", str(guess10))
        time.sleep(5)
        quit()
    elif hashedGuess10 != hashval:
        print("Hash guess ",str(guess10)," does not match, trying next...")
for guess11 in LIST_OF_COMMON_HASHES2.split('\n'):
    hashedGuess11 = hashlib.sha3_384(bytes(guess11, 'utf-8')).hexdigest()
    if hashedGuess11 == hashval:
        print("The plaintext for the hash is ", str(guess11))
        time.sleep(5)
        quit()
    elif hashedGuess11 != hashval:
        print("Hash guess ",str(guess11)," does not match, trying next...")
for guess12 in LIST_OF_COMMON_HASHES3:
    hashedGuess12 = hashlib.sha3_384(bytes(guess12, 'utf-8')).hexdigest()
    if hashedGuess12 == hashval:
        print('The plaintext for the hash is ', str(guess12))
        time.sleep(5)
        quit()
    elif hashedGuess12 != hashval:
        print('Hash guess ', str(guess12), ' does not match, trying next...')
for guess13 in LIST_OF_COMMON_HASHES.split('\n'):
    hashedGuess13 = hashlib.sha3_512(bytes(guess13, 'utf-8')).hexdigest()
    if hashedGuess13 == hashval:
        print("The plaintext for the hash is ", str(guess13))
        time.sleep(5)
        quit()
    elif hashedGuess13 != hashval:
        print("Hash guess ",str(guess13)," does not match, trying next...")
for guess14 in LIST_OF_COMMON_HASHES2.split('\n'):
    hashedGuess14 = hashlib.sha3_512(bytes(guess14, 'utf-8')).hexdigest()
    if hashedGuess14 == hashval:
        print("The plaintext for the hash is ", str(guess14))
        time.sleep(5)
        quit()
    elif hashedGuess14 != hashval:
        print("Hash guess ",str(guess14)," does not match, trying next...")
for guess15 in LIST_OF_COMMON_HASHES3:
    hashedGuess15 = hashlib.sha3_512(bytes(guess15, 'utf-8')).hexdigest()
    if hashedGuess15 == hashval:
        print('The plaintext for the hash is ', str(guess15))
        time.sleep(5)
        quit()
    elif hashedGuess15 != hashval:
        print('Hash guess ', str(guess15), ' does not match, trying next...')
for guess16 in LIST_OF_COMMON_HASHES.split('\n'):
    hashedGuess16 = hashlib.md5(bytes(guess16, 'utf-8')).hexdigest()
    if hashedGuess16 == hashval:
        print("The plaintext for the hash is ", str(guess16))
        time.sleep(5)
        quit()
    elif hashedGuess16 != hashval:
        print("Hash guess ",str(guess16)," does not match, trying next...")
for guess17 in LIST_OF_COMMON_HASHES2.split('\n'):
    hashedGuess17 = hashlib.md5(bytes(guess17, 'utf-8')).hexdigest()
    if hashedGuess17 == hashval:
        print("The plaintext for the hash is ", str(guess17))
        time.sleep(5)
        quit()
    elif hashedGuess17 != hashval:
        print("Hash guess ",str(guess17)," does not match, trying next...")
for guess18 in LIST_OF_COMMON_HASHES3:
    hashedGuess18 = hashlib.md5(bytes(guess18, 'utf-8')).hexdigest()
    if hashedGuess18 == hashval:
        print('The plaintext for the hash is ', str(guess18))
        time.sleep(5)
        quit()
    elif hashedGuess18 != hashval:
        print('Hash guess ', str(guess18), ' does not match, trying next...')
print('Hash cracking attempt failed. HashCrack is terminating...')
time.sleep(5)
quit()