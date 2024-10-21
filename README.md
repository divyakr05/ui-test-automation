# ui-test-automation
This is simple ui-test-automation project created to test sample flows for airalo application, using Playwright Framework (Python, playwright, PyTest, Page Object Model, HTML Reports)

# Setup Instructions
- Clone the project https://github.com/divyakr05/ui-test-automation
- Install python on your system. Download it from python.org
- Install playwright:
     pip install playwright
     playwright install
- Install pytest and pytest-html:
    pip install pytest
    pip install pytest-html
- Open the project in any IDE
- To execute the tests and generate the HTML report, run the following command in your terminal:
    pytest
After running the tests, you will find a report_home.html file inside the root directory. Open this file in a web browser to view a detailed report of the test results.
  
# Folder Structure
ui-test-automation framework/
├── tests/
│   └── home_test.py
    └── base_test.py
├── pages/
│   └── home_page.py
    └── base_page.py
├── utilities/
│   └── read_config.py
├── config.json
├── conftest.py
└── pytest.ini

config.json File -->  file to store your configuration settings
read_cofig.py --> file in the utilities directory. This file is to read the config.json file
pytest.ini --> file to configure pytest
conftest.py --> file to setup and teardown
base_page.py --> file in the pages directory. This file will define a base class for all page objects
home_page.py --> file in the pages directory. This is to create page object for home page
base_test.py --> file in the tests directory. This file will define a base class for all test cases
home_test.py --> test cases are created in this file

Approach to implement the testcase:
Created a test case "test_verify_package_details" in home_page.py
This will automate the following test steps:
    1. Launch a browser and navigate to airalos website
    2. Type 'Japan' in the search field on the home page, select the destination from the “Local” section in the autocomplete options
    3. On the next page, choose the first eSIM package, and click on the Buy Now button
    4. Verify Package Details in the popup that appears, assert the following details are accurate:
        ■ Title: Moshi Moshi
        ■ Coverage: Japan
        ■ Data: 1 GB
        ■ Validity: 7 days
        ■ Price: $4.50
Note : The verification will fail for Price. The actual value from UI is '4.50€'. It is verified against '$4.50' as the instructions provided
    
  
