# Different methods to reverse a string in Python

def reverse_with_slicing(text):
    """Most Pythonic way using slicing"""
    return text[::-1]

def reverse_with_reversed(text):
    """Using reversed() function and join()"""
    return ''.join(reversed(text))

def reverse_with_loop(text):
    """Using a loop"""
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def reverse_with_list(text):
    """Using list and reverse() method"""
    char_list = list(text)
    char_list.reverse()
    return ''.join(char_list)

# Example usage
if __name__ == "__main__":
    text = "hello"
    
    print(f"Original: {text}")
    print(f"Method 1 (slicing): {reverse_with_slicing(text)}")
    print(f"Method 2 (reversed): {reverse_with_reversed(text)}")
    print(f"Method 3 (loop): {reverse_with_loop(text)}")
    print(f"Method 4 (list): {reverse_with_list(text)}")
