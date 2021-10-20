# python_mail_sender
Sending emails manually is a time-consuming and error-prone task, but with Python, it is easy to automate. python_mail_sender.py can be used to send email using python.

In this code, we are going
  - To generate the app password, we will use the generated app password for this Python script instead of exposing the Gmail account password.
  - To setup a secure connection to the SMTP server using _SMTP_SSL()_ and _.starttls()_.
  - And, will use Python's built-in _smtplib_ library to send basic emails.

## **Let's get started**

1. **Create Application Password**: This is a 16-digit passcode that allows a less secure app or device to access our Google Account. This is because we have to adjust the security settings of our Gmail account to allow access from this Python code and because there is a possibility that we may inadvertently expose our login details.
      ###### Create & use App Passwords
      1. Go to your [Google Account](https://myaccount.google.com/).
      2. Select Security
      3. Under "Signing in to Google," select [**App Passwords**](https://myaccount.google.com/apppasswords). You may need to sign in. 
      4. At the bottom, choose Select Other and name it as python_mail_sender.py and then Generate.
      5. Copy the 16 digit password. Use that 16 digit code as a password in the python_mail_sender.py program > Tap Done.
      >  ***Note***: If you don't have the option to choose the app passwords, [2-Step Verification](https://myaccount.google.com/signinoptions/two-step-verification) hasn't been set up for the account. You have to turn it on.
 
 2. **SMTP server**: We are using a Gmail account, Gmail connects to port 465 when using _SMTP_SSL()_, and port 587 when using _.starttls()_.
      > But if you are using a local debugging server, just make sure to use localhost as the SMTP server and use the appropriate port instead of port 465 or 587.
 
 3. **smtplib**: smtplib is Python’s built-in module for sending emails to any Internet machine with an SMTP listener daemon.
