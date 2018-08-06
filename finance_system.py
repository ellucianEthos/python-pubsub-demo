#
# Finance System - this code simulates a finance system collecting parking tickets
#
import time
from ethos import Ethos

API_KEY = '*** finance system api key here ***'

def main():
    print('Starting finance system')

    ethos = Ethos(API_KEY)

    while True:

        print('Checking for change notifications in Ethos Integration')
        data = ethos.get_change_notifications()

        if data and len(data) > 0:
            process_change_notifications(data)
        else:
            print('No change notifications available')

        wait_seconds = 60
        print('Waiting for {seconds} seconds...\n'.format(seconds=wait_seconds))
        time.sleep(wait_seconds)

def process_change_notifications(data):
    print('Received {count} change notifications'.format(count=len(data)))
    for d in data:
        parking_ticket = d['content']
        print('Received Parking Ticket for {first} {last}, Amount ${amount}, License Plate: {plate}'
            .format(first=parking_ticket['firstName'],last=parking_ticket['lastName'],amount=parking_ticket['amount'],plate=parking_ticket['licensePlate']))

if __name__ == '__main__':
    main()
