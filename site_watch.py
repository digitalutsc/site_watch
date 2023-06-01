#!/usr/bin/python3

import sys
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By

# Read the ASCII logo from a file and print it to the console in yellow
with open("logo.txt", "r") as f:
    logo = f.read()
print(colored(logo, "yellow"))