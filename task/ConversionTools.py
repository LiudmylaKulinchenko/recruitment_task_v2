import random
import threading
import time

from task.Logger import Logging


class ConversionTools:
    EVENT = threading.Event()
    WRONG_FRMT_ERROR = "Converting format should be bin or dec"

    def __init__(self) -> None:
        self.logging = Logging(file_name="LogsFile.log")
        self.thread1_file = "./logs/hex_to_dec.log"
        self.thread2_file = "./logs/hex_to_bin.log"
        self.thread1_delay = 1
        self.thread2_delay = 2

    def thread1(self) -> None:
        """
        Write a random number in hexadecimal and decimal
        to the "hex_to_dec.log" file every 1 second
        """

        with open(self.thread1_file, "w") as f:
            while True:
                number = random.randint(0, 1_000)
                data = f"{hex(number)}: {number}"

                f.write(data + "\n")

                self.logging.logger.info(data)
                time.sleep(self.thread1_delay)

                if self.EVENT.is_set():
                    break

    def thread2(self) -> None:
        """
        Write a random number in hexadecimal and binary
        to the "hex_to_bin.log" file every 2 second
        """

        with open(self.thread2_file, "w") as f:
            while True:
                number = random.randint(0, 1_000)
                data = f"{hex(number)}: {bin(number)}"

                f.write(data + "\n")

                self.logging.logger.info(data)
                time.sleep(self.thread2_delay)

                if self.EVENT.is_set():
                    break

    def convert_data(self, file_path: str, frmt: str) -> None:
        """Converts the contents of the file to the format (bin or dec)"""

        if frmt not in ("bin", "dec"):
            raise TypeError(self.WRONG_FRMT_ERROR)

        with open(file_path, "r") as f:
            readfile = f.readlines()

        with open(file_path, "w") as f:
            for line in readfile:
                line = line.split()
                current_number = line[-1]

                line = convert_number(frmt, current_number, line)

                f.write(line + "\n")

    def stop_threads(self) -> None:
        if not self.EVENT.is_set():
            self.EVENT.set()


def convert_number(frmt: str, number: str, line: list[str]) -> str:
    if frmt == "bin":
        if number.startswith("0b"):
            return " ".join(line)
        else:
            number = int(number)
            return " ".join(line[:-1]) + " " + bin(number)

    if frmt == "dec":
        if number.startswith("0b"):
            number = int(number, 2)
            return " ".join(line[:-1]) + " " + str(number)

        else:
            return " ".join(line)
