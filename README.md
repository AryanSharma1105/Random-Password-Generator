# Random-Password-Generator
🔐 Random Password Generator

A simple Python project that generates random passwords using letters, numbers, and special characters.

This project demonstrates the use of Python's "random" and "string" modules, along with "random.sample()" and "random.choices()".

✨ Features

- Generates 16-character passwords
- Includes:
  - Uppercase and lowercase letters
  - Numbers
  - Special characters
- Generates a password with unique characters
- Generates another password where characters can repeat
- Simple and beginner-friendly Python code

🛠️ Technologies Used

- Python 3
- "random" module
- "string" module

📌 How It Works

THIS SIMPLE PROJECT WAS MADE USING PYTHON LIBRARY FUNCTIONS LIKE string & random.
string.ascii_letters

The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.
string.ascii_lowercase

The lowercase letters abcdefghijklmnopqrstuvwxyz. This value is not locale-dependent and will not change.
string.ascii_uppercase

The uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ. This value is not locale-dependent and will not change.
string.digits

The string 0123456789.

string.punctuation

String of ASCII characters which are considered punctuation characters in the C locale: !"#$%&'()*+,-./:;<=>?@[\]^_{|}~

characters = string.ascii_letters + string.digits + string.punctuation

It then generates two different passwords:

1. Unique Character Password

password = "".join(random.sample(characters, length))

"random.sample()" selects characters without replacement, so the same character is not selected more than once.

2. Password With Repeating Characters

password1 = "".join(random.choices(characters, k=length))

"random.choices()" selects characters with replacement, so characters can appear multiple times.

▶️ How to Run

1. Install Python

Make sure Python 3 is installed on your computer.

2. Clone the Repository

git clone https://github.com/AryanSharma1105/random-password-generator.git

3. Run the Program

python password_generator.py

💻 Example Output

Your Unique Password is: aB7@kP2!xQ9#Lm$R
Your Password is: 7@aaP!2xQ9#Lm$Rk

The passwords shown above are only examples. Your program will generate different passwords each time.

📚 What I Learned

Through this project, I practiced:

- Importing Python modules
- Using the "random" module
- Using the "string" module
- "random.sample()"
- "random.choices()"
- String concatenation
- The "join()" method
- Generating random data with Python

⚠️ Note

This project is intended as a beginner Python learning project. For passwords that need strong security, use a cryptographically secure generator such as Python's "secrets" module rather than "random".
-For Secure Password Check Out My Secure Password Generator Github Repository.

👨‍💻 Author

Aryan Sharma

A beginner Python project created for learning and practicing Python fundamentals.
