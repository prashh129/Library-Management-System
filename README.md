# 📚 Library Management System

A simple **Library Management System** built with Python that allows users to **view available books, add new books, and save data persistently** using a JSON file.

## 🚀 Features

- View all available books.
- Add new books to the collection.
- Persistent storage using `books.json`.
- User-friendly CLI interface.

## 🛠️ Installation & Usage

### 1️⃣ Clone the repository

```sh
git clone https://github.com/prashh129/Library-Management-System.git
cd library-management
```

### 2️⃣ Run the script

```sh
python library.py
```

## 📌 How It Works

- The program reads books from `books.json` (or creates one if it doesn't exist).
- Users can **view** or **add** books.
- The book list is updated and saved automatically.

## 📜 Code Overview

The main components:

- `Library` class: Handles loading, saving, viewing, and adding books.
- `main()` function: Runs the interactive menu.
- `if __name__ == "__main__":` ensures the script runs only when executed directly.

## 🖥️ Example Output

```
Welcome to Library Management System!
Please choose your option:
1. View books
2. Add book
3. Exit
Enter your choice (1-3): 2
Enter book name: The Python Guide
Your book 'The Python Guide' is added!
```

## 🛠️ Future Enhancements

- Option to remove books.
- Borrow/return book functionality.
- GUI version using Tkinter or PyQt.

## 📜 License

This project is **open-source** and free to use under the MIT License.


#Python #Coding #Project #LibraryManagement #OpenSource

