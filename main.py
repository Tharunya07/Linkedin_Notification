# main.py
from linkedin_notification.utils import login_to_linkedin

# Replace with your LinkedIn username and encrypted password through a file in desktop
with open("C:\Users\tharu\OneDrive\Desktop\username.txt") as myUser:
    username= myUser.read().replace('\n', '')
with open("C:\Users\tharu\OneDrive\Desktop\username.txt") as mypass:
    encrypted_password = mypass.read().replace('\n', '')

driver = login_to_linkedin(username, encrypted_password)

from linkedin_notification.utils import retrieve_unread_messages, retrieve_unread_notifications

unread_messages = retrieve_unread_messages(driver)
unread_notifications = retrieve_unread_notifications(driver)

from linkedin_notification.utils import compare_data_with_prev

current_data = [unread_messages, unread_notifications]
comparison_result = compare_data_with_prev(current_data)

email_body = f"""
<html>
<head></head>
<body>
<p>Number of Unread Messages: {unread_messages}</p>
<p>Number of Unread Notifications: {unread_notifications}</p>
<p>Comparison Results:</p>
<ul>
    <li>Unread Messages Change: {comparison_result['unread_messages_change']}</li>
    <li>Unread Notifications Change: {comparison_result['unread_notifications_change']}</li>
</ul>
</body>
</html>
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Read credentials from a different file
sender_email = "tharunyapathipati@gmail.com"
with open("C:\Users\tharu\OneDrive\Desktop\username.txt") as senderpass:
    sender_password = senderpass.read().replace('\n', '')
recipient_email = "tharunya077@gmail.com"

# Create the email message
message = MIMEMultipart("alternative")
message["Subject"] = "Proactive User Notification- LinkedIn"
message["From"] = sender_email
message["To"] = recipient_email
message.attach(MIMEText(email_body, "html"))

# Send the email
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())

# Close the driver
driver.quit()
