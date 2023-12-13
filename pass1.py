import string
import hashlib

master = 'master-pass'
url    = 'test.url'
length = 32
iter0  = 3

key = list(hashlib.pbkdf2_hmac('sha256', master.encode('utf-8'), url.encode('utf-8'), iter0, length))

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

password = ''.join([chars[i % len(chars)] for i in key])

print(password)
