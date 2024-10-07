ALPHABETLENGTH = 256
def encrypt(text : bytes, key: bytes) -> bytes:
    bytesout = b""
    for index, char in enumerate(text):
        keyval = 0
        for indexkey, charkey in enumerate(key):
            keyval += (charkey)*(index**indexkey)
        bytesout += int((char + keyval)%ALPHABETLENGTH).to_bytes(1, 'little')
    return bytesout

def decrypt(ciphertext : bytes, key : bytes) -> bytes:
    bytesout = b""
    for index, char in enumerate(ciphertext):
        keyval = 0
        for indexkey, charkey in enumerate(key):
            keyval += (charkey)*(index**indexkey)
        bytesout += int((char - keyval)%ALPHABETLENGTH).to_bytes(1, 'little')
    return bytesout

if __name__ == "__main__":
    print("ENTER MODE:")
    print("1 - Encrypt")
    print("2 - Decrypt")
    choice = str(input("Mode: "))
    if choice == "1":
        textinp = bytes(input("Input plaintext: "), "utf-8")
        keyinp = bytes(input("Input key: "), "utf-8")
        print(f"Result: {encrypt(textinp, keyinp)}")
    elif choice == "2":
        textinp = bytes(input("Input ciphertext: "), "utf-8")
        keyinp = bytes(input("Input key: "), "utf-8")
        print(f"Result: {decrypt(textinp, keyinp)}")