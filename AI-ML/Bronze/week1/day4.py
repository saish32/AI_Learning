


# students = {"Alice": "A", "Bob": "B", "Charlie": "C"}

# grade_points = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
# average_grade = sum(grade_points[grade] for grade in students.values()) / len(students)
# print(average_grade)



# list1=[1,2,3,4,4,5,5,3,4,2,1]
# # list1.reverse()
# # print(list1)
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i],end=" ")
# empty_set=set()
# for i in list1:
#     empty_set.add(i)
# print(empty_set)

# sentence=input("Enter a sentence:")

# words=sentence.split()
# print(words)

# words_count={}

# for word in words:
#     word=word.lower()
#     if word in words_count:
#         words_count[word]+=1
#     else:
#         words_count[word]=1

# print(words_count)


# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1.union(set2))
# print(set1|set2)#union
# print(set1.intersection(set2))
# print(set1&set2)#intersection
# print(set1.difference(set2))
# print(set1-set2)#difference
# print(set2-set1)#difference


# numbers={1,2,3,4,5}
# print(numbers)
# numbers.add(6)
# numbers.add(4)
# print(numbers)
# numbers.remove(2)
# print(numbers)


# dict={"name": "Alice", "age": 30, "city": "New York"}
# print(dict["name"])
# print(dict["age"])
# dict["age"]=31#update
# dict["country"]="USA"#add
# print(dict)
# dict.pop("city")#remove
# print(dict)
# del dict["country"]#remove
# print(dict)
# for key,value in dict.items():
#     print(key,value)



# colour=("red","green","blue")
# single_tuple=("apple",)
# print(colour[0])
# print(single_tuple[0])

# fruits=["apple","orange","banana","kiwi"]
# print(fruits)
# print(f"{fruits[0]}")
# print(f"{fruits[-1]}")
# fruits[0]="mango"
# print(fruits)
# fruits.append("grapes")
# print(fruits)
# fruits.insert(1,"papaya")
# print(fruits)
# # fruits.remove("banana")
# # print(fruits)
# # del fruits[2]
# # print(fruits)
# # fruits.pop()
# # print(fruits)
# sliced_fruits=fruits[1:3]
# print(sliced_fruits)
