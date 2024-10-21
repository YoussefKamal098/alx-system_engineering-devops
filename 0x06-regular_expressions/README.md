# Comprehensive Guide to Regular Expressions

Regular expressions (regex) are powerful tools for searching and manipulating strings. They provide a flexible and efficient way to specify patterns for matching text, which can be used in programming languages, text editors, and command-line utilities. This guide covers both fundamental concepts and advanced topics in regex.

## Content Table

| **Topic**                         | **Description**                                                                                                          | **Link**                                           |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| **1. Fundamentals of Regex**      | Introduction to the basic concepts, syntax, and usage of regular expressions.                                            | [Fundamentals of Regex](#fundamentals-of-regex)   |
| **2. Lookahead**                  | Asserts that a pattern is followed (positive) or not followed (negative) by another pattern.                              | [Lookahead](#lookahead)                            |
| **3. Lookbehind**                 | Asserts that a pattern is preceded (positive) or not preceded (negative) by another pattern.                              | [Lookbehind](#lookbehind)                          |
| **4. Backreferences**             | Refers to a previously captured group within the same regex.                                                              | [Backreferences](#backreferences)                  |
| **5. Named Capturing Groups**     | Assigns names to capturing groups and refers to them by name in the regex.                                                | [Named Capturing Groups](#named-capturing-groups)  |
| **6. Non-Capturing Groups**       | Groups parts of the regex without storing them for backreferences.                                                        | [Non-Capturing Groups](#non-capturing-groups)      |
| **7. Lazy Quantifiers**           | Matches as few characters as possible (non-greedy).                                                                       | [Lazy Quantifiers](#lazy-quantifiers)              |
| **8. Anchors**                    | Matches positions within a string (start or end).                                                                         | [Anchors](#anchors)                                 |
| **9. Word Boundaries**            | Matches a word boundary or non-boundary.                                                                                  | [Word Boundaries](#word-boundaries)                 |
| **10. Conditional Matching**      | Applies different patterns based on a condition.                                                                          | [Conditional Matching](#conditional-matching)       |
| **11. Atomic Groups**             | Matches a portion of the regex and prevents backtracking within that group.                                               | [Atomic Groups](#atomic-groups)                     |
| **12. Subroutines and Recursion** | Reuses part of the regex by referring to a capturing group or recursively matching.                                        | [Subroutines and Recursion](#subroutines-and-recursion) |

---

## 1. **Fundamentals of Regex**

Regular expressions are a sequence of characters that form a search pattern. They can be used for various text processing tasks, such as searching, matching, and replacing strings. Below are the key components of regular expressions explained with examples.

### **1.1 Literal Characters**

**Definition**: Literal characters are the simplest form of regex and match themselves exactly.

**Example**:
```regex
abc
```
- **Matches**: The exact string `"abc"` in the text.
- **String**: `"abc def"`
  - **Match**: `"abc"`

### **1.2 Metacharacters**

**Definition**: Metacharacters have special meanings in regex and are used to create more complex search patterns. Common metacharacters include:

- **Dot (`.`)**: Matches any single character except a newline.
  
  **Example**:
  ```regex
  a.c
  ```
  - **Matches**: `"abc"`, `"a1c"`, `"a_c"` (any character between `a` and `c`).
  
- **Caret (`^`)**: Asserts the position at the start of a string.
  
  **Example**:
  ```regex
  ^Hello
  ```
  - **Matches**: The string must start with `"Hello"`.
  - **String**: `"Hello world"` (matches), `"world Hello"` (does not match).
  
- **Dollar Sign (`$`)**: Asserts the position at the end of a string.
  
  **Example**:
  ```regex
  world$
  ```
  - **Matches**: The string must end with `"world"`.
  - **String**: `"Hello world"` (matches), `"world Hello"` (does not match).

- **Asterisk (`*`)**: Matches zero or more occurrences of the preceding element.
  
  **Example**:
  ```regex
  a*
  ```
  - **Matches**: `""`, `"a"`, `"aa"`, `"aaa"`.
  
- **Plus (`+`)**: Matches one or more occurrences of the preceding element.
  
  **Example**:
  ```regex
  a+
  ```
  - **Matches**: `"a"`, `"aa"`, `"aaa"` (does not match `""`).
  
- **Question Mark (`?`)**: Matches zero or one occurrence of the preceding element.
  
  **Example**:
  ```regex
  a?
  ```
  - **Matches**: `""`, `"a"` (does not match `"aa"`).

### **1.3 Quantifiers**

Quantifiers specify how many times an element can occur.

- **Exact Number**: `{n}`
  
  **Example**:
  ```regex
  a{3}
  ```
  - **Matches**: `"aaa"` (exactly three `a`s).
  
- **At Least**: `{n,}`
  
  **Example**:
  ```regex
  a{2,}
  ```
  - **Matches**: `"aa"`, `"aaa"`, `"aaaa"` (two or more `a`s).
  
- **Range**: `{n,m}`
  
  **Example**:
  ```regex
  a{2,4}
  ```
  - **Matches**: `"aa"`, `"aaa"`, `"aaaa"` (between two and four `a`s).

### **1.4 Character Classes**

Character classes define a set of characters to match.

- **Basic Character Class**: `[...]`
  
  **Example**:
  ```regex
  [abc]
  ```
  - **Matches**: Any single character that is `a`, `b`, or `c`.
  
- **Negation**: `[^...]`
  
  **Example**:
  ```regex
  [^abc]
  ```
  - **Matches**: Any single character **except** `a`, `b`, or `c`.
  
- **Ranges**: Use `-` to specify a range of characters.
  
  **Example**:
  ```regex
  [a-z]
  ```
  - **Matches**: Any lowercase letter from `a` to `z`.

### **1.5 Special Escape Characters**

Some characters in regex have special meanings. To match them literally, escape them with a backslash (`\`).

**Example**:
```regex
\.
```
- **Matches**: A literal period (`.`).

### **1.6 Grouping and Capturing**

Parentheses `(...)` are used to group parts of the regex. This can also create capturing groups, which can be referenced later.

**Example**:
```regex
(a|b)c
```
- **Matches**: The string `"ac"` or `"bc"` (either `a` or `b` followed by `c`).
  
- **Capturing Group**: In the regex `(\d{2})-(\d{2})-(\d{4})`, the digits are captured as groups.

### **1.7 Escape Sequences**

Escape sequences are used to match special characters.

- **Common Escape Sequences**:
  - `\d`: Matches any digit (equivalent to `[0-9]`).
  - `\D`: Matches any non-digit.
  - `\w`: Matches any word character (equivalent to `[a-zA-Z0-9_]`).
  - `\W`: Matches any non-word character.
  - `\s`: Matches any whitespace character (spaces, tabs, line breaks).
  - `\S`: Matches any non-whitespace character.

**Example**:
```regex
\d{3}-\d{2}-\d{4}
```
- **Matches**: A pattern like `"123-45-6789"` (a typical Social Security Number format).

---

## 2. **Lookahead (`?=...` and `?!...`)**

Lookahead assertions allow you to check if a pattern is followed by another pattern, without including that pattern in the match.

- **Positive Lookahead (`?=...`)**: Asserts that what follows the current position matches the pattern inside `(?=...)`.

    **Example**:
    ```regex
    \d(?=\D)
    ```
    - This matches a digit `\d` only if it's followed by a non-digit `\D`.
    - **String**: `"123abc"`
      - Matches: `"1"`, `"2"`, `"3"` (only if followed by a non-digit).

- **Negative Lookahead (`?!...`)**: Asserts that what follows does **not** match the pattern inside `(?!...)`.

    **Example**:
    ```regex
    \d(?!\d)
    ```
    - This matches a digit `\d` only if it's **not** followed by another digit.
    - **String**: `"123abc"`
      - Matches: `"3"` (since it's not followed by a digit).

---

## 3. **Lookbehind (`?<=...` and `?<!...`)**

Lookbehind assertions allow you to check if a pattern is preceded by another pattern, without including that pattern in the match.

- **Positive Lookbehind (`?<=...`)**: Asserts that what precedes the current position matches the pattern inside `(?<=...)`.

    **Example**:
    ```regex
    (?<=\d)\D
    ```
    - This matches a non-digit `\D` only if it's preceded by a digit `\d`.
    - **String**: `"123abc"`
      - Matches: `"a"`, `"b"`, `"c"` (only if preceded by a digit).

- **Negative Lookbehind (`?<!...`)**: Asserts that what precedes the current position does **not** match the pattern inside `(?<!...)`.

    **Example**:
    ```regex
    (?<!\d)\D
    ```
    - This matches a non-digit `\D` only if it's **not** preceded by a digit.
    - **String**: `"123abc"`
      - Matches: `"a"`, `"b"`, `"c"` (only if not preceded by a digit).

---

## 4. **Backreferences**

Backreferences allow you to refer to a previously captured group within the same regular expression.

- **Syntax**: `\1`, `\2`, etc., refer to the first, second, etc., capturing groups.

    **Example**:
    ```regex
    (\d)\1
    ```
    - This matches any digit that is repeated.
    - **String**: `"112233"`
      - Matches: `"11"`, `"22"`, `"33"`

---

## 5. **Named Capturing Groups and Backreferences**

You can assign names to capturing groups and refer to them by name.

- **Syntax**:
    - Define: `(?P<name>...)` or `(?<name>...)`
    - Backreference: `(?P=name)` or `\k<name>`

    **Example**:
    ```regex
    (?P<digit>\d)\k<digit>
    ```
    - This matches any digit that is repeated, similar to numbered backreferences.
    - **String**: `"112233"`
      - Matches: `"11"`, `"22"`, `"33"`

---

## 6. **Non-Capturing Groups (`(?:...)`)**

Non-capturing groups group parts of the regex without creating backreferences.

- **Syntax**: `(?:...)`
  
    **Example**:
    ```regex
    (?:\d{2}-){2}\d{4}
    ```
    - This matches a pattern of two digits followed by a hyphen, repeated twice, and then four digits.
    - **String**: `"12-34-5678"`
      - Matches: `"12-34-5678"`

    **Benefit**: It groups parts of the expression for alternation or quantification without storing them for backreferencing.

---

## 7. **Lazy Quantifiers (`*?`, `+?`, `??`)**

Lazy (or non-greedy) quantifiers try to match as **few** characters as possible, as opposed to the default greedy quantifiers, which match as **many** as possible.

- **Greedy Quantifier**: `*`, `+`, `?`
- **Lazy Quantifier**: `*?`, `+?`, `??`

    **Example**:
    ```regex
    <.*?>
    ```
    - This matches the shortest possible string between `<` and `>`.
    - **String**: `"<div>text</div>"`
      - Greedy match: `"<div>text</div

>"`
      - Lazy match: `"<div>"`

---

## 8. **Anchors (`^`, `$`)**

Anchors specify positions within the string rather than matching characters.

- **Caret (`^`)**: Asserts the start of a string.

    **Example**:
    ```regex
    ^Hello
    ```
    - This matches if the string starts with `"Hello"`.

- **Dollar Sign (`$`)**: Asserts the end of a string.

    **Example**:
    ```regex
    World$
    ```
    - This matches if the string ends with `"World"`.

---

## 9. **Word Boundaries (`\b` and `\B`)**

Word boundaries allow you to match the position between a word character and a non-word character.

- **Word Boundary (`\b`)**: Asserts a position at a word boundary.

    **Example**:
    ```regex
    \bcat\b
    ```
    - This matches the word `"cat"` only when it appears as a whole word.

- **Non-Word Boundary (`\B`)**: Asserts a position that is **not** at a word boundary.

    **Example**:
    ```regex
    \Bcat\B
    ```
    - This matches `"cat"` when it appears within another word, like `"scat"` or `"catalog"`.

---

## 10. **Conditional Matching**

Conditional matching applies different patterns based on whether a capturing group has been matched.

- **Syntax**: `(?(1)then|else)`, where `1` is the capturing group.

    **Example**:
    ```regex
    (?(1)\d+|[a-z]+)
    ```
    - This matches digits if group 1 matched, otherwise matches lowercase letters.

---

## 11. **Atomic Groups**

Atomic groups prevent backtracking within that group.

- **Syntax**: `(?>...)`

    **Example**:
    ```regex
    (?>\d+)
    ```
    - This matches one or more digits and does not backtrack within this match.
  
---

## 12. **Subroutines and Recursion**

Subroutines allow you to reuse part of the regex by referring to a capturing group or recursively matching.

- **Syntax**: `(?R)` or `(?0)`, or `\d`.

    **Example**:
    ```regex
    \((?:[^()]+|(?R))*\)
    ```
    - This matches balanced parentheses, allowing for nested parentheses.

    **String**: `"(1(2(3)))"` (matches the entire string).

---

This guide provides an overview of the fundamental concepts and advanced techniques of regular expressions. By understanding these principles, you can effectively utilize regex for various text processing tasks.
