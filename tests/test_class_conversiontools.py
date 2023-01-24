import os
import threading

import pytest

from tests.conftest import THREAD1_FILE, THREAD2_FILE

ALL_LOGS_FILE = "./logs/AllLogs.log"


def test_stop_threads_method(preparing_class_conversiontools):
    conversion_instance = preparing_class_conversiontools
    thread1 = threading.Thread(target=conversion_instance.thread1, args=[])
    thread2 = threading.Thread(target=conversion_instance.thread2, args=[])
    thread1.start()
    thread2.start()

    conversion_instance.stop_threads()

    thread1.join()
    thread2.join()

    os.remove(THREAD1_FILE)
    os.remove(THREAD2_FILE)

    assert threading.active_count() == 1


def test_thread1_file_created(start_thread1):
    assert os.path.exists(THREAD1_FILE)


def test_thread2_file_created(start_thread2):
    assert os.path.exists(THREAD2_FILE)


def test_thread1_file_format(start_thread1):
    with open(THREAD1_FILE, "r") as f:
        thread1_file = f.readline()

    line = thread1_file.split()

    assert len(line) == 2
    assert line[0].endswith(":")


def test_thread2_file_format(start_thread2):
    with open(THREAD2_FILE, "r") as f:
        thread2_file = f.readline()

    line = thread2_file.split()

    assert len(line) == 2
    assert line[0].endswith(":")


def test_thread1_numeral_systems(start_thread1):
    with open(THREAD1_FILE, "r") as f:
        read_line = f.readline()

    line = read_line.split()
    hex_number, dec_number = line[0][:-1], line[1][:-1]

    assert int(hex_number, 16)
    assert int(dec_number)


def test_thread2_numeral_systems(start_thread2):
    with open(THREAD2_FILE, "r") as f:
        read_line = f.readline()

    line = read_line.split()
    hex_number, bin_number = line[0][:-1], line[1][:-1]

    assert int(hex_number, 16)
    assert int(bin_number, 2)


# @patch("time.sleep")
def test_thread1_delay(start_thread1, mocked_sleep):
    delay = 5
    mocked_sleep(delay)

    with open(THREAD1_FILE, "r") as f:
        read_file = f.readlines()

    assert len(read_file) == delay


def test_thread2_delay(start_thread2, mocked_sleep):
    delay = 5
    mocked_sleep(delay)

    with open(THREAD2_FILE, "r") as f:
        read_file = f.readlines()

    assert len(read_file) == delay // 2


def test_convert_data_wrong_formats_exception(preparing_class_conversiontools):
    conversion_instance = preparing_class_conversiontools

    with pytest.raises(TypeError):
        conversion_instance.convert_data(ALL_LOGS_FILE, "binary")


def test_convert_data_bin_format(preparing_class_conversiontools):
    pass


def test_convert_data_dec_format(preparing_class_conversiontools):
    pass
