# auto-email-python

This repo was created by Sampath for the UBC pottery club based off a few automated email scripts found on the internet.

## Files

#### main.py

The main python code is in the `main.py` file. This is where all the magic happens.

#### message.txt

This desired email template can be placed at `message.txt`. The parts that need to be changed in each email such as the recipient's name, position in queue, time of submission etc are denoted by `${VARIABLE}` in string literal form.

#### textcontacts.txt

The list of contacts that the emails need to be send to are in the `contacts.txt`, or `testcontacts.txt` files. These files can be obtained by extracting the following columns from the filled out excel sheet -

1. Date-Time
2. Name
3. Email Address

The `main.py` expects the `contacts.txt` file to be in the above format, or else the code may not work as expected.

## How to run this

#### Verify message.txt, contacts.txt

Ensure that your message template and contacts.txt adhere to the aforementioned formats.

#### Less secure app access

For this script to work, you need to allow the app to send emails on behalf of ubcpotteryclub@gmail.com. To prevent email-spoofing gmail doesn't not let external unverified apps do this. Follow [these](https://support.google.com/accounts/answer/6010255?) instructions here to turn on **Less Secure App Access** when you send these emails out. **DO NOT FORGET** to turn it back off again once these emails have been sent out.

#### Test email yourself before emailing actual individuals

Giving folks false hope that they have a chance of getting in is the worst. Check and triple check that the script works as you expect it to by emailing yourself and other members of the exec. You can use a `testcontacts.txt` file and pass that to the python script on line 45.

#### Use the correct sequence index

The sequence index, `i` marks an individual's position in the queue. The first time the script is run, when you want to start sending the emails from the first row in the `contacts.txt` file, the value of `i` is 1.

Sometimes, when there are >100 people that have filled the form, running the script will only send out 50 or so emails before gmail shuts the script down suspecting spamming. At that point, check the console logs to see what the last send email was and note the sequence number. Delete all rows to which a successful email was sent. Run the script with this new value of `i` to keep sending emails to remaining people in the `contacts.txt` file.

Rinse, lather and repeat.

#### Email credentials

Confirm and check if email credentials on line 51 of `main.py` are correct. 

#### Running the python command

If you have python installed `python main.py` should be enough to run the script. If you don't code much and aren't comfortable with command line interfaces, download [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) community IDE and run the script through that!