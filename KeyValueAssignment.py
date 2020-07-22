phone_number = input(f'Phone Number: ')
numbers = {
 "1" : "one",
"2" : "two",
"3" : "three",
"4" : "four",
"5" : "five"
}
num = ""
for value in phone_number:
    num += numbers.get(value, "!") + " "
print(num)