import datetime
import os

from tests.conftest import LOGS_PATH, ALL_LOGS_PATH


def test_logfiles_created():
    assert os.path.exists(LOGS_PATH)
    assert os.path.exists(ALL_LOGS_PATH)


def test_messages_logging(preparing_class_logging):
    log_messages = [
            "First test info message",
            "Second test info message",
            "Last test info message",
        ]
    logging = preparing_class_logging

    clear_file(LOGS_PATH)
    clear_file(ALL_LOGS_PATH)

    for message in log_messages:
        logging.logger.info(message)

    with open(LOGS_PATH, "r") as f:
        read_logs = f.readlines()
    with open(ALL_LOGS_PATH, "r") as f:
        read_alllogs = f.readlines()

    assert len(read_logs) == 3
    assert log_messages[0] in read_logs[0]
    assert log_messages[-1] in read_logs[-1]
    assert read_logs == read_alllogs


def test_logging_data_with_timestamp(preparing_class_logging):
    logging = preparing_class_logging
    message = "Test info message"

    logging.logger.info(message)

    now = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    log_timestamp = f"{now} {message}\n"

    with open(LOGS_PATH, "r") as f:
        read_logs = f.readlines()

    assert read_logs[-1] == log_timestamp


def clear_file(file_path: str) -> None:
    file_to_clear = open(file_path, "w")
    file_to_clear.close()
