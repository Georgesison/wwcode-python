""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

bill = input('How Much is Your Bill? : ')

payment = input('How Much is Your Payment? : ')

Change = int(payment) - int(bill)

print('Hi! Your Change is '+str(Change))