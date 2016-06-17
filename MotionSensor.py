from Sensor import *
from Relay import *
import webhelper
import threading


class MotionSensor(Sensor):

    def __init__(self, pin):
        Sensor.__init__(self,pin)
        # 上次检测到移动的时间
        self.lastMotionTime = 0

    def onStateChange(self, channel):
        print("%s: pin: %d state: %d" % (time.asctime(), channel, self.getState()))
        # 当前时间戳，如1466101905.8010414，单位秒
        current_time = time.time()
        time_span = current_time - self.lastMotionTime
        # 上报最短间隔3s
        if time_span > 3:
            print("%f report. time span : %d s" % (current_time, time_span))
            # 运动上报服务器, 子线程中进行
            threading.Thread(target=report_to_server, args=[current_time]).start()
            # 重置移动时间
            self.lastMotionTime = current_time
            # 1号灯亮
            relay.switch(0, 1)


def report_to_server(motion_time):
    result = webhelper.report_motion(motion_time)    # 访问的网络链接，耗时任务
    print("%f report status: %s" % (motion_time, result))
    # 1号灯灭
    relay.switch(0, 0)


def main():
    print("Start motion sensor")
    sensor = MotionSensor(17)
    sensor.setEvent(GPIO.BOTH)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    relay = Relay()
    main()
