'''
                  File Handling
Python can be used to read and write data.
Also it supports reading and writing data to files.

File is a named location on disc to store related information.
It is used to permanently store data in a non-volatile memory(eg. hard disk).

Generally, we divide files in :
1) Text file
2) Binary file

Text file: Text files contains simple text (character data).
Ex. html, .c, .cpp, .java,....etc
Binary file: Binary files contain binary data which is only readable by computer.

To perform file handling, we ned to perform these steps:
1) Open file
2) Read / Write file
3) Close file

Step 1:   Opening a file: ---------------------------------------

To open a file, Python has a built-in function open().
It returns an object of file which is used with other functions.
The open function takes 2 arguments, the name of the file and mode of operation.
SYNTAX: f = open(filename, mode)

The default file operations is read mode
f = open("test.txt")   # open file in current directory
f = open("C:Python22/demo.txt")  # specifying full path

Step 2:    Write or read or append data: ---------------------------------------
NOTE: The default mode of the file is : Read

Writing to a file: write() method is used to write a string into a file.
Reading forma file: read() method is used to read data from the file.

The read functions contain different methods:
1) read()     - return one big string
2) readline   - return one line at a time
3) readlines  - returns a list of lines

Append operations: used to append the data to existing file.

Step 3:   Close the file:

Closing a file: close()

'''

'''

Modes for opening a file:
r = Open a file for reading
w = Opens a file for writing only. Overwrites the file if the file exists. 
    If the file does not exist, it creates a new file for writing.
r+= Opens for reading and writing(cannot truncate a file)
w+= For writing and reading(can truncate a file)
a = Opens for appending a file at the end of the file without truncating it.
    Creates a new file if it does not exits.
t = Open in text mode.
b = Open in binary mode.
x = Open for exclusive creation, failing if the file is already present.
'''

f = open("sample.txt", "w") # if the file is not available then create the file and the write the data.
f.write("Hi this is Aryan")
f.close()

f = open("sample.txt") # no mode is given so it opens the file in read mode by default.
print(f.read())

print(f.tell()) # this tell the current position of the cursor.
print(f.seek(5)) # moving the cursor to a specific location
print(f.read())
f.close()

f = open("sample.txt", "w")
f.write("List is a python object.\nList is mutable.\nModifications are allowed in list.")
f.close()

f = open("sample.txt")
print(f.readline()) # printing the text on the current line
f.seek(45)
print(f.readline())

f.seek(0) # moving the cursor to the beginning of the file
print(f.readlines()) # print the file contents in list format

print("*****************************************************")

f = open("sampleMyfile", "w")
f.write("My name is Aryan Shisode\nI live in Pune")
f.close()
