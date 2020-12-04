#!/usr/bin/env python
# coding: utf-8

# ##### Coded By Harshanthi

#Make sure the Excel you will be working with is in your current working directory
import os 
os.getcwd()
#this changes our CWD, if the excel sheet is not in CWD
#os.chdir('C:\\Users\\harsh\\Ismile Technologies\\Restaurant Management') 

#work on excel sheet
import openpyxl
import xlrd

# Import smtplib for the actual sending function
import smtplib, ssl
from string import Template
# Import the email modules we'll need
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage

import pandas as pd
import re

global sender_email 
sender_email = 'rgeddam96@gmail.com'
global password
password = 'marutihonda'

file = 'donation.xls'
data = pd.read_excel(file)

#reading each sheet1 from the excel, i.e, dishesList
dishesList = pd.read_excel(file, sheet_name=0, index_col=0)


#exploring the data
dishesList.shape


#Gives all the dishes who's quantity is above 1000 grams
donationItems = dishesList.loc[dishesList['Quantity(grams) Dishes left at( 8:00 PM )'] >= 3000,['Menu items','Quantity(grams) Dishes left at( 8:00 PM )']]

donationItems.shape


# Convert the dataframe to Excel object. 
donationItems.to_excel('leftOvers.xlsx',index=False,header=True)


leftOverFile = 'leftOvers.xlsx'

#reading each sheet2 from the excel, i.e, email details(mycontacts) given names and email address
mycontacts = pd.read_excel(file, sheet_name=1, header=0,dtype={'Name':str,'Email':str})
mycontacts.head()


mycontacts.columns
receiver_email = mycontacts['Email']
receiver_email.dtype


#reading each sheet3 from the excel, i.e, email body message
messages = pd.read_excel(file, sheet_name=2,header=0,dtype={'Item_No':int,'message_template':str})
messages.head()

#messages.index
messages.columns
messageDonation = messages['message_template']
messageDonation.dtype


def sendEmail():
    #creating an SMTP secure instance that encapsulates an SMTP connection
    connection = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)


    # create and send a simple text message through email



    # Create the container email message.
    msg = EmailMessage()


    msg['Subject'] = 'Donation of excess food'
    #The email address of sender
    msg['From'] = sender_email
    #Send email address of reciever

    #maybe use a for loop here to send emails to several receivers
    msg['To'] = receiver_email[2]
    print(msg['To'])
    msg.set_content(messageDonation[0])


    with open(leftOverFile, 'rb') as f:
        leftOverFile_data = f.read()
    msg.add_attachment(leftOverFile_data,maintype="application", subtype="xlsx", filename=leftOverFile)


    #https://support.google.com/mail/thread/23341254?hl=en
    connection.login(sender_email, password)


    connection.send_message(msg)

