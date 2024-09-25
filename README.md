Robot Speaker Program with Timer

The Robot Speaker Program is a Python-based program that takes user input and returns the output by converting it into speech using the Windows text-to-speech functionality. The program also includes a timer feature, allowing the user to interact within a specified time limit.

Features:
Converts user input into speech using Windows text-to-speech.
Uses a timer to limit user interaction within a specific time period.

Requirements:
To run this program, you need to install some required libraries.
win32com.client: For text-to-speech functionality on Windows.
time: (Built-in module) For managing the timer functionality.

Installation:
To install the necessary library for win32com.client, use the following command:
pip install pywin32
The time module is built-in, so no need to install anything for it.

Usage:
After installing the required libraries, you can run the program. It will prompt you to enter some text, which will then be spoken aloud by the system. The program also tracks the time and ensures it functions within the time limit.

Example interaction:
Upon running the program, the robot will start and notify you that you have 20 seconds to interact.
You can type any message, and the robot will speak it out loud.
To exit the program manually, type "T" and the program will end.
If the timer runs out, the program will notify you and terminate automatically.
