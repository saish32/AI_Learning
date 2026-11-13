


# def count_no_of_words(filename,specific_word):
#     try:
#         with open(filename,"r")as file:
#             content=file.read()
#             words=content.split()
#             count=0
#             for word in words:
#                 if word == specific_word:
#                     count += 1
#             print(f"The word '{specific_word}' appears {count} times in the file.")
#     except FileNotFoundError:
#         print(f"File {filename} not found.")


# def copy_file(source_file,destination_file):
#     try:
#         with open(source_file,"r")as source:
#             content=source.read()
#         with open(destination_file,"w")as destination:
#             destination.write(content)
#     except FileNotFoundError:
#         print(f"File {source_file} not found.")


# def write_to_file(filename,content):
#     with open(filename,"w")as file:
#         file.write(content)

# def read_from_file(filename):
#     with open(filename,"r")as file:
#         content=file.read()
#         return content


# def count_lines_words(filename):
#     try:
#         with open(filename, "r") as file:
#             lines=file.readlines()
#             numlines=len(lines)
#             numwords=sum(len(line.split()) for line in lines)
#             print(f"Number of lines: {numlines}")
#             print(f"Number of words: {numwords}")
#     except FileNotFoundError:
#         print(f"File {filename} not found.")

# count_lines_words("sample.txt")
         

# try:
#     with open("sample.txt","r") as file:
#         content = file.readlines()
#         print(content)
# except FileNotFoundError:
#     print("File not found.")

# with open("sample.txt","r") as file:
#     content = file.readlines()
#     print(content)
# with open("sample.txt","a") as file:
#     file.write("New line added to the file.\n")
#     content = file.readlines()
#     print(content)

