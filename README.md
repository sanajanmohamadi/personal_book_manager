# Personal Book Manager

A simple book manager built with Python.

## Features
- Add multiple tasks
- Save tasks
- Load saved tasks
- Admin mode

## Requirements
- Python
- python-dotenv

## Installation

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Environment setup

Use `.env.example` as a template.

Add your admin password:

```env
admin_pass=your_password_here
```

Replace `your_password_here` with your own admin password.

## Run the program

Run the main file:

```bash
python main.py
```

## Screenshot

![Personal Task Manager Screenshot](images/screenshot.png)

## Demo

![Personal Task Manager Screenshot](images/screenshot.png)



![Static Badge](https://img.shields.io/badge/python-pink)




### File Description

| file | description |
| --- | --- |
| `main.py` | main file used to run book manager |
| `book.py` | stores book and answers |
| `Requirements.txt` | lists the python packages needed for the project |
| `.env.example` | shows the environment variables needed by the project |
| `.gitignore` | tells git which files and folders should not be tracked |
| `README.md` | contains the project documentation |
| `pictures/` | stores project screenshots |
| `gifs/` | stores demo GIF files |


### How It Works

First of all, after running the project, you will be asked whether or not you would like to gain access to "admin mode." You will then proceed to specify the number of books you wish to add, and for each one, you will enter the book's title.


## Troubleshooting

### 1. FileNotFoundError

- **Problem:** The program cannot find the file.

- **Possible Cause:** The file does not exist.

- **How to Check:** Check if the file exists in the project folder.

### 2. JSONDecodeError

- **Problem:** The program cannot read the books.json file.

- **Possible Cause:** The file is empty or contains incorrect data.

- **How to Check:** Open books.json and check its contents.

### 3. ModuleNotFoundError

- **Problem:** The program cannot find the required module.

- **Possible Cause:** The module is not installed.

- **How to Check:** Check if the required module is installed.

### 4. Admin Password Error

- **Problem:** The admin password is not working.

- **Possible Cause:** The password in the .env file is incorrect.

- **How to Check:** Check the password in the .env file.