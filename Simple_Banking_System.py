import random

class Card:
  def __init__(self):
    self.number = self.new_card_number()
    self.pin = self.new_card_pin()
    self.balance = 0

  def new_card_number(self):
    account_number = str(random.randint(000000000, 999999999))
    if len(account_number) < 9:
      account_number = '0' * (9 - len(account_number)) + account_number
    account_number = '400000' + account_number
    return account_number + self.luhn_alg(account_number)

  def luhn_alg(self, number):
    summ = 0
    for i in range(1, 16):
      if i % 2 == 1:
        digit = int(number[i-1]) * 2
        if digit > 9:
          digit -= 9
        summ += digit
      else:
        summ += int(number[i-1])
    if summ % 10 == 0:
      checksumm = 0
    else:
      checksumm = 10 - summ % 10
    return str(checksumm)

  def new_card_pin(self):
    account_pin = str(random.randint(0000, 9999))
    if len(account_pin) < 4:
      account_pin = '0' * (4 - len(account_pin)) + account_pin
    return account_pin

  def check_inf(self, number, pin):
    if self.number != number or self.pin != pin:
      print('\nWrong card number or PIN!\n')
    else:
      print('\nYou have successfully logged in!\n')
      return True

  def balances(self):
    print('\nBalance: ', self.balance, '\n')



client_choice = int(input('1. Create an account\n2. Log into account\n0. Exit\n'))
cards = []
while client_choice != 0:
  
  if client_choice == 1:
    client_card = Card()
    cards.append(client_card)
    print('\nYour card has been created')
    print('Your card number:')
    print(client_card.number)
    print('Your card PIN:')
    print(client_card.pin)
    print('\n')

  elif client_choice == 2:
    card_number = input('\nEnter your card number:\n')
    card_pin = input('Enter your PIN:\n')
    if client_card.check_inf(card_number, card_pin) == True:
      client_balance = input('1. Balance\n2. Log out\n0. Exit\n')
      if client_balance == '0':
        break
      while True:
        if client_balance == '1':
          client_card.balances()
        elif client_balance == '2':
          print('\nYou have successfully logged out!\n')
          break
        client_balance = input('1. Balance\n2. Log out\n0. Exit\n')

  client_choice = int(input('1. Create an account\n2. Log into account\n0. Exit\n'))

print('\nBye!')
