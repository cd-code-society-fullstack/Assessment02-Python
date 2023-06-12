## Problem 01

**Problem Statement**

You are given a string and a keyword. Your task is to implement a function called `get_contents` that performs the following operation:

- The function finds the first two substrings that match the keyword in the string, and returns the string that is between them. If there is only one or no occurrence of the keyword, it should return an empty string.

The `get_contents` function should accept two parameters:

1. `str`: a string value.
2. `keyword`: a string value representing the keyword.

Here are some examples:

- `get_contents("breadjambread", "bread")` should return `"jam"`, because "jam" is between the first and second occurrence of "bread".

{Try It!}(python3 .guides/01/try-it-01.py)

- `get_contents("xxbreadjambreadyy", "bread")` should return `"jam"`, because "jam" is between the first and second occurrence of "bread".

{Try It!}(python3 .guides/01/try-it-02.py)

- `get_contents("xxbreadyy", "bread")` should return `"None"`, because there is only one occurrence of "bread".

{Try It!}(python3 .guides/01/try-it-03.py)

**Hint**

You can use the `indexOf()` method with the keyword to find the first occurrence, then use `indexOf()` again starting from the position of the first occurrence to find the second. After that, use the `substring()` method to extract the string between these two positions.

## Submit

python3 .guides/secure/testRunner01.py

"xxbreadjambreadyy" "bread" - jam
"xxbreadyy" "bread" - none
"xxlemonjambreadyylemonxx" "lemon" - jambreadyy

## Problem 02

**Problem Statement**

Given a string `text`, your task is to implement a function `count_word_frequency` that counts the frequency of each word in the string and returns an object. The object should have the words as keys and the count of each word as values. The words should be converted to lowercase. Punctuation should be removed and not considered part of a word.

The `count_word_frequency` function should accept one parameter:

1. `text`: a string.

Here are some examples:

- `count_word_frequency("Hello, hello!")` should return `{ hello: 2 }`, as 'hello' appears twice.

{Try It!}(python3 .guides/03/try-it-01.py)

- `count_word_frequency("This is a test. This is only a test.")` should return `{ this: 2, is: 2, a: 2, test: 2, only: 1 }`.

{Try It!}(python3 .guides/03/try-it-02.py)

- `count_word_frequency("The quick brown fox, jumped over the lazy dog.")` should return `{ the: 2, quick: 1, brown: 1, fox: 1, jumped: 1, over: 1, lazy: 1, dog: 1 }`.

{Try It!}(python3 .guides/03/try-it-03.py)

**Hint**

You can use the `split()` method to divide the string into an array of words. Then, you can loop through the array, using each word as a key in an object. Each time a word is encountered, increase its count in the object. Don't forget to remove punctuation and convert words to lowercase before counting them.

## Submit 

python3 .guides/secure/testRunner03.py

'Hello, hello!' { hello: 2 }
'This is a test. This is only a test.' { this: 2, is: 2, a: 2, test: 2, only: 1 }
'The quick brown fox, jumped over the lazy dog.' { the: 2, quick: 1, brown: 1, fox: 1, jumped: 1, over: 1, lazy: 1, dog: 1 }

## Problem 03

# Problem

Your task is to write a function that accepts a string `s` as input and returns the minimum number of characters that need to be deleted to make the given string a palindrome.

A palindrome is a word, number, phrase, or other sequences of characters that reads the same backward as forward. This includes ignoring spaces, punctuation, and capitalization.

### Example

**Example 1:**

```
Input: s = "abcba"
Output: 0
```

{Try It!}(python3 .guides/04/try-it-01.py)

In this example, the input string "abcba" is already a palindrome as it reads the same from both ends. So, no character deletion is necessary.

**Example 2:**

```
Input: s = "abca"
Output: 1
```

{Try It!}(python3 .guides/04/try-it-02.py)

In this example, by deleting the character 'c', the string "abca" becomes "aba", which is a palindrome.

**Example 3:**

```
Input: s = "abcd"
Output: 3
```

{Try It!}(python3 .guides/04/try-it-03.py)

In this example, to make the string "abcd" a palindrome, we need to delete three characters, 'b', 'c', and 'd', leaving only "a" which is a valid palindrome.

## Submit

python3 .guides/secure/testRunner04.py

abcba - 0 
abca - 1
abcd -3
racecar - 0

## Problem 04

## Problem

You are given two sentences, `s` and `t`. Your task is to determine if `t` is an anagram of `s`, however, this problem has a twist. 

An anagram is a word or phrase that is formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For this problem, a space is also considered as a character. All characters are treated as lowercase.

Write a function `are_strict_sentences_anagrams(s, t)` that takes the sentences `s` and `t` as its parameters. It should return `true` if `t` is an anagram of `s`, and `false` otherwise. The function should consider all characters including spaces, symbols, and punctuation marks as significant characters for the purpose of this problem.

The length of both `s` and `t` is at least 1 and at most 5 * 10^4. Both sentences will consist of English letters, spaces, symbols, punctuation marks, and numbers.

## Examples

1. 
   **Input**
    ```js
    are_strict_sentences_anagrams("listen now", "silent won")
    ```
    **Output**
    ```js
    true
    ```
    **Explanation**: By rearranging the letters of "listen now", you can form "silent won".

    {Try It!}(python3 .guides/05/try-it-01.py)


2. 
    **Input**
    ```js
    are_strict_sentences_anagrams("The Morse Code.", "Here come dots.")
    ```
    **Output**
    ```js
    true
    ```
    **Explanation**: By rearranging the letters of "The Morse Code.", you can form "Here come dots.".

    {Try It!}(python3 .guides/05/try-it-02.py)

3. 
    **Input**
    ```js
    are_strict_sentences_anagrams("Hello, world!", "Howdy, partner!")
    ```
    **Output**
    ```js
    false
    ```
    **Explanation**: No matter how you rearrange the letters of "Hello, world!", you can't form "Howdy, partner!".

    {Try It!}(python3 .guides/05/try-it-03.py)

## Submit

python3 .guides/secure/testRunner05.py

'listen now' 'silent won' true

'The Morse Code.' 'Here come dots.' true

'Hello, world!' 'Howdy, partner!' false

## Problem 06

## Problem

Given a string `s` that consists of numbers (0-9), addition operators ('+'), subtraction operators ('-'), multiplication operators ('*'), division operators ('/'), and parentheses ('(', ')'), determine if the input string is a valid mathematical expression.

An input string is a valid mathematical expression if:

1. Parentheses are correctly paired and nested. That is, every open parenthesis '(' has a corresponding closing parenthesis ')', and pairs of parentheses are properly nested in other pairs of parentheses.
2. There are no two operators next to each other. That is, an operator '+', '-', '*', or '/' must always be surrounded by numbers or parentheses. There should be no two operators without a number or a pair of parentheses between them.
3. Division operator '/' should not have zero immediately after it. Division by zero is undefined in mathematics.

### Example 1:

Input: s = "(1+2)*(3/4)"
Output: true

{Try It!}(python3 .guides/06/try-it-01.py)

### Example 2:

Input: s = "1+2*3/4"
Output: true

{Try It!}(python3 .guides/06/try-it-02.py)

### Example 3:

Input: s = "1++2*3"
Output: false

{Try It!}(python3 .guides/06/try-it-03.py)

Constraints:

1 <= s.length <= 10^4
s consists of numbers, '+', '-', '*', '/', '(', and ')' only.

## Submit

python3 .guides/secure/testRunner06.py

'foo(bar)' foorab
'foo(bar)blim' foorabblim
'foo(bar(baz))blim' foobazrabblim