# TestAutomation.Python

These are the python automation tests.




## GETTING STARTED

These instructions will get you a copy of the project up and running on your 
local machine for development and testing purposes.

### STEP 1: INSTALLING PYTHON3

Python3 is the language that is used for this repo. Instructions on getting it 
set up can be found here:

http://docs.python-guide.org/en/latest/starting/installation/

### STEP 2: INSTALLING REQUIRED PYTHON3 MODULES

Required Python3 modules are listed in the 'requirements.txt' file. Via  
terminal, install all of these requirements using the 'requirements.txt' file,
by using the following command:

```
pip3 install -r {{path_to_requirements.txt}}
```

Verify they appear in the list (additional pre-req modules may have been 
installed):

```
pip3 list
```

NOTE, that if you get the following error:

```
Could not install packages due to an 
EnvironmentError: [Errno 13] Permission denied: '/usr/local/man'
Consider using the `--user` option or check the permissions.
```

You should run the install with a --user flag:

```
pip3 install --user -r {{path_to_requirements.txt}}
```

### STEP 3: GRAB A COPY OF THE REPO

The repo can be grabbed from Bitbucket.

Run the following git command, to create a local copy of the repo in your
current working directory:

```
git clone {{repo_url}}
```

### STEP 5: SETTING UP THE CONFIG.PY FILE

This file is not added to the repo, due to containing sensitive information. An
example of this file can be found on the following file. Simply create a copy 
of the file, rename it to be "config.py", and fill in the required fields.

```
../testautomation/python/example.config.py 
```

### STEP 6: EXPLANATION OF LAYOUT

The Page Object Model testing strategy is being used. Each page/feature has the 
following:

(a) method/module files

(b) test files

(c) variables files

Method/module files contains relevant code related to each of the features. The 
majority of action code lives here.

Test files contain the execution code for each test, and tests can be 
configured here.

Variable files contain any relevant variables needed to complete the tests. This
file is shared between multiple features.

Log files are automatically created, and keeps track a log of the automation.
These live in the log folder.

### STEP 7: HOW TO RUN THE TESTS

Run all tests in a folder using the following command:

```
pytest {{path_to..}}/python/eapi/tests/
```

Specify which tests to run by specifying the test file to run:

```
pytest {{path_to..}}/python/eapi/tests/test_heartbeats.py
```

NOTE, that you can run tests without the pytest command, but there are 
additional steps required. This is the easiest method of running tests.

### STEP 8: HOW TO RUN THE TESTS, WITH JUNIT XML OUTPUT

Additionally, the pytest has built-in functionality which supports outputting 
to a JUnit XML format. This can help in integration with Bamboo logs. To do 
this, use the following command while running the tests:

```
pytest {{path_to..}}/python/eapi/tests/ --junitxml={{path_to_log_file.xml}}
```

### STEP 9: HOW TO RUN THE TESTS, WITH TEST COVERAGE OUTPUT

Also, there is a pytest library which allows for outputting of test coverage, 
"pytest-cov". This library is included in the requirements.txt file. This can 
help in integration with Bamboo logs. To do this, use the following command 
while running the tests:

```
pytest --cov={{path_to..}}/python/eapi/tests/ {{path_to..}}/python/eapi/tests/ 
    --junitxml=test_junit.xml
```




## RUNNING CODE IN A VIRTUAL ENVIRONMENT (OPTIONAL)

It is suggested that you run/install the Automation in a Virtual Environment 
(abbreviated as venv). However, this is NOT a requirement. These instructions 
will help you get up and rolling with one.

VENVs are useful, as they allow you to test your code free from other 
dependencies.

### STEP 1: INSTALLING REQUIRED PYTHON3 MODULES

A 'virtualenv' library exists as a module for Python3. It should have been 
installed already, via the 'requirements.txt' file installation listed above. 
However, if not, then the following command line can be run to install it
manually:

```
pip3 install virtualenv
```

### STEP 2: CREATE THE VENV

Navigate to the target folder where you want the venv to live. Then, run the 
following terminal command, to create the venv in your current working 
directory:

```
python3 -m virtualenv {{name_of_your_venv}}
```

That's it. You now have a venv ready for use!

### STEP 3: ACTIVATING AND DEACTIVATING YOUR VENV

To start off with, locate your venv folder. Within the main venv parent 
folder, there will be a child folder called 'bin'. Within the 'bin' child 
folder, there is a file named 'activate'. NOTE, that there are multiple
'activate' files. The one you want is the one without a file extension.

Once you know where the file is, run the following terminal command, to start
your venv:

```
source {{path_to_venv}}/bin/activate
```

This command will automatically start your venv, and put you into your venv.

To exit the venv, simply type this command while in the venv:

```
deactivate
```

You should now be removed from the venv, and back in your normal shell.
