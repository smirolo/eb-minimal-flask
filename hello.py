import os
import boto
from boto.s3.key import Key
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    decrypt_key = os.getenv("CREDENTIALS_KEY", None)
    conn = boto.connect_s3()
    mybucket = conn.get_bucket('eb-minimal-flask-credentials')
    k = Key(mybucket)
    k.key = 'credentials'
    secret_key = k.get_contents_as_string()
    return "Hello World!\nThe decription key is: '%s'\nThe secret is '%s'" \
        % (decrypt_key, secret_key)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"))
