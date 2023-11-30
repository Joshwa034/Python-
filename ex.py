# # Step 1: Read and understand the problem statement and sample test cases
# 
# # Click on Next once you are ready to proceed.
# 
# 
# # number = int(input())
# # 
# # for i in range(number+1):
# #     n,m = input().split()
# #     n = int(n)
# #     m = int(m)
# #     
# #     z= n*2
# #     c= z-m
# #     print(c)
# #     
# 
# def decode(a,b):
#     revb = b[::-1]
#     a=list(a)
#     b=list(b)
#     if (len(a)!=len(b)):
#         return "Invalid input"
#     else:
#         for i in range(0, len(a)):
#             if(a[i].isUpper() or b[i].isUpper):
#                 return "Invalid input"
#             else:
#                 for i in range(0,len(a)):
#                     if (len(b[i]) %2==0):
#                         word = a[i]
#                         for i in word:
#                             new += word[i]
#                     else:
#                         word = a[i]
#                         for i in word:
#                             new +=word[i]
#     print(new)
# decode("qiiz gz hghd", "one orange ball")



# 
# 
# 
# def process_strings(a, b):
#     # Step 1: Reverse string B
#     reversed_b = b[::-1]
# 
#     # Step 2: Check if both strings have the same number of words
#     if len(a.split()) != len(reversed_b.split()):
#         return "Invalid: Different number of words"
# 
#     # Step 3: Check if either string contains capital letters
#     if any(char.isupper() for char in a + reversed_b):
#         return "Invalid: Contains capital letters"
# 
#     # Step 4: Split string A into words
#     words_a = a.split()
# 
#     # Step 5: Iterate over each word in reversed string B
#     for i, word in enumerate(reversed_b.split()):
#         # Step 6: Update string A based on word length and parity
#         if len(word) % 2 == 0:
#             words_a[i] = ''.join(chr((ord(char) - len(word) - ord('a')) % 26 + ord('a')) if char.islower() else char for char in words_a[i])
#         else:
#             words_a[i] = ''.join(chr((ord(char) + len(word) - ord('a')) % 26 + ord('a')) if char.islower() else char for char in words_a[i])
# 
#     return ' '.join(words_a)
# 
# 
# # Example usage:
# string_a = "jrrg zmw"
# string_b = "one girl"
# result = process_strings(string_a, string_b)
# print(result)
# 
# # 
# # good boy
# # 
# # one girl
# # 
# #  jrrg zmw


def check_strings(input_str1, input_str2):
    # Split input strings into words
    words_str1 = input_str1.split()
    words_str2 = input_str2.split()
    print(words_str2)

    # Check if either string has capital letters
    if any(char.isupper() for char in input_str1) or any(char.isupper() for char in input_str2):
        # Check if the number of words is equal
        print("Invalid input")
        return
        
    elif( len(words_str1) != len(words_str2)):
        print("Invalid input")
        return
    else:
        # Function to handle wrapping around from 'z' to 'a'
        def wrap_around(char, increment):
            if 'a' <= char <= 'z':
                return chr((ord(char) - ord('a') + increment) % 26 + ord('a'))
            
            else:
                return char
        words_str2 = words_str2[::-1]
        print(words_str2)

        # Iterate through each word
        for i in range(len(words_str1)):
            word1 = words_str1[i]
            word2 = words_str2[i]

            # Check if the length of the corresponding word in input_str2 is even
            if len(word2) % 2 == 0:
                # Decrease the letters of the corresponding word in input_str1
                new_word1 = ''.join(wrap_around(char, -len(word2)) for char in word1)
                words_str1[i] = new_word1
            # Check if the length of the corresponding word in input_str2 is odd
            elif len(word2) % 2 != 0:
                # Increment the letters of the corresponding word in input_str1
                new_word1 = ''.join(wrap_around(char, +len(word2)) for char in word1)
                words_str1[i] = new_word1

        # Print the modified words in input_str1
        modified_str1 = ' '.join(words_str1)
        print("Modified input 1:", modified_str1)


    

# Example usage:
string1 = "qiix gz clro"
string2 = "one orange ball"
check_strings(string1, string2)

























