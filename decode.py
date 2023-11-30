
def check_strings(input_str1, input_str2):
    words_str1 = input_str1.split()
    words_str2 = input_str2.split()
    print(words_str2)

    if any(char.isupper() for char in input_str1) or any(char.isupper() for char in input_str2):
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
