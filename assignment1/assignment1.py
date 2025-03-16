# Write your code here.

# Task 1

def hello():
    return "Hello!"

# Task 2

def greet(name):
    return f"Hello, {name}!"

# Task 3

def calc(a, b, operation = "multiply"):
    total_calc = 0
    try:
        if operation == "add":
            total_calc = a + b
        elif operation == "subtract":
            total_calc = a - b
        elif operation == "multiply":
            total_calc = a * b
        elif operation == "divide":
            try:
                total_calc = a / b
            except ZeroDivisionError:
                total_calc = str()
                total_calc = "You can't divide by 0!"
        elif operation == "modulo":
            total_calc = a % b
    except Exception:
        total_calc = str()
        total_calc = "You can't multiply those values!"
    return total_calc

# Task 4

def data_type_conversion(value, type):
    
    # convert to integer type
    if type == "int":
        try:
            value = int(value)
        except Exception:
            value = f"You can't convert {value} into a {type}."
            
    # convert to float type
    elif type == "float":
        try:
            value = float(value)
        except Exception:
            value = f"You can't convert {value} into a {type}."
    
    # convert to string typer
    elif type == "str":
        try:
            value = str(value)
        except Exception:
            value = f"You can't convert {value} into a {type}."
            
    return value

# Task 5

def grade(*args):
    try:
        # check if no arguments were provided
        if len(args) == 0:
            return "Invalid data was provided."
        
        # compute the average of the provided scores
        avg = sum(args) / len(args)
        
        # grades based on the average
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    except Exception:
        return "Invalid data was provided."
    
# Task 6

def repeat(string, count):
    try:
        result = ""
        for _ in range(count):
            result += string
    except Exception as e:
        print(f"Error: {e}")
        
    return result


# Task 7

def student_scores(pos, **kwargs):
    
    # Find the average score
    if pos == "mean":
        try:
            avg_score = 0
            sum_score = 0
            score_length = 0
            for key, value in kwargs.items():
                sum_score += value
                score_length += 1
                avg_score = sum_score / score_length
            return avg_score
        except Exception as e:  
            print(f"Error: {e}")
    # Find the best student with the highest score
    elif pos == "best":
        try:
            best_student = ""
            current_score = 0
            for key, value in kwargs.items():
                if value > current_score:
                    current_score = value
                    best_student = key
                else:
                    continue
            return best_student
        except Exception as e:  
            print(f"Error: {e}")

# Task 8

def titleize(string):
    # Rules for book title
    # (1) The first word is always capitalized.
    # (2) The last word is always capitalized.
    # (3) All the other words are capitalized, except little words.
    #  For the purposes of this task, the little words are "a", "on", "an", "the", "of", "and", "is", and "in".
    
    # Little words
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    
    words = string.split()
    
    if not words:
        result = ""
    else:
        try:
            new_words = []
            for i, word in enumerate(words):
                # Always capitalize the first and last word.
                if i == 0 or i == len(words) - 1:
                    new_words.append(word.capitalize())
                else:
                    # If the word is a little word, make it lowercase
                    # If not, capitalize it.
                    if word.lower() in little_words:
                        new_words.append(word.lower())
                    else:
                        new_words.append(word.capitalize())
            result = " ".join(new_words)
        except Exception as e:
            print(f"Error: {e}")
    return result

# Task 9

def hangman(secret, guess):
    result = ""
    
    # Loop through the secret words and only change words to _ if they are not "guess" words
    try:
        for i in secret:
            if i in guess:
                result += i
            else:
                result += "_"
    except Exception as e:
            print(f"Error: {e}")
    return result


# Task 10

def pig_latin(sentence):
    
    # Rules:
    # (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end. 
    # (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them. 
    # (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
    
    vowels = "aeiou"
    words = sentence.split()
    result = []
    try:
        for word in words:
            # if the word starts with a vowel, just add "ay" at the end
            if word[0] in vowels:
                result.append(word + "ay")
            else:
                i = 0
                # move through the word until a vowel is foun
                # treating "qu" as a single consonant sound
                while i < len(word):
                    if word[i] in vowels:
                        break
                    # if a 'q' is encountered and followed by a 'u'
                    # treat both letters as part of the initial consonant cluster
                    if word[i] == 'q' and i + 1 < len(word) and word[i + 1] == 'u':
                        i += 2
                        break
                    i += 1
                # rearrange the word
                # move the leading consonant cluster to the end and add "ay"
                result.append(word[i:] + word[:i] + "ay")
                result = " ".join(result)
    except Exception as e:
            print(f"Error: {e}")
    return result