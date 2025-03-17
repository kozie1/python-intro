# app.py

def reverse_string(text):
    return text[::-1]

def get_max_value(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def count_words(sentence):
    return len(sentence.split())

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

