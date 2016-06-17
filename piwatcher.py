#!/usr/bin/env python3

import os
import argparse
import utils
from utils import run_command
import webhelper


def init_argparse():
    parser = argparse.ArgumentParser(description="Start or Stop the Pi Watcher")
    subparsers = parser.add_subparsers(dest="subparser")
    subparsers.add_parser('start', help='Start the watcher')
    subparsers.add_parser('stop', help='Stop the watcher')
    subparsers.add_parser('restart', help='Restart the watcher')
    subparsers.add_parser('status', help='Get status of the watcher')
    return parser.parse_args()


def init():
    utils.gen_identity()
    result = webhelper.create_account()
    if result:
        print("create account")


def start():
    init()
    run_command('systemctl start piweb.service')
    run_command('systemctl enable piweb.service')
    run_command('systemctl start pisensor.service')
    run_command('systemctl enable pisensor.service')
    return


def stop():
    run_command('systemctl stop piweb.service')
    run_command('systemctl disable piweb.service')
    run_command('systemctl stop pisensor.service')
    run_command('systemctl disable pisensor.service')
    return


def restart():
    stop()
    start()
    return


def status():
    run_command('systemctl status piweb.service')
    run_command('systemctl status pisensor.service')


def route(args):
    if args.subparser == 'start':
        start()
    elif args.subparser == 'stop':
        stop()
    elif args.subparser == 'restart':
        restart()
    elif args.subparser == 'status':
        status()


def main():
    args = init_argparse()
    route(args)


if __name__ == '__main__':
    if os.getuid() == 0:
        main()
    else:
        print("Need permission. Use 'sudo python3 piwatcher.py <args>'")

