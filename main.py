import subprocess
import shlex


print("Welcome, this is some manage ment thing lol...\n\n")

print("exit - Exit the session.")
print("cpp - C++ Compiler")
print("c - C Compiler")
print("py - Python Compiler")
print("js - JavaScript compiler")
print("read - Read a file")
print("\nInput what you wanna do: ")

x = input(" ")

if x == "exit":
    exit(0)

if x == "cpp":
    filen = input("Please type the name of the c++/cpp file that you want to compile ")
    subprocess.run(shlex.split(f"g++ {filen} -o output"))
    subprocess.run("./output")

if x == "c":
    filen = input("Please type the name of the c file that you want to compile ")
    subprocess.run(shlex.split(f"gcc {filen} -o output"))
    subprocess.run("./output")

if x == "py":
    filen = input("Please type the name of the python file that you want to run ")
    subprocess.run(shlex.split(f"python3 {filen}"))

if x == "js":
    filen = input("Please type the name of the javascript file that you want to run ")
    subprocess.run(shlex.split(f"node {filen}"))

if x == "read":
    filen = input("Please type the name of the file that you want to read ")
    with open(filen, "r") as f:
        print(f.read())

else:
    print("Error: Command not found!")