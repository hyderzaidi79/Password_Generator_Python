# 🔐 Secure Password Generator (Python)

A simple yet effective command-line tool to generate secure and randomized passwords using a custom core word, with configurable length and quantity. Ideal for creating passwords that are strong and memorable.

---

## ✨ Features

- 🧩 Add your own **core word** for memorable personalization
- 🔁 Generate **multiple passwords** at once
- 🔒 Combines letters, digits, and symbols for strong security
- 🧪 Shuffles the final password to enhance randomness
- ⚠️ Warns if the core word is too long

---

## 🛠 Requirements

- Python 3.x  
(No external libraries required; uses built-in `random` and `string` modules)

---

## 🚀 How to Run

1. Clone or download the script.
2. Run the file using Python:

```bash
python secure_password_generator.py

    Follow the prompts:

📝 Enter a core word or base for your password: sunrise
🔢 Enter the total length of each password: 14
🔁 How many passwords would you like to generate? 5

🔓 Example Output

🔓 Your Generated Passwords:
-----------------------------
1. rni7@uSu>ne#s
2. ius^nrn>9$e7s
3. s%r7n@ei&us!n
...

Each password includes the core word (in shuffled form) and random characters.
⚠️ Input Validation

    If the core word is longer than the total length, an error is shown.

    If the length or count inputs are not valid numbers, the script exits with a helpful message.

💡 Use Cases

    Personal or business account passwords

    Password generation for apps or testing

    Teaching randomness and security basics

📄 License

This project is open-source and licensed under the MIT License.
