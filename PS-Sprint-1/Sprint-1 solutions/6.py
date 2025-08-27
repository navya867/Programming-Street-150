def is_palindrome(p):
    p=p.lower()
    result=[]
    if not p:
        return False
    # return p == p[::-1]       another logic
    for i in p:
        result.insert(0,i)
    return "".join(result)
    # for char in p:
    #     result.append(char)  # O(1) per call
    # result.reverse()         # O(n) once
    # return ''.join(result)
    #string concatenation creates new string every time
p=input(" ")
final=is_palindrome(p)
if final == p:
    print("palidrome")
else:
    print("not palindrome")

# Basic String Reversal - O(n) time, O(n) space
# Two Pointer - O(n) time, O(1) space ⭐ Most efficient
# Recursive - O(n) time, O(n) space (stack)
# Alphanumeric Only - O(n) time, O(1) space
# With Preprocessing - O(n) time, O(n) space

# Edge Cases Covered:

# Basic strings: "radar", "level", "hello"
# Numbers: 121, 12321, 123
# Single characters: "a", 1
# Empty strings: ""
# Case sensitivity: "Radar", "RaceCar"
# Spaces & punctuation: "A man, a plan, a canal: Panama"
# Invalid inputs: None, [], {}
# Unicode characters: "午后后午", "αβα"
# Very long strings: Performance testing
# Special cases: "00100", float numbers

# Complexity Comparison:
# MethodTimeSpaceBest Use CaseTwo PointerO(n)O(1)Large strings, memory-constrainedBasic ReversalO(n)O(n)Simple, readable codeRecursiveO(n)O(n)Educational, functional styleAlphanumericO(n)O(1)Real-world text with punctuationPreprocessingO(n)O(n)When you need the cleaned string
# Recommendations:

# For production code: Use the Two Pointer approach (optimal time & space)
# For text with punctuation: Use Alphanumeric Only approach
# For learning: Try the Recursive approach
# For simplicity: Use Basic Reversal approach