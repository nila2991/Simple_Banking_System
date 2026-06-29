# Simple Banking System (Hyperskill)

This repository contains my solution for the Simple Banking System project from Hyperskill (JetBrains Academy). The application simulates a real-world banking backend, allowing users to create accounts, manage card balances, and securely transfer funds.

## 🛠️ Tech Stack & Features
* Language: Python
* Database: SQLite (SQL connectivity via JDBC/sqlite3)
* Core Concepts: Object-Oriented Programming (OOP), Luhn Algorithm for card generation, Database Management, Data Integrity.

---

## 🚀 Key Functionality

* Card Generation: Automatically generates a 16-digit card number with a valid Bank Identification Number (BIN) and checks validity using the Luhn Algorithm.
* Secure PIN: Generates a random 4-digit PIN for every new account.
* Database Persistence: All account credentials and balances are securely stored and updated in an SQLite database.
* Banking Operations: 
  * Check account balance
  * Deposit/Add income
  * Transfer money to another account (with full validation of the target card number)
  * Close/Delete account

---

## 📅 Project Progress

* Stage 1: Card generation —  Completed
* Stage 2: Luhn algorithm —  Completed
* Stage 3: I'm a database man —  Completed
* Stage 4: Advanced system —  Completed
