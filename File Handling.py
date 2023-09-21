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

print("*****************************************************")
'''
s = input("Enter your name")

s1 = "My name is :" + s
f = open("sampleNewfile", "w")
f.write(s1)
f.close()
'''
print("*****************************************************")

# opening the file in r mode:

f = open('demo.txt','a')
print(f.write("welcome to the append mode\n"))
f.close()
f = open("demo.txt","r")
print(f.read())

print(f.name) # to return the file name
print(f.mode) # to return the file mode
print(f.closed) # to check whether the file is closed or not
f.close()
print(f.closed)

print("***********************")

'''
Opening the file using the with statement:
when we declare the file by using the with statement, the file is automatically closed once the execution is completed.
'''

with open("demo.txt") as fh:
    print(fh.read())
print(fh.closed)

print("*****************************************************")

'''
File operations module os:
There is a module os defined in python that provides the various functions which are used to perform various operations on files.
To use these functions, 'os' needs to be imported by using import keyword. 

Function             Function Description 
  name
-----------------------------------------------------------------------------------------------------------------  
rename() = It is used to rename a file. It takes 2 arguments, existing_file_name and new_file_name.
remove() = It is used to delete a file. It takes 1 argument.
mkdir()  = It is used to create a directory. A directory contains the file.
chdir()  = It is used to change the current working directory
getcwd() = It gives the current working directory.
rmdir()  = It is used to delete a directory.It takes 1 argument which is the name of the directory.

'''
import os
# os.rename("sample.txt","sam.txt")
# os.remove("sam.txt") # to remove the file

#os.mkdir("New")
#os.chdir("New") # to change the directory path
# print(os.getcwd()) # for this to work, comment the above 2 lines
#print(os.getcwd())
#os.chdir('../') # dots are the paths
                 # 1st dot -  to go outside the current folder ,
                 # 2nd dot - to go inside the parent folder in which the folder is present
#print("new path", os.getcwd())

print("*****************************************************")

'''
            r+ mode:
r+ is used for opening a file for both reading and writing operations.(file is mandatory)
While performing operations on the file, if it is not available, we will get an error as a message.
In this mode while performing write operations, the data will be replaced with existing data.
'''

f = open("demo.txt", "r+")
f.write("Hello")
f.seek(0)
print(f.read())

print("*****************************************************")

'''
             w+ mode:
w+ is used for opening a file for both reading and writing operations(file is optional).
When we open teh file, if the file is not available then it will create the file.
When we open the file, if the file is available then it will erase the data, then it creates empty file.             
'''

f = open("sample1.txt", "w+") # after write the cursor will be at the end of the line
f.write("Welcome to w+ mode")
f.seek(0)
print(f.read())

print("*****************************************************")

'''
"x" - create - creates the specified file, returns an error if the file exists.
x : exclusive creation : it is only present in python 3 not in 2
If the file is not available, then only it will create new file.
If the file is available, then we will get error: FileExistsError:[Errno 17] File exists:abc.txt'
'''

f = open("hello1.txt", "x") # change the name to hello 1,2,3 while running again
f.write("Hello,...getting error???????")
#print(f.read()) # in x mode, file can only be written in , we cannot read the file

