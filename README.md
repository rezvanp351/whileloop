# 🐍 Python While Loops, Break, Continue, If/Elif/Else
### Author: **Rezvan Panah**
> A clear and practical guide to Python control structures — ideal for beginners and GitHub learners 💡

---

## 📖 About This Project
This project explains the logic and use of **while loops** and control statements in Python:  
`break`, `continue`, `if`, `elif`, and `else`.

Each section includes clear explanations, inline comments, and example outputs to make learning intuitive and easy.  
Perfect for students, coding beginners, or anyone who wants to build strong fundamentals.

---

## 🧩 Sections Overview

### 🎯 **Part 1: What is a While Loop?**
A `while` loop runs as long as its condition remains **True**.  
Be careful — if the condition never becomes `False`, it creates an **infinite loop**.

```python
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
```

📤 **Output:**
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

---

### 🎯 **Part 2: Using 'break'**
The `break` statement immediately stops the loop, even if the condition is still `True`.

```python
x = 1
while x <= 10:
    print("Number:", x)
    if x == 5:
        print("Breaking the loop at 5")
        break
    x += 1
```

📤 **Output:**
```
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
Breaking the loop at 5
```

💡 **Tip:**  
`break` is commonly used to exit a loop early when a condition is met (e.g., finding a target in data).

---

### 🎯 **Part 3: Using 'continue'**
The `continue` statement skips the rest of the code for the current loop iteration and moves on to the next one.

```python
y = 0
while y < 7:
    y += 1
    if y == 3:
        print("Skipping number 3")
        continue
    print("y =", y)
```

📤 **Output:**
```
y = 1
y = 2
Skipping number 3
y = 4
y = 5
y = 6
y = 7
```

💡 **Tip:**  
`continue` is useful when you want to **skip certain values** or conditions but continue looping.

---

### 🎯 **Part 4: Combining While with If / Elif / Else**
You can use conditional statements inside a loop to make your program behave differently depending on each iteration.

```python
num = 1
while num <= 7:
    if num == 1:
        print("One - Start of Loop")
    elif num == 4:
        print("Four - Middle of Loop")
    elif num == 7:
        print("Seven - End of Loop")
    else:
        print("Number:", num)
    num += 1
```

📤 **Output:**
```
One - Start of Loop
Number: 2
Number: 3
Four - Middle of Loop
Number: 5
Number: 6
Seven - End of Loop
```

💬 This is a common technique for tracking stages or progress during a loop.

---

### 🎯 **Part 5: Practical Example — User Input**
This example shows how a `while` loop can handle **user input** repeatedly until a negative number is entered.

```python
while True:
    user_input = int(input("Enter a positive number (negative to exit): "))
    if user_input < 0:
        print("You entered a negative number. Exiting...")
        break
    elif user_input == 0:
        print("Zero entered, try again.")
        continue
    else:
        print("You entered:", user_input)

print("Program ended successfully!")
```

📤 **Sample Output:**
```
Enter a positive number (negative to exit): 5
You entered: 5
Enter a positive number (negative to exit): 0
Zero entered, try again.
Enter a positive number (negative to exit): -2
You entered a negative number. Exiting...
Program ended successfully!
```

---

## 🧠 Key Concepts Summary

| Concept | Description |
|----------|--------------|
| **while loop** | Repeats a block of code while a condition is True |
| **break** | Exits the loop immediately |
| **continue** | Skips the rest of the loop and goes to the next iteration |
| **if / elif / else** | Decision-making structures to control flow inside loops |

---

## ⚙️ How to Run This Code
1. Open the file in your Python IDE (e.g., VS Code, IDLE, or PyCharm).  
2. Run the script.  
3. Observe the printed results in the console.  

---

## 💬 Practice Ideas
🔹 Create a loop that sums numbers from 1 to 10.  
🔹 Use `break` to stop once the total exceeds 30.  
🔹 Use `continue` to skip number 5.  

---

## 🌟 Support This Project
If this tutorial helped you ❤️  
please consider supporting it by:

- 🌟 **Starring** this repository on GitHub  
- 👥 **Following** for more Python tutorials  
- 🔗 **Sharing** it with your friends and learners  

> Every ⭐ star motivates me to make more free educational content!

---

## 📬 Contact
**GitHub:** [Mohd R. Panah](https://github.com/rezvanp351)  
**Email:** rezvanpanah4@example.com  

---

## 🧾 License
This project is open-source and free to use, modify, and share for educational purposes.

---
