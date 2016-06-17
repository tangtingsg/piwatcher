#!/usr/bin/env python3

import log
import logging
import random
import time
import webhelper
import threading

log.setup_logging()


def watching():
    logging.info('start watching')
    while True:
        move = move_detection()
        if move:
            print('moving')
            threading.Thread(target=report_move, args=[time.time()]).start()
            time.sleep(5)
        else:
            print("quiet")
            time.sleep(1)


def move_detection():
    var = random.randint(0, 10)
    return var == 0


# report move event to server
def report_move(timestamp):
    result = webhelper.report_motion(timestamp)
    print("%f report status: %s" % (timestamp, result))

watching()
