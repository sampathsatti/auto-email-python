import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    dates = []
    times = []
    names = []
    emails = []
    seqs = []
    """
    This is the index you want to start from
    """
    i = 1
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            dates.append(a_contact.split()[0])
            times.append(a_contact.split()[1])
            names.append(a_contact.split()[2])
            emails.append(a_contact.split()[-1])
            seqs.append(i)
            i = i+1
    return dates, times, names, emails, seqs

def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    dates, times, names, emails, seqs = get_contacts('testcontacts.txt') # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('ubcpotteryclub@gmail.com', 'password')

    # For each contact, send the email:
    for date, time, name, email, seq in zip(dates, times, names, emails, seqs):
        msg = MIMEMultipart()       # create a message

        dtime = date + ' ' + time
        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title(), LINE=seq, TIME_RECD=dtime.title())
        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From'] = 'ubcpotteryclub@gmail.com'
        msg['To'] = email
        msg['Subject'] = "UBC Pottery Club: Token number for filling out the September Waitlist"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()

if __name__ == '__main__':
    main()
