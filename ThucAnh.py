#1
a = str(input("Nhap chuoi: "))
print ("do dai: ", len(a))

#2
a = input(str("Nhap chuoi: "))
String = {}
for i in a:
  if i in String:
    String[i] += 1
  else:
    String[i] = 1
print(String)

#3
a = str(input("Nhap chuoi: "))
if len(a) >= 2:
  print (a[:2] + a[-2:])
else:
  print ("Empty string")

#4
a = str(input("Nhap chuoi: "))
a1 = a[0]
b = a1

for char in a[1:]:
  if char == a1:
    b += "$"
  else:
    b += char

print(b)

#5
a = str(input("Nhap chuoi: "))
b = str(input("Nhap chuoi thu 2: "))
print(b[:2] + a[2:] + " " + a[:2]+ b[2:])

#6
a = str(input("Nhap chuoi: "))
if len(a) >= 3:
  if a[-3:] == "ing":
    print (a + "ly")
  else:
    print (a + "ing")
else:
  print (a)

#7
a = str(input("Nhap chuoi: "))
result = a.replace("not that poor", "good!")
print(result)

# 8.
def find_longest_word(strings):
    longest = ""
    max = 0

    for word in strings:
        if len(word) > max:
            longest = word
            max = len(word)

    return longest, max

words_list = (input("Nhap 1 chuoi bat ki: ")).split()
longest, length = find_longest_word(words_list)
print("Longest word:", longest)
print("Length:", length)

#9
a = str(input("Nhap chuoi: "))
b = int(input("Nhap so: "))

result = ""

for i in range(len(a)):
    if i == b:
      result += ""
    else:
      result += a[i]

print(result)

#10
a = str(input("Nhap chuoi: "))
a1 = a[0]
a2 = a[-1]
print(a2 + a[1:-1] + a1)

#11
a = str(input("Nhap chuoi: "))
even_char = ""
for i in range(len(a)):
  if i % 2 == 0:
    even_char += a[i]
print(even_char)

#12
a = str(input("Nhap chuoi: "))
count = {}
words = a.split()

for i in words:
  if i in count:
    count[i] += 1
  else:
    count[i] = 1
print(count)

# 13.
a = str(input("Nhap chuoi: "))
print(a.upper())
print(a.lower())

#14
a = input("nhap chuoi co phay: ").split(",")

words = []
for i in a:
  words.append(i.strip())

b = []
for i in words:
  if i not in b:
    b.append(i)

print(". ".join(sorted(b)))

#17
a = str(input("Nhap chuoi: "))
if len(a) < 2:
  print( "empty string")
else:
  print(a[-2:]*4)

#18
a = str(input("Nhap chuoi: "))
if len(a) >= 3:
  print(a[:3])
else:
  print(a)

#20
a = str(input("Nhap chuoi: "))
if len(a) % 4 == 0:
  print(a[::-1])

#21
a = str(input("Nhap chuoi: "))
def upper_str(a):
  count = 0
  for char in a[:4]:
    if char == char.upper():
     count +=1
     if count >=2:
       return a.upper()

print (upper_str(a))

#22
a = str(input("Nhap chuoi: "))

Up = []
Low = []
number = []
special = []

for i in a:
  if i.isupper():
    Up.append(i)
  elif i.islower():
    Low.append(i)
  elif i.isdigit():
    number.append(i)
  else:
    special.append(i)

result = sorted(Up) + sorted(Low) + sorted(number) + sorted(special)
print(" ".join(result))

#23
a = str(input("Nhap chuoi co dong: "))
print(a.replace("\n", " "))

#24
a= str(input("Nhap chuoi: "))

x = a.startswith("Hello")

print(x)

#25
def caesar_encrypt(Text, step):
    out = []
    crypt = []

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for eachLetter in Text:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)

            crypting = (index + step) % 26
            crypt.append(crypting)

            newLetter = uppercase[crypting]
            out.append(newLetter)

        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)

            crypting = (index + step) % 26
            crypt.append(crypting)

            newLetter = lowercase[crypting]
            out.append(newLetter)

    return out
a = str(input("Nhap chuoi: "))
b = int(input("Nhap so: "))
print(caesar_encrypt(a, b))

#26
import textwrap

a = """Painting is a timeless form of artistic expression that conveys emotions, stories, and ideas. From ancient cave paintings to modern digital art, it has evolved across cultures and eras. Artists use color, texture, and composition to create visually compelling works that inspire and provoke thought."""

format = textwrap.fill(a, width=50)

print(format)

#27
a ='''
      Painting is a timeless form of artistic expression that conveys emotions, stories, and ideas.
      From ancient cave paintings to modern digital art, it has evolved across cultures and eras.
      Artists use color, texture, and composition to create visually compelling works that inspire and provoke thought.
'''
clean = textwrap.dedent(a)

print(clean)

#28
a ='''
      Painting is a timeless form of artistic expression that conveys emotions, stories, and ideas.
      From ancient cave paintings to modern digital art, it has evolved across cultures and eras.
      Artists use color, texture, and composition to create visually compelling works that inspire and provoke thought.
'''
print(a.splitlines())

#30
x = 3.5343543
print("{:.2f}".format(x))
y = 11.535466
print("{:.2f}".format(y))

#35
a = int(input("Nhap so: "))
print("{:,}".format(a))

#36
a = float(input("Enter a number: "))
percentage = a / 100
print(f"{percentage:.2f}")

#38
a = 'The lady standing over there has a white lace dress that gleaming in the sun.'

print(a.count("the"))

#39
a = str(input("Nhap chuoi: "))
print(a[::-1])

def reverse_words(a):
  words = a.split()
  reversed_words = words[::-1]
  return " ".join(reversed_words)

a = input("Enter a string: ")
reversed_string = reverse_words(a)
print("Reversed string:", reversed_string)

#41
def strip_chars(input_string, chars):
    result = ''.join(char for char in input_string if char not in chars)
    return result

a = "Good morning"
chars_to_strip = "o,n"
stripped_string = strip_chars(a, chars_to_strip)
print(f"Original string: {a}")
print(f"Stripped string: {stripped_string}")

#42
import collections

a = 'The lady standing over there has a white lace dress that gleaming in the sun.'
d = collections.defaultdict(int)
for c in a:
    d[c] += 1
for c in sorted(d, key=d.get, reverse=True):
    if d[c] > 1:
        print('%s %d' % (c, d[c]))

def char_index(string):
  for index, char in enumerate(string):
    print(f"Current character {char} position at {index}")

sample_string = "Good mornign"
char_index(sample_string)

# 47.
get_str = input("Nhap chuoi: ")
low = int(input("chuoi duoc ghi thuong den: "))

result = get_str[:low].lower() + get_str[low:]

print(result)

# 48.
a = input("Nhap chuoi: ")

swapp = []

for char in a:
    if char == ".":
      swapp.append(",")
    elif char == ",":
      swapp.append(".")
    else:
       swapp.append(char)

print("".join(swapp))

# 49.
a = input("Nhap chuoi: ")

vowels = {"u", "e", "a", "o", "i"}
is_vowel = [char for char in a if char in vowels]

print(f"So luong so nguyen am: {len(is_vowel)}")
print(f"cac chu cai nguyen am: {''.join(is_vowel)}")

#51
def Norepeat(string):
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    for char in string:
        if counts[char] == 1:
            return char
    return None

a = str(input("Nhap chuoi: "))
result = Norepeat(a)

if result:
    print(f"chu khong bi lap lai: {result}")
else:
    print("khong co chu nao bi lap lai")

#53
def Repeat(string):
    counts = {}
    for char in string:
        if char in counts:
            return char
        counts[char] = 1
    return None

a = str(input("Nhap chuoi: "))
result = Repeat(a)

if result:
    print(f"chu dau tien bi lap lai: {result}")
else:
    print("khong co chu nao lap lai")

#60
def capitalize(text):
    words = text.split()
    result = []
    for word in words:
        if len(word) > 1:
            result.append(word[0].upper() + word[1:-1] + word[-1].upper())
        elif len(word) == 1:
            result.append(word[0].upper())
        else:
            result.append("")
    return " ".join(result)

a = str(input("Nhap chuoi: "))
result = capitalize(a)
print(result)

# 70
def uncommon_chars(a, b2):
    combined_str = ""

    for char in a:
        if char not in b and char not in combined_str:
            combined_str += char
    for char in b:
        if char not in a and char not in combined_str:
            combined_str += char
    return combined_str

a = str(input("Nhap chuoi: "))
b = str(input("Nhap chuoi: "))
result = uncommon_chars(a, b)
print(result)

# 77
def count(s):
    n = len(s)
    return n * (n + 1) // 2

a = "abcdefg"
count = count(a)
print(count)

#79
def Smallest(text):
    words = text.split()
    if not words:
        return None, None

    smallest_word = min(words, key=len)
    largest_word = max(words, key=len)

    return smallest_word, largest_word

input_string = "The lady standing over there has a white lace dress that gleaming in the sun."
smallest, largest = Smallest(input_string)

if smallest is not None and largest is not None:
    print("chu nho nhat:", smallest)
    print("chu lon nhat:", largest)
else:
    print("Empty!.")

#86
def delete(string, char):
    modified = string.replace(char, "")
    return modified

a = "The lady standing over there has a white lace dress that gleaming in the sun."
b = "a"
result = delete(a, b)
print(result)

#87
def common_values(a, b):
    common = ""
    for char in a:
        if char in b and char not in common:
            common += char
    return common

a = str(input("Nhap chuoi: "))
b = str(input("Nhap chuoi: "))
result = common_values(a, b)
print(result)

#88
import re

def check_string(input_string):

    if len(input_string) < 8:
        return False

    if not re.search("[A-Z]", input_string):
        return False

    if not re.search("[a-z]", input_string):
        return False

    if not re.search("[0-9]", input_string):
        return False

    return True

a = input("Nhap chuoi: ")

if check_string(input_string):
    print(["hop le"])
else:
    print(["khong hop le"])

#98
def decapitalize(string):
    if not string:
        return string
    return string[0].lower() + string[1:]
a = str(input("Nhap chuoi: "))
result = decapitalize(a)
print(result)

#99
a = '''
      The lady standing
      over there has a white
      lace dress that gleaming
      in the sun.
'''
print(a.splitlines())

#104
def capitalize(string):
  if not string:
    return string
  return string[0].upper() + string[1:].lower()

a = "GoOd MorNINg"
capitalized = capitalize(a)
print(a)
print(capitalized)

#106
def remove(string):
    if not string:
        return ""

    result = [string[0]]
    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            result.append(string[i])
    return "".join(result)

strings = ["Red Green White", "aabbbcdeffff", "Yellowwooddoor"]
for string in strings:
    updated_string = remove(string)
    print(f'"{string}" -> "{updated_string}"')

#110
def insert_spaces(word):
    result = ""
    for i, char in enumerate(word):
        result += char
        if i < len(word) - 1 and char.islower() and word[i+1].isupper():
            result += " "
    return result
a = str(input("Nhap chuoi: "))
print(insert_spaces(a))
