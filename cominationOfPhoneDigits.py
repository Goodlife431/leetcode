def letterCombinations(digits):
    if not digits:
        return []

    # Mapping of digits to letters
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    def backtrack(index, path):
        if index == len(digits):
            combinations.append(path)
            return
        
        digit = digits[index]
        letters = digit_to_letters[digit]
        
        for letter in letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations

# Example usage
digits = "23"
result = letterCombinations(digits)
print(result)
