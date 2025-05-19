# 🧠 AlgoPro Tracker – A Command Line Problem Tracker in Python

**AlgoPro Tracker** is a beginner-friendly, Python-based command-line application that helps programmers track the coding problems they want to solve, have already solved, or are currently solving. It's perfect for learners who want to build the habit of structured problem-solving and organize their algorithm journey efficiently.

---

## 📌 Features

- ✅ Add new problems to your problem list
- 📖 View all added problems at any time
- ✅ Mark problems as **Solved**
- 🗑️ Delete problems from the list
- 🔍 Filter problems by **status** (Solved/Unsolved)
- 💾 Persistent data storage using a text file (`problems.txt`) — no external libraries or JSON

---

## 🚀 How It Works

1. Run the program in your terminal.
2. Choose from a menu: add problem, view, solve, delete, or filter.
3. Problems are stored in a plain text file for simplicity.
4. The app uses simple file I/O and string operations — no JSON or databases, perfect for beginners!

---

## 📂 File Structure

```
AlgoPro-Tracker/
├── problems.txt       # Stores the list of problems
└── main.py            # Main Python script with all functions
```

---

## 🛠️ Technologies Used

- Python 3.x
- File Handling (`open`, `readlines`, `write`, `append`)
- Functions
- Loops and Conditional Statements

---

## 💡 Why I Built This

As a beginner in Python, I created this project to:
- Practice working with files and functions
- Understand how to structure small command-line tools
- Strengthen my logical thinking before jumping into complex frameworks
- Add a meaningful open-source project to my portfolio

---

## 🎯 What I Learned

- Writing modular code using functions
- Handling input/output and text manipulation
- Building a user-friendly command-line interface
- The power of small but focused utilities in Python

---

## 📸 Sample Demo

```bash
$ python main.py
Welcome to AlgoPro Tracker

1. Add a problem
2. View all problems
3. Mark problem as solved
4. Delete a problem
5. View only unsolved problems
6. Exit

Enter your choice:
This project is open-source and free to use for educational purposes.
