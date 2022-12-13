import random
import time
from threading import Thread

from task.ConversionTools import ConversionTools


def main():
    conversion_instance = ConversionTools()
    thread1 = Thread(target=conversion_instance.thread1, args=[])
    thread2 = Thread(target=conversion_instance.thread2, args=[])
    thread1.start()
    thread2.start()
    time.sleep(random.randint(10, 200))
    conversion_instance.stop_threads()

    conversion_instance.convert_data("./logs/AllLogs.log", frmt="bin")


if __name__ == "__main__":
    main()
