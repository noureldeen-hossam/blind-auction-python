# 🔨 Blind Auction

A simple **Blind Auction** program built with Python 🐍 that collects bids from multiple bidders and determines who placed the highest bid.

---

## ✨ Features

* 👤 Takes the name of each bidder
* 💰 Collects a bid amount from each participant
* 📦 Stores names and bids using a Python dictionary
* 🔁 Allows multiple participants to enter their bids
* 🔒 Clears the terminal between bidders for privacy
* 🏆 Identifies the highest bidder
* 💻 Runs directly in the terminal

---

## 🧠 How It Works

The program follows a simple process:

```text
        👤 Bidder's Name
               +
        💰 Bid Amount
               │
               ▼
      📦 Store Name and Bid
          in a Dictionary
               │
               ▼
      ❓ Any Other Bidders?
          /           \
        Yes             No
         │               │
         ▼               ▼
  🧹 Clear Screen    🔍 Compare Bids
         │               │
         └── Repeat      ▼
                   🏆 Find Highest Bid
                          │
                          ▼
                    🎉 Announce Winner
```

### Example

Suppose three people participate in the auction:

| Bidder  | Bid |
| ------- | --: |
| Ahmed   | 200 |
| Mohamed | 500 |
| Ali     | 350 |

The program compares their bids and determines the winner.

```text
The winner is Mohamed with a bid of 500
```

---

## 🚀 Example

### Input

```text
What's your name?
Ahmed

What is your bid?
200

Are there any other bidders? Type 'yes' or 'no'.
yes
```

The program continues collecting bids until the last participant enters `no`.

### Output

```text
The winner is Mohamed with a bid of 500
```

---

## 🛠️ Technologies Used

* 🐍 Python
* 📦 Dictionaries
* 🔁 `while` loops
* 🔄 `for` loops
* ❓ `if` statements
* ⚙️ Functions
* ⌨️ `input()`
* 🔠 `.lower()`
* 📊 Comparison operators
* 📂 Python modules

---

## 📚 What I Learned

This project helped me practice:

* Creating and calling functions
* Working with dictionaries to store data
* Using loops to process multiple bidders
* Comparing values to find the highest bid
* Using conditional statements to control program flow
* Collecting user input
* Using a separate Python module to store ASCII art
* Combining multiple Python concepts to build a complete program

---

## 📂 Project Structure

```text
Blind-Auction/
│
├── main.py
├── art.py
└── README.md
```

---

## 📸 Project Preview

```text
          ___________
          \         /
           )_______(
           |"""""""|
           | BLIND |
           |AUCTION|
           |_______|

================================
       🔨 BLIND AUCTION 🔨
================================

What's your name?
Mohamed

What is your bid?
500

Are there any other bidders? Type 'yes' or 'no'.
no

The winner is Mohamed with a bid of 500
```

---

## 🎯 Project Status

**Completed ✅**

This is a beginner Python project created as part of my journey to improve my programming and problem-solving skills.

---

## 👨‍💻 Author

**Nour Eldeen**

Python Developer 🐍 | Building Projects 🚀 | Improving Every Day 📈

---

⭐ If you found this project interesting, feel free to star the repository!
