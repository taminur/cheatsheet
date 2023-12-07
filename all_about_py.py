#Project 1: to manage files

import shutil
import os
import frontmatter

# List of frontmatter properties with folder destinations
frontmatter_to_dir = {
    'project': '1. Projects',
    'area': '2. Areas',
    'resource': '3. Resources',
}

def try_move_file(file, destination):
    print('- Moving file', file, "to", destination)
    try:
        shutil.move(file, destination)
    except Exception as err:
        print('-  - Project not found', err)


# Read all the files inside the "!inbox" directory
notes = os.listdir('!inbox')
for note in notes:
    note_path =  f"!inbox/{note}"
    # Read the file's frontmatter
    note_metadata = frontmatter.load(note_path)
    
    # Check if the file has a property to categorize this note,
    # for example: project, area, or resource
    for group, group_destination in frontmatter_to_dir.items():
        if group in note_metadata:
            # Try moving the file, it can be the case the project is
            # for example mispelled, in that case it won't do anything with the note
            try_move_file(note_path, f"{group_destination}/{note_metadata[group]}/{note}")


#########################

# Project2: Data extraction

import requests
from bs4 import BeautifulSoup

# Load the newspapaer website to scrap information about the current exchange rate for USD/ARS
URL = 'https://www.lanacion.com.ar/'
page = requests.get(URL)

# Parse the HTML data
soup = BeautifulSoup(page.content, "html.parser")
# Use select to find an element in the DOM
# In our case, we need a span inside a link with a specific title
span = soup.select('a[title="Dólar blue"] span')[0]
price = span.get_text()
# In a real scenario, instead of simply printing the price,
# I'd for example, email me the results or do some other processing
print(price) # e.g. $930,00

#####################

# Project3: sending email

import boto3
import json

# All email addresses where store in s3
s3_bucket = ''
# Provide the path to your file in the S3 bucket
s3_key = 'mail_list/addresses.txt'

s3_client = boto3.client('s3')
# Retrieve the email ids from the file
s3_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
email_ids = s3_object['Body'].read().decode('utf-8').split('\n')

# Send email for each email ID
ses_client = boto3.client('ses')
for email_id in email_ids:
	email_id = email_id.strip() # Remove leading/trailing whitespace
	
	# Perform email sending operations using SES client
	response = ses_client.send_email(
		Source='<FromAddress>',
		Destination={'ToAddresses': [email_id]},
		Message={
			'Subject': {'Data': 'Your Subject'},
			'Body': {'Text': {'Data': 'Your Email Body'}}
		}
	)

print(f"Email sent to {email_id}. Message ID: {response['MessageId']}")

############

#Project4: Application testing

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set the driver to use Firefox, can also be Chrome, IE, and Remote
driver = webdriver.Firefox()
# Load the target website
driver.get("http://www.python.org")
# Validate that the page loaded by comparing the page title
assert "Python" in driver.title
# Find the search input element by name
elem = driver.find_element(By.NAME, "q")
# Empty it
elem.clear()
# Type `pycon`
elem.send_keys("pycon")
# Press an enter to trigger the search form
elem.send_keys(Keys.RETURN)
# Validate that the text `No results found.` is not present in the page
assert "No results found." not in driver.page_source
# Close the browser
driver.close()