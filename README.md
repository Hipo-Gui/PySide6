# PySide6 Basic GUI Example

This project is a **basic study of graphical user interfaces using PySide6 (Qt for Python)**.
It demonstrates how to create widgets, apply visual styles, organize them using layouts, and run a Qt application.

The focus is on understanding the **structure of a Qt application**, not on building a complete or production-ready interface.

---

## What is PySide6?

PySide6 is the official Python binding for the **Qt framework**.
It allows you to build modern, cross-platform graphical applications using Python while following the same concepts used in Qt (C++).

---

## Project goal

The purpose of this project is to practice and understand:

- How a Qt application starts
- The role of `QApplication`
- How widgets are created and displayed
- How to style widgets using Qt Style Sheets
- How layouts manage widget positioning
- How the widget hierarchy works

---

## How the code works

### 1. Application initialization

Every Qt application must start with a `QApplication` instance.
It manages the event loop and handles user interactions such as clicks and window events.

```python
app = QApplication(sys.argv)
