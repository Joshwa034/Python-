def wrap_around(char, increment):
            if 'a' <= char <= 'z':
                print(chr((ord(char) - ord('a') + increment) % 26 + ord('a')))
            
            else:
                print(char) 
            
wrap_around("y", 4)

