### Implement a program with the following functionality:
- Create class Logging (based on built-in logging) that takes 1 parameter - the name of file to write log to.
The class instance must log data with timestamp to that file and to another AllLogs.log file
- Create a class named ConversionTools, containing 3 methods, with 2 of them running in a separate thread:
   - thread1() - every 1 second writes to file "hex_to_dec.log" a random number in hex and its decimal value in the format: "0x01: 1"
   - thread2() - every 2 seconds writes to file "hex_to_bin.log" a random number in hex and its binary representation in the format: "0x22: 00100010"
   - convert_data() - converts the contents of the file to the format (bin or dec) "0x{hex_number}: {format(hex_number)}"
- Write unit tests for Logging and ConversionTools classes
- Your tests will be run by [pytest](https://docs.pytest.org/en/7.1.x/contents.html)
- Your work must be done in a fork of this repo
- Create pull-request in your fork when you`re done (add reviewers in Settings -> Collaborators)

### Install project
````bash
bash make.sh
````
