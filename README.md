# Job Application Email Script

This is a Python script for sending job applications via email. It reads email addresses and company names from a file, and sends personalized job application emails with attachments.

## Prerequisites

- Python 3.x installed
- SMTP server details (e.g., Gmail SMTP server)

## Setup

1. Clone the repository or download the script file.
```
git clone https://github.com/pratikranaa/Job-apply-email-loop.git
```

3. Create a file named credentials.txt in the same directory as the script. Enter your email address and password on separate lines, like this:
  ```
  your_email@example.com
  your_password
  ```
Note: Make sure to keep this file private and secure. Add credentials.txt to your .gitignore file to exclude it from version control.

3. Prepare your email list file (email_list.txt):

Create a text file named email_list.txt in the same directory as the script.

Each line should contain an email address and the corresponding company name, separated by a comma. Example:
```
john@example.com, Example Company
jane@example.com, Another Company
```
4. Customize the email content:

Open the script file and locate the subject and body variables.
Modify the subject line and email body to suit your needs. You can use placeholders like {company_name} to dynamically insert the company name from the email list file.

5. Place the attachment file:

Ensure that the attachment file is in the same directory as the script.
Update the attachment_path variable in the script with the correct file name.

## Usage

6. To run the script and send job application emails, execute the following command:

```
python3 email_script.py
```
The script will read the email addresses and company names from email_list.txt, personalize the email content, and send the job application emails with the specified attachment.

Note: Make sure you have a stable internet connection and that the SMTP server details (e.g., server address, port) are correctly configured in the script.
