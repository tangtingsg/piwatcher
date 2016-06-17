import time
import subprocess
import shlex
import string
import random
from uuid import uuid1
import os
import pyqrcode
import config
import hashlib

string_pool = string.ascii_letters + string.digits
gen_random_text = lambda s: ''.join(map(lambda _: random.choice(string_pool), range(s)))


def timestamp():
    return int(time.time())


def run_command(cmd):
    args = shlex.split(cmd)
    subprocess.call(args)


def generate_uuid():
    return str(uuid1())


def gen_identity():
    if config.get_uuid() == "":
        uuid = generate_uuid()
        psw = gen_random_text(6)
        config.set_uuid_psw(uuid, psw)
    qrimg = os.path.join(config.PROJECT_DIR, config.get_identity_path())
    if not os.path.isfile(qrimg):
        gen_identity_img(qrimg)


def regen_identity():
    uuid = config.get_uuid()
    if uuid == "":
        uuid = generate_uuid()
    psw = gen_random_text(6)
    config.set_uuid_psw(uuid, psw)
    gen_identity_img()


def gen_identity_img(qrimg):

    json_str = str({'UUID': config.get_uuid(), 'PSW': config.get_psw()})
    qr = pyqrcode.create(json_str)
    qr.png(qrimg, scale=5)


def psw_salt(uuid, psw):
    md5 = hashlib.md5()
    pwbytes = (uuid+psw).encode('utf-8')
    md5.update(pwbytes)
    return md5.hexdigest()
