file='../Resource/test.txt'
# open the file in "read" mode ('r') and store te variable in variable "text"
with open(file,'r') as text:
    print(text) #this stores reference to a file stream
    lines=text.read() #stores the text inside a variable called "lines"
    print(lines)