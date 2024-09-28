from argparse import ArgumentParser
from base64 import b64decode
from Crypto.Cipher import AES

def decrypt(encrypted_message: bytes, key: bytes) -> bytes:
    encrypted_message = b64decode(encrypted_message)
    iv = encrypted_message[:AES.block_size]  # Extract the IV (first 16 bytes)
    cipher_text = encrypted_message[AES.block_size:]  # The rest is the actual encrypted data

    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted = aes.decrypt(cipher_text)

    # Remove potential padding (e.g., PKCS7 padding)
    padding_length = decrypted[-1]
    return decrypted[:-padding_length]

def main() -> None:
    required_key_size = max(AES.key_size)

    parser = ArgumentParser()
    parser.add_argument("encrypted_message")
    parser.add_argument("password")

    args = parser.parse_args()
    encrypted_message: bytes = str(args.encrypted_message).encode()
    password: bytes = str(args.password).lower().ljust(required_key_size, "5").encode()

    decrypted_message = decrypt(encrypted_message, password)
    print(decrypted_message.decode())

if __name__ == "__main__":
    main()