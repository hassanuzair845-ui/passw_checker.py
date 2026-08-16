# 🔐 Password Strength Checker

A simple Python program that checks the strength of a user's password and classifies it as **Weak, Medium, or Strong** based on different conditions.

## 📌 Project Description

This project is designed to practice Python **string methods, loops, Boolean variables, and conditional statements**.

The program asks the user to enter a password and checks:

* Password length
* Presence of a number
* Presence of an uppercase letter

Based on these conditions, the password is classified as **Weak**, **Medium**, or **Strong**.

## 🚀 How It Works

The program follows these rules:

| Condition                                                              | Result |
| ---------------------------------------------------------------------- | ------ |
| Password has fewer than 6 characters                                   | Weak   |
| Password has 6+ characters but is missing a number or uppercase letter | Medium |
| Password has 6+ characters, a number, and an uppercase letter          | Strong |

## 🧠 Concepts Practiced

* `input()`
* `len()`
* `for` loops
* `if / elif / else`
* Boolean variables
* `.isdigit()`
* `.isupper()`
* `and`
* String handling

## 💻 Example

```text
Enter password: hello
Password is Weak
```

```text
Enter password: hello123
Password is Medium
```

```text
Enter password: Hello123
Password is Strong
```

## 📂 Project Structure

```text
password-strength-checker/
│
├── password_checker.py
└── README.md
```

## ▶️ How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Open the project folder in your terminal.
4. Run:

```bash
python password_checker.py
```

5. Enter your password when prompted.

## 🎯 Learning Goal

The main goal of this project is to strengthen my understanding of **Python conditional logic, loops, Boolean values, and string methods** while building small practical projects.

---

### 👨‍💻 Author

**Python Developer | Learning Django**

This project is part of my Python learning journey and practice projects.
