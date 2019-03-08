This code will start a web server when executed from the command line, relying on a venv noted in the first line of the executable.

The command is (sudo must be used to utilize port 80):

sudo ./app.py


A GET request can then be sent to the localhost with parameters 'begin' and 'end', and FizzBuzz results will be returned, e.g.
http://localhost/fizzbuzz?begin=0&end=100

fizz,1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizz,16,17,fizz,19,buzz,fizz,22,23,fizz,buzz,26,fizz,28,29,fizz,31,32,fizz,34,buzz,fizz,37,38,fizz,buzz,41,fizz,43,44,fizz,46,47,fizz,49,buzz,fizz,52,53,fizz,buzz,56,fizz,58,59,fizz,61,62,fizz,64,buzz,fizz,67,68,fizz,buzz,71,fizz,73,74,fizz,76,77,fizz,79,buzz,fizz,82,83,fizz,buzz,86,fizz,88,89,fizz,91,92,fizz,94,buzz,fizz,97,98,fizz,buzz

