### Implement a program with the following functionality:
- Create a class named Logging, which will inherit the properties and methods from the logging class.
- This class takes 1 parameter - the name of the file to which the text will be written.
- The class Instance must log data to this file and to the allLogs.log
- Create a class named conversionTools, which contains 2 methods that are run in separate thread:
   - thread1 method, which every 10 seconds writes to self.logger_hex_to_dec a random number in hex and its decimal value in the format: "0x01: 1"
   - thread2 method, which every 20 seconds writes to self.logger_hex_to_bin a random number in hex and its binary representation in the format: "0x22: 00100010"
   - logger_hex_to_bin and logger_hex_to_dec - Logger instances
   - convertData method that takes 2 parameters: filePath - path and name to the file, format - numeric system (bin or dec) and converts the content of the file to the format "0x{hex_number}: {format(hex_number)}"
- Write unit tests for Logging and conversionTools classes
- Your tests will be run by [pytest](https://docs.pytest.org/en/7.1.x/contents.html)
- Your work must be done in a fork of this repo
- Make sure only reviewers have access to your code (Settings -> Collaborators)
- Create pull-request in your fork when you`re done

### Install project
````
- poetry install
or
- bash make.sh
````
