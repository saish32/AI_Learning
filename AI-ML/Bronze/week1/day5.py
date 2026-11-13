import re 


# def reverse_words(sentence):
#    words=sentence.split()
#    reversed_words=words[::-1]
#    return " ".join(reversed_words)

# sentence="Python is a high-level programming language"
# reversed_sentence=reverse_words(sentence)
# print(reversed_sentence)  # prints 'language programming high-level a is Python'



# def replace_email_addresses(text):
#     pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#     return re.sub(pattern, "[EMAIL]", text)

# input_text = "Please contact us at john.doe@example.com or jane.smith@test.org"
# clean_text = replace_email_addresses(input_text)
# print(clean_text)  # prints 'Please contact us at [EMAIL] or [EMAIL]

# def countnoofvowels(s):
#     count=0
#     for i in range(len(s)):
#         if s[i] in "aeiouAEIOU":
#             count+=1
#     return count

# input_text=input("Enter a string: ")
# print(countnoofvowels(input_text))

# def isplaindrome(s):
#     s="".join(char.lower() for char in s if char.isalnum())
#     return s==s[::-1]

# input_text=input("Enter a string: ")
# print(isplaindrome(input_text))


# def clean_text(text):
#     text=re.sub(r"[^\w\s]", "", text)
#     text=" ".join(text.split()) 
#     return text.lower()

# input_text="   hello.world,!!! welcome to   python, programming....   "
# cleaned_text=clean_text(input_text)
# print(cleaned_text)  # prints 'hello world welcome to python programming'




# text="contact me at 123-456-7890 or 987-654-3210"
# # digits=re.findall(r"\d",text)
# # print(digits) 
# updated_text=re.sub(r"\d", "X", text)
# print(updated_text)  # prints 'contact me at XXX-XXX-XXXX or XXX-XXX-XXXX'



# sentence="Python is a high-level"
# words=sentence.split()
# print(words)  # prints ['Python', 'is', 'a', 'high-level']

# new_sentence="    ".join(words)
# print(new_sentence)  # prints 'Python java & is java & a high-level'

# text="i love java"
# text1=text.replace("java","python")
# print(text1)  # prints 'i love python'

# text2="        python,. programming          "
# text3=text2.strip()
# print(text3)  # prints 'python,. programming'
# string1="hello"
# string2="world"
# result=string1+" "+string2
# print(result)

# text="python programming"
# print(text[0:6])  # prints 'python'
# print(text[-11:])  # prints 'programming'