Fibonacci backend test code

This project consists of
test_be.py = main REST API test code

Everything has been set up to run with an API which can be found at:  http://13.59.70.88/:5000/api/fibonacci/<num>

#In order to run the tests you need to execute the following command from Linux system

python -m pytest -v test_be.py

#If you want to generate a Final_test_report.xml file run the code

python -m pytest -v test_be.py --junitxml=Final_test_report.xml

# to generate a results.log file run the code

python -m pytest -v test_be.py >results.log






