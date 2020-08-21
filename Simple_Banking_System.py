import random

class Card:
  def __init__(self):
    self.number = None
    self.pin = None
    self.balance = 0


  def new_card(self):
    account_number = str(random.randint(0000000000, 9999999999))
    if len(account_number) < 10:
      account_number = '0' * (10 - len(account_number)) + account_number
    self.number = '400000' + account_number

    self.pin = str(random.randint(0000, 9999))
    if len(self.pin) < 4:
      self.pin = '0' * (4 - len(self.pin)) + self.pin


  def check_inf(self, number, pin):
    if self.number != number or self.pin != pin:
      print('\nWrong card number or PIN!\n')
    else:
      print('\nYou have successfully logged in!\n')
      return True


  def balances(self):
    print('\nBalance: ', self.balance, '\n')



client_choice = int(input('1. Create an account\n2. Log into account\n0. Exit\n'))

while client_choice != 0:
  
  if client_choice == 1:
    client_card = Card()
    client_card.new_card()
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
