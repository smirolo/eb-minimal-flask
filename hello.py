import os

import boto
from boto.s3.key import Key
from Crypto.Cipher import DES3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    conn = boto.connect_s3()
    mybucket = conn.get_bucket('eb-minimal-flask-credentials')
    k = Key(mybucket)
    k.key = 'credentials'
    content = k.get_contents_as_string()

    decrypt_key = os.getenv("CREDENTIALS_KEY", None).decode('hex')
    decrypt_iv = os.getenv("CREDENTIALS_IV", None).decode('hex')
    cipher = DES3.new(decrypt_key, DES3.MODE_CBC, decrypt_iv)
    secret_key = b''
    encoded_text = bytes(content)
    for block in range(0, len(encoded_text) // DES3.block_size):
        secret_key += cipher.decrypt(
          encoded_text[block * DES3.block_size : (block + 1) * DES3.block_size])
    result = "Hello World!\nThe decription key is: '%s'\nThe secret is '%s'" \
        % (decrypt_key, secret_key)
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=True)
