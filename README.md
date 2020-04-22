# bes_automated_testing

I wrote this simple Python script to help with testing Chat Bot applications. This is especially useful if you want to test the Chat Bot against a LOT of keywords. This is still bare and simplified, but it already helped me save a lot of effort and time. As always, it can be improved anyway.

The testing setup uses Selenium and Python. 

Here's how to do it:

## Install ChromeDriver.

Grab `chromedriver_32.zip` from https://sites.google.com/a/chromium.org/chromedriver/downloads.
Unzip the file and place `chromedriver.exe` to a location specified in your `PATH`.

## Install Selenium.

`pip install selenium`

## Write your Python test script.

For example, see chat-bot-tester.py.
