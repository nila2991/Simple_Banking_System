import random
import sqlite3

class Card:
  def __init__(self):
    self.id = self.new_card_id()
    self.number = self.new_card_number()
    self.pin = self.new_card_pin()

  def new_card_id(self):
    account_id = str(random.randint(000000000, 999999999))
    if len(account_id) < 9:
      account_id = '0' * (9 - len(account_id)) + account_id
    return account_id

  def new_card_number(self):
    account_number = '400000' + self.id
    return account_number + luhn_alg(account_number)

  def new_card_pin(self):
    account_pin = str(random.randint(0000, 9999))
    if len(account_pin) < 4:
      account_pin = '0' * (4 - len(account_pin)) + account_pin
    return account_pin


def luhn_alg(number):
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

def check_inf(number, pin):
  if number not in all_client_cards or all_client_cards[number] != pin:
    print('\nWrong card number or PIN!\n')
  else:
    print('\nYou have successfully logged in!\n')
    return True

def client_balance(number):
  cur.execute('SELECT * FROM card WHERE number = ?;', (number, ))
  conn.commit()
  r = cur.fetchone()
  return r[3]

def client_income(number, income):
  cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?;', (income, number))
  conn.commit()

def client_decline(number, summ):
  cur.execute('UPDATE card SET balance = balance - ? WHERE number = ?;', (summ, number))
  conn.commit()

def transfer(number_from, number_to):
  cur.execute('SELECT * FROM card WHERE number = ?;', (number_to, ))
  conn.commit()
  existence = cur.fetchall()
  if number_from == number_to:
    print("You can't transfer money to the same account!\n")
  elif luhn_alg(number_to[0:15]) != number_to[15]:
    print('Probably you made a mistake in the card number. Please try again!')
  elif len(existence) == 0:
    print('Such a card does not exist.')
  else:
    print('Enter how much money you want to transfer:')
    money = int(input())
    if client_balance(number_from) < money:
      print('Not enough money!')
    else:
      print('Success!')
      client_income(number_to, money)
      client_decline(number_from, money)

def close_account(number):
  cur.execute('DELETE FROM card WHERE number = ?;', (number, ))
  conn.commit()
  del all_client_cards[number]


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

#cur.execute('DROP TABLE card')
cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
conn.commit()
client_choice = int(input('1. Create an account\n2. Log into account\n0. Exit\n'))
all_client_cards = {}
while client_choice != 0:

  if client_choice == 1:
    client_card = Card()
    cur.execute('SELECT * FROM card WHERE number = ?;', (client_card.number, ))
    conn.commit()
    rows = cur.fetchall()
    while len(rows) != 0:
      client_card = Card()
      cur.execute('SELECT count(*) FROM card WHERE number = ?;', (client_card.number, ))
      conn.commit()
      rows = cur.fetchall()
    all_client_cards[client_card.number] = client_card.pin
    cur.execute('INSERT INTO card (number, pin) VALUES (?, ?)', (client_card.number, client_card.pin))
    conn.commit()
    #cur.execute('SELECT id, number, pin, balance FROM card')
    #print(cur.fetchall())
    #cards.append(client_card)
    print('\nYour card has been created')
    print('Your card number:')
    print(client_card.number)
    print('Your card PIN:')
    print(client_card.pin)
    print('\n')

  elif client_choice == 2:
    card_number = input('\nEnter your card number:\n')
    card_pin = input('Enter your PIN:\n')
    if check_inf(card_number, card_pin) == True:
      client_act = input('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n')

      while client_act != '0':
        if client_act == '1':
          print('\nBalance: ', client_balance(card_number))

        elif client_act == '2':
          print('\nEnter income:')
          income = int(input())
          client_income(card_number, income)
          print('Income was added!')

        elif client_act == '3':
          print('\nTransfer\nEnter card number:')
          number_to = input()
          transfer(card_number, number_to)

        elif client_act == '4':
          print('\nThe account has been closed!\n')
          close_account(card_number)
          break

        elif client_act == '5':
          print('\nYou have successfully logged out!\n')
          break

        client_act = input('\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n')
      if client_act == '0':
        break

  client_choice = int(input('1. Create an account\n2. Log into account\n0. Exit\n'))

print('\nBye!')
