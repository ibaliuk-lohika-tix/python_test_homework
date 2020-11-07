# homework from interview for INTELLIAS company

Given next objective:
```
As a final solution, we expect a working function/method
and passing test cases, that test this function/method.
 
Please create a function/method that will get
on an input a path to a file destination
and N integer number. This method on the
output should print N last lines from file
in the correct order.
 
Please create test cases which will
test the previously written function/method
```


#### To install packages which are required go to project directory and execute command:
```
"pip install req"
```

# How to run tests
#### Go to project directory and execute command:
```
"py.test -v"
```

# How to set non-default variables
Open test_profile.json where you can set:
- "file_path" for file  with  strings that should be readed and sorted
- "error_message" text for expected message  that you expecting as a output for negative scenarios
- "result" file where will be stored result of  method calculation (needed for solution where "print" are mandatory Option)
#### Please keep in mind that method or app that we are testing have his own profile  version (./app/app_profile.json)
#### So for correct testing both profiles should contain equal data
