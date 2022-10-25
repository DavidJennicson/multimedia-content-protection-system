from hashlib import sha256

def hasher(input):
    input=str(input)
    return (sha256(input.encode('utf-8')).hexdigest())