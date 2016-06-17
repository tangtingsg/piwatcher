#!/usr/bin/env python3

from utils import run_command
import os
import piwatcher


def main():
    print("============Install Packages============")
    run_command('apt-get install -y sqlite3 python-sqlite')
    run_command('pip3 install Django')
    run_command('pip3 install pyqrcode')
    run_command('pip3 install pypng')

    print("============Copy Files============")
    run_command('cp pisensor.service /lib/systemd/system')
    run_command('cp piweb.service /lib/systemd/system')

    run_command('systemctl daemon-reload')

    print("============Start PiWatcher============")
    piwatcher.start()

if __name__ == '__main__':
    if os.getuid() == 0:
        main()
    else:
        print("Need permission. Use 'sudo python3 install.py'")
