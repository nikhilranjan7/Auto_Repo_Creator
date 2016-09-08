#! /usr/bin/env python3
# new_repo.py - create a new repository with first command line argument as its name and second
# one to choose between private and public mode.
# run it like *** python3 new_repo.py repo_name private
# replace ##username and ##password by your github credentials

from selenium import webdriver
import sys

browser = webdriver.Firefox()
browser.get('https://github.com/login')
username = browser.find_element_by_id('login_field')
username.send_keys('##username')
password = browser.find_element_by_id('password')
password.send_keys('##password')
password.submit()
repo = browser.find_element_by_link_text('New repository')
repo.click()

# filling repository info

name = browser.find_element_by_id('repository_name')
name.send_keys(' '.join(sys.argv[1:2]))


mode = ' '.join(sys.argv[2:])

if mode == 'private':
    private = browser.find_element_by_id('repository_public_false')
    private.click()

name.submit()

print('Done')
browser.close()
