# Task 1
def hello():
    return "Hello!"

# Task 2
def greet(name):
    return "Hello, " + name + "!"

#Task 3
def calc(x,y,z='multiply'):
    try: 
        match z:
            case 'add':
                return x+y
            case 'subtract':
                return x-y
            case 'multiply':
                return x*y
            case 'divide':
                try:
                    return x/y
                except ZeroDivisionError:
                    return("You can't divide by 0!")
            case 'modulo':
                try:
                    return x%y
                except ZeroDivisionError:
                    return("You can’t take modulo by 0!")
            case 'int_divide':
                try:
                    if type(x)== int and type(y)==int:
                        return x/y
                    else:
                        raise TypeError
                except TypeError:
                    return("x and y should ne integers")
                except ZeroDivisionError:
                    return("You can't divide by 0!")
            case 'power':
                try:
                    x**y
                except ZeroDivisionError:
                    return("0 cannot be raised to a negative power!")
    except:
        return("You can't " + z + " those values!")

#Task 4
def data_type_conversion(value, name):
    try:
        match name:
            case 'str':
                return str(value)
            case 'float':
                return float(value)
            case 'int':
                return int(value)
    except ValueError:
        return("You can't convert " + value + " into a " + name +".")
    
#Task 5
def grade(*args):
    try:
        value = sum(args)/len(args)
        if value >= 90:
            return 'A'
        elif 80<=value<90:
            return 'B'
        elif 70<=value<80:
            return 'C'
        elif 60<=value<70:
            return 'D'
        else:
            return 'F'
    except TypeError:
        return('Invalid data was provided.')
    
#Task 6
def repeat(string, count):
    new_str = ''
    for i in range(count):
        new_str += string
    return new_str

#Task 7
def student_scores(par, **kwargs):
    if par == 'best':
        max_val = max(kwargs.values())
        for key, value in kwargs.items():
            if value == max_val:
                return key
    elif par == 'mean':
        return sum(kwargs.values())/len(kwargs.values())
    
#Task 8
def titleize(title):
    words = title.split()
    words[0] = words[0].capitalize()
    words[-1] = words[-1].capitalize()
    for i, word in enumerate(words):
        if i != 0 and i != len(words)-1:
            if word not in ["a", "on", "an", "the", "of", "and", "is", "in"]:
                words[i] = word.capitalize()
    return " ".join(words)

#Task 9
def hangman(secret, guess):
    final_hangman =''
    for letter in secret:
        if letter in guess:
            final_hangman += letter
        else:
            final_hangman += '_'
    return final_hangman

#Task 10
def pig_latin(string):
    vowels = ['a', 'e','i','o','u']
    strings = string.split()
    new_str = []
    for word in strings:
        new_word = ''
        if word[0] in vowels:
            new_word = word + 'ay'
        else:
            consonants = ''
            for i,let in enumerate(word):
                if let =='q' and word[i+1] =='u':
                    consonants += 'qu'
                    continue
                elif let not in vowels:
                    consonants += let
                else:
                    break
            new_word = word[len(consonants):] + consonants + 'ay'
        new_str.append(new_word)
    return ' '.join(new_str)
