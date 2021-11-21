import hashlib
def take_inp():
    hash_inp = input("Enter your hash: ")
    user_inp = input("Enter your string: ")

    #MD5
    if hash_inp=='md5' or hash_inp=='md5':
        result = hashlib.md5(user_inp.encode()).hexdigest()
        print(result)

    #SHA-1
    elif hash_inp=='sha1' or hash_inp=='SHA1':
        result = hashlib.sha1(user_inp.encode()).hexdigest()
        print(result)

    #SHA-224
    elif hash_inp=='sha224' or hash_inp=='SHA224':
        result = hashlib.sha224(user_inp.encode()).hexdigest()
        print(result)
        
    #SHA-256
    elif hash_inp=='sha256' or hash_inp=='SHA256':
        result = hashlib.sha256(user_inp.encode()).hexdigest()
        print(result)
        
    #SHA-384
    elif hash_inp=='sha384' or hash_inp=='SHA384':
        result = hashlib.sha384(user_inp.encode()).hexdigest()
        print(result)
        
    #SHA-512
    elif hash_inp=='sha512' or hash_inp=='SHA512':
        result = hashlib.sha512(user_inp.encode()).hexdigest()
        print(result)
        
    #SHA-3-224
    elif hash_inp=='sha3_224' or hash_inp=='SHA3_224':
        result = hashlib.sha3_224(user_inp.encode()).hexdigest()
        print(result)

    #SHA-3-256
    elif hash_inp=='sha3_256' or hash_inp=='SHA3_256':
        result = hashlib.sha3_256(user_inp.encode()).hexdigest()
        print(result)

    #SHA-3-384
    elif hash_inp=='sha3_384' or hash_inp=='SHA3_384':
        result = hashlib.sha3_384(user_inp.encode()).hexdigest()
        print(result)
        
    #SHA-3-512
    elif hash_inp=='sha3_512' or hash_inp=='SHA3_512':
        result = hashlib.sha3_512(user_inp.encode()).hexdigest()
        print(result)

    else:
        print("Invalid command.")
take_inp()
        
while True:
    take_inp()
