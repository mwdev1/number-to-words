# numbers_to_words/cli

numbers_to_words.py is a command-line interface (CLI) tool that takes an integer from 0 to 100,000 and converts it into grammatically correct English words. 

## Documentation

The following points describe the program behaviour:

* The solution will reject numbers outside of the expected range which is 0 to 100,000
* The expected range can be extended by modyfying MAX_NUMBER variable inside the script.
* Negative numbers are currently not supported but this feature could be easily added.
* The program uses standard streams and exit codes

## Usage

The script requires Python programming language interpreter to be available:
https://www.python.org/downloads/

To run the script, run the following command from the command line:

> ./bin/py numbers-to-words.py [number]

The script will give the outputs as the below examples:
~~~
./bin/numbers-to-words 52
fifty-two

./bin/numbers-to-words 1000
one thousand

./bin/numbers-to-words 101
one hundred and one

./bin/numbers-to-words 352
three hundred and fifty-two

./bin/numbers-to-words 12300
twelve thousand, three hundred

./bin/numbers-to-words 12055
twelve thousand and fifty-five

./bin/numbers-to-words 12345
twelve thousand, three hundred and forty-five
~~~
**Error scenarions:**

* The script will **exit with 1 code** if the expected number argument is invalid or missing.
* The script will **exit with 2 code** if the provided number is not with the expected range which is by default 0 to 100,000. The upper limit can be configured inside the script by modyfying the MAX_NUMBER variable.

After exiting the script with sys.exit(), the exit code can be accessed by the calling process. 
For example, if you run the Python script from the command line, you can check the exit code with the **echo %errorlevel%** command in Windows or **echo $?** in Unix-like systems (Linux, macOS).

