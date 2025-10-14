

def counter(word: str, letter: str):
    """
        takes a word and counts the amount of ocurrences for a certain letter
        Args:
            word (str): the word to iterate over
            letter (str): the letter to count
        Returns:
            int: the total number of ocurrances for that letter in a word
    """
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count
            
    
print(counter("banana", "a"))