import os
import threading
from unittest import mock

import pytest

from task.ConversionTools import ConversionTools
from task.Logger import Logging


LOGS_FILE = "TestLogs.log"
ALL_LOGS_FILE = "AllLogs.log"
THREAD1_FILE = "./logs/hex_to_dec.log"
THREAD2_FILE = "./logs/hex_to_bin.log"
LOGS_PATH = os.path.join("./logs", LOGS_FILE)
ALL_LOGS_PATH = os.path.join("./logs", ALL_LOGS_FILE)


@pytest.fixture()
def preparing_class_logging():
    return Logging(LOGS_FILE)


@pytest.fixture()
def preparing_class_conversiontools():
    return ConversionTools()


@pytest.fixture()
def start_thread1(preparing_class_conversiontools, mocked_sleep):
    conversion_instance = preparing_class_conversiontools
    thread1 = threading.Thread(target=conversion_instance.thread1, args=[])
    thread1.start()
    mocked_sleep(10)

    yield thread1

    conversion_instance.stop_threads()
    thread1.join()

    os.remove("./logs/hex_to_dec.log")


@pytest.fixture()
def start_thread2(preparing_class_conversiontools, mocked_sleep):
    conversion_instance = preparing_class_conversiontools
    thread2 = threading.Thread(target=conversion_instance.thread2, args=[])
    thread2.start()
    mocked_sleep(10)

    yield thread2

    conversion_instance.stop_threads()
    thread2.join()

    os.remove("./logs/hex_to_bin.log")


@pytest.fixture()
def mocked_sleep():
    with mock.patch("time.sleep") as mock_sleep:
        yield mock_sleep
