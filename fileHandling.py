#Normal file reading
f = open("message.txt", "r")

content = f.read(2)
print(content)

content = f.read()
print(content)

f.close()


# 
try:
    f = open('message.txt', 'r')
    content = f.read()
    print(content)

finally:
    # close the file
    f.close()

# There is a better way to write the above code using the with...open syntax. Here's how:
with open('message.txt', 'r') as f:
    content = f.read()
    print(content)

# The file is automatically closed if we use this syntax to work with files.
# Remember: Make a habit of using with..open syntax when working with files so that you don't have to worry about closing the file.



# open file for writing
with open('python.txt', 'w') as f:
    # perform file operation
    

# Suppose we have a folder structure like this:

# main.py
# external
#   - messages.txt

# Here, the main.py file and the external folder are in the same folder, and the message.txt file is inside the external folder.

# Now, if we have to access messages.txt file from main.py, we have to specify the path like this:

# with open('external/messages.txt', 'r'):
#     f.read()