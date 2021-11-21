import hashlib
def take_inp():
    hash_inp = input("Enter your hash: ")
    user_inp = input("Enter your string: ")

    if hash_inp=='md5' or hash_inp=='md5':
        result = hashlib.md5(user_inp.encode())
        final_result = result.hexdigest()
        print(final_result)

    elif hash_inp=='sha256' or hash_inp=='SHA256':
        result = hashlib.sha256(user_inp.encode())
        final_result = result.hexdigest()
        print(final_result)

    elif hash_inp=='sha384' or hash_inp=='SHA384':
        result = hashlib.sha384(user_inp.encode())
        final_result = result.hexdigest()
        print(final_result)

    elif hash_inp=='sha224' or hash_inp=='SHA224':
        result = hashlib.sha224(user_inp.encode())
        final_result = result.hexdigest()
        print(final_result)

    elif hash_inp=='sha512' or hash_inp=='SHA512':
        result = hashlib.sha512(user_inp.encode())
        final_result = result.hexdigest()
        print(final_result)

    elif hash_inp=='sha1' or hash_inp=='SHA1':
        result = hashlib.sha1(user_inp.encode())
        final_result = result.hexdigest()
        print(final_result)

    else:
        print("Invalid command.")
take_inp()
        
while True:
    take_inp()
