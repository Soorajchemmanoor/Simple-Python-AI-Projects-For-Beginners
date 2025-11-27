# Grammar Checker Using AI

This project is a simple AI-powered grammar correction tool built using Python and OpenAI.

It takes input from the user, sends it to an AI model, and returns a grammatically corrected version of the sentence.

---

## Features

- Uses OpenAI GPT model for grammar correction  
- Secure API key handling using `.env` file  
- Simple command-line based interaction  
- Clean and beginner-friendly Python code  

---

## Folder Structure

Grammar-Checker/
├── main.py
├── README.md
├── requirements.txt
└── .env  


---

## Requirements

- Python 3.8 or above
- An OpenAI API key
- Internet connection

---

## Setup Instructions

1. Move into the project folder:

cd grammar-checker

2. Install required libraries:

pip install -r requirements.txt

3. Setup your OpenAI API key:

 - Rename .env.example to .env
 - Open it and add your API key:

 OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE

---

## How to Run

 - Start the program:
   python main.py

 - Example:

   Enter a sentence: i has a apple
   Corrected version: I have an apple
   
 - To exit, type:
   q

---

## 🎓 Learning Purpose

 This project helps you understand:

  - How to connect Python with the OpenAI API
  - How AI can be used for Natural Language Processing
  - How to build simple AI tools using prompt engineering
  - How to handle environment variables securely

## 🚀 Possible Improvements

  - Add file-based grammar correction
  - Create a web interface using Flask or FastAPI
  - Add tone options (formal, casual)
  - Add GUI using Tkinter or PyQt

## Author

Sooraj P
GitHub: https://github.com/Soorajchemmanoor  
LinkedIn: https://www.linkedin.com/in/sooraj-p/  


---
