"""
PROGRAMMING ASSIGNMENT 06
Filename: 'exercise2.py'

Write a program (in the main() in exercise2.py) which:
    1. asks the user to input a filename (supposedly in the same folder as your program)
    2. reads the numbers (type int ) in the file (filename given by the user in previous step)
    and stores them into a list
    3. prints the minimum, the maximum and the average of the numbers (2 decimal places for the average)

Note: Your program should be impossible to crash.
      Think about all the possibilities to make your program crash.
      If one of the steps throws an exception,
        display a message to the user and your program should loop back to step 1.

Output: If the file cannot be found, display "File not found".
        For the rest of the exception, simply display "Error".

"""

# Place your imports here if any


def main():
    while True:
        filename = input("Filename: \n")
        try:
            f = open(filename, "r")
        except:
            print("File not found")  # No File Error
        else:
            content = f.readlines()
            if len(content) == 0:
                print("Error")  # Empty File Error
                continue
            try:
                for i in range(len(content)):
                    content[i] = int(content[i])
            except:
                print("Error")  # Invalid Data Error
                continue
            break

    print(f"Minimum: {min(content)}")
    print(f"Maximum: {max(content)}")
    print(f"Average: {sum(content)/len(content):.2f}")  # 2-decimal digit rounding


if __name__ == "__main__":
    main()
