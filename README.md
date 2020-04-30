# Too Lazy To Do It Manually

I wrote these simple Python scripts to automate the tasks I used to do manually.

For example, `chat-bot-tester.py` helped me test chat bot applications. Since I need to test the chat bots against a LOT of keywords, this has been very useful and helped me uncover bugs.

The script `download-payslips` allowed me to download all my payslips from our company's payroll management website. Also, `encode-timesheet` encodes my timesheet in our portal.

The scripts are relatively bare and simplified, but they already saved me a lot of effort and time. Also, these scripts cover the basics of web automated testing and can already serve as a groundwork for bigger projects.

The testing setup uses Selenium and Python. 

Here's how to do it:

## Install ChromeDriver.

Grab `chromedriver_32.zip` from https://sites.google.com/a/chromium.org/chromedriver/downloads.
Unzip the file and place `chromedriver.exe` to a location specified in your `PATH`.

## Install Selenium.

`pip install selenium`

## Write your Python test script.

See the sample test scripts.