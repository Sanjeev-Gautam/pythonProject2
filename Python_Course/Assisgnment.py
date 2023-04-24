# Assignment 3:

list1 = ["Apple","Banana","Chhomu","loving_this"]
str1 = "Hello there"

def separation(srt1):
    return list(str1)

def multi_merge(list1,str1):
    result1 = separation(str1)
    list1 = list1 + result1
    print(list1)

multi_merge(list1, str1)