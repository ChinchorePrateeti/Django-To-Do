# def reverse_check(word1, word2):
#     if len(word1) != len(word2):
#         print("false")
#         return False
#     i = 0
#     j = len(word2)-1 


#     while j >= 0:
#         if word1[i] != word2[j]:
#             print("false")
#             return False
#         print(i, j)
#         i = i+1
#         j = j-1
#     print("True")
        
#     return True

# reverse_check('abcj', 'dcba')

# valueobject concept
# a = 'abc'
# b = 'abc'
# print(a is b)

# p = [1, 2, 3]
# q = [1, 2, 3]
# print(p is q)

# q[1]= 33
# print(p,"hello", q)

# referencing

# list1 = [1, 2, 3]
# list2 = list1.append(44) #same list get's modified
# print(list1)
# print(list2)# because append function returns none

# list1 = [1, 2 ,3]
# list2 = [44, 45]
# list3 = list1+list2 # a new list is returned after concatenation
# print(list3)

# def func1(t):
#     t = t[1:]
#     print(t)
#     return t

# t4 = [1, 2, 3]
# print(func1(t4))
# print(t4)

# list4 = [3, 6, 1, 4]
# print(list4.sort())
# print(list4)

#sort() sorts the same list while sorted return a new sorted list
# list4 = [3, 6, 1, 4]
# list5 = sorted(list4)
# print(list5)
# print(list4)

#========================== Questions on string =======================

#Counting letter 'a' in a string 'banana' using a function [method1]


# def count_letter(mystring):
#     count = 0
#     for letter in mystring:
#         if letter == 'a':
#             count += 1
#     return count    


# counter = count_letter('banana') 
# print(counter)


#Counting letter 'a' in a string 'banana' using a built-in count method [method2]
# mystring = 'banana'

# counter = mystring.count('a')
# print(counter)

#checking if a string is a palindrome
# def if_palindrome(mystring):
#     my_new_string = mystring[::-1]
#     if my_new_string == mystring:
#         print("its a palindrome..")
#     else:
#         print("not a plaindrome")
    
# if_palindrome('popy')

#checking if a string is a palindrome by character


# def if_palindrome(str1, str2):
#     if len(str1) != len(str2):
#         print('Not a palindrome')
#         return False
#     i = 0 
#     j = len(str2)

#     while j>=0:
#         if str1[0] != str2[j-1]:
#             print("Not a palindrome")
#         i += 1
#         j -= 1
#         print("Its a palindrome")
#         return False
    
#     print("Its a palindrome")
#     return True

# if_palindrome('pop', 'pop')


# Write a function called rotate_word that takes a string and an integer as parameters, and returns a new string that contains the letters from the original string rotated by the given amount.

# def rotate_word(mystring, int_to_rotate):
#     new_string = ''
#     #print(chr(int_to_rotate))
#     for character in mystring:
#         #print(ord(character))
#         new_ascii_characrter = ord(character) + int_to_rotate
#         #print(new_ascii_characrter)
#         new_character = chr(new_ascii_characrter)
#         new_string += new_character
#     print(new_string)

        
# rotate_word('hal', 1)
# rotate_word('HAL', 1)
# rotate_word('Hal', 1)



#========================== Questions on lists =======================

# Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all of the nested lists.
# def nested_sum(mylist):
#     sum_of_listnumbers = 0
#     #length = len(mylist)
#     #while length > 3:
#     for a_list in mylist:
#         for value in a_list:
#             sum_of_listnumbers += value
#     print("total sum is : ", sum_of_listnumbers)    

# nested_list = [[2], [1,2], [3, 4, 5], [5]]
# nested_sum(nested_list)


# Write a function called cumsum that takes a list of numbers and returns the cumu-lative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the original list
# def cumsum(mylist):
#     cumulative_sum = 0
#     new_cumulated_list = []
#     for value in mylist:
#         cumulative_sum += value
#         new_cumulated_list.append(cumulative_sum)
#     print(new_cumulated_list)

# mylist = [1, 3, 5]
# cumsum(mylist)


# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements
# def middle(mylist):
#     new_list = []
#     index = 1
#     total_length = len(mylist) - 1
#     for num in range(index, total_length):
#         new_list.append(mylist[num])
#     print(new_list)    

# mylist = [2,11, 54, 5, 8, 1, 9, 4]
# middle(mylist)


# Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None.
# def chop(mylist):
#     mylist.pop()
#     mylist.remove(mylist[0])
#     print(mylist)


# mylist = [3, 6, 1, 4, 8, 9, 2]
# chop(mylist)    



# Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams.
# [method1]
# a=input("Enter string 1:")
# b=input("Enter string 2:")
# count=0
# for i in a:
#     for j in b:
#         if i==j:
#             count=count+1
            
# if count==len(a):
#     print("Strings are anagram of each other.")
# else:
#     print("Strings are not anagram of each other.")


# [method2]
# def is_anagram(str1, str2): 
#     if len(str1) != len(str2):
#         print("not an anagram..")
#     elif sorted(str1) == sorted(str2):
#         print("its an anagram")
# is_anagram('anad', 'dan')




# Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
# def has_duplicates(mylist):
#     counter = 0
#     new_list = sorted(mylist)
#     print(new_list)
#     for index in range(len(new_list)-1):
#         if new_list[index] == new_list[index+1]:
#             return True
#         else:
#             return False
# mylist = [2, 4, 3, 1, 5]
# result = has_duplicates(mylist)
# print(result)


#========================== Questions on dictionary =======================
# def reverse_lookup(d, v):
#     for c in d:
#         if d[c] == v:
#             print(c)
#             return c
#     raise LookupError()

# reverse_lookup({1:'a', 2: 'g', 3:'i'}, 'l')


# function to invert a dictionary   2:['a', 'f', 'k'], 
    # 6: ['q', 't'],
    # 3:['u', 'g', 'v'], 
    # 1:['z', 'm', 'x', 't']
        

# def invert_dict_func(mydict):
#     inverse_dict = {}
#     for key in mydict:
#         value = mydict[key]
#         if value not in inverse_dict:
#             inverse_dict[value] = [key]
#         else:
#             inverse_dict[value].append(key)
#     print(inverse_dict)

# mydict = {  'z':1, 'a':2, 'm':1, 'x':1, 'f':2, 'u':3, 'q':6,  'v':3,  't':6}
# invert_dict_func(mydict)

def demofunction(x, y):
    if x == 2:
        return False
    else:
        return True
    return True

print(demofunction(3, 1))