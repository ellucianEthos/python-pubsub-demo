#
# Parking Ticket System - this code simulates a parking ticket system generating
# and posting parking tickets to Ethos Integration.
#
import random
import time
import string
import uuid
from ethos import Ethos

API_KEY = '*** parking ticket system api key here ***'

def main():
    print('Starting parking ticket system')

    ethos = Ethos(API_KEY)

    while True:
        t = generate_random_parking_ticket()

        print('Generated Parking Ticket for {first} {last}, Amount ${amount}, License Plate: {plate}'
            .format(first=t['firstName'],last=t['lastName'],amount=t['amount'],plate=t['licensePlate']))

        publish_ticket_to_ethos(ethos, t)

        wait_seconds = random.randint(1,20)
        print('Waiting for {seconds} seconds...\n'.format(seconds=wait_seconds))
        time.sleep(wait_seconds)

def generate_random_parking_ticket():
    ticket = create_blank_parking_ticket()

    ticket['firstName'] = random.choice(['Billy','Joey','Jen','Taylor','Marissa','Clay','Chris','Nick','Keith','Wyatt','Christian','Priya'])
    ticket['lastName'] = random.choice(['Smith','Johnson','Williams','Brown','Jones','Miller','Davis','Garcia','Rodriguez','Wilson'])
    ticket['amount'] = random.choice([25,50,75,100])
    ticket['licensePlate'] = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
    ticket['parkingTicketId'] = str(uuid.uuid4())

    return ticket

def create_blank_parking_ticket():
    return {'parkingTicketId':'', 'firstName' : '', 'lastName': '', 'licensePlate': '', 'amount': 0}

def create_blank_change_notification():
    return { 'resource' : {'name':'', 'id':''},'operation': '','contentType':'','content': None}

def publish_ticket_to_ethos(ethos, parking_ticket):
    print('Publishing change-notification to Ethos Integration')
    change_notification = create_blank_change_notification()

    change_notification['operation'] = 'created'
    change_notification['contentType'] = 'resource-representation'
    change_notification['resource']['name'] = 'parking-tickets'
    change_notification['resource']['id'] = parking_ticket['parkingTicketId']
    change_notification['content'] = parking_ticket

    print(change_notification)
    ethos.send_change_notification(change_notification)

if __name__ == '__main__':
    main()
