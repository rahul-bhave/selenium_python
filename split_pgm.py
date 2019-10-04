# python string operation

my_string1="TrainingseniorQA,program"

split_wit_spaces=my_string1.split(",")
print(split_wit_spaces)

# Paragraph split
my_intro = "I am QA engineer. I live in Mumbai"
print("What do you do?")
my_answer1 = my_intro.split()[0] + my_intro.split()[1] + my_intro.split()[2] + my_intro.split()[3]
print(my_answer1)

# my list search list

my_list=['Ronaldo', 'Messi', 'Neymar']
search_string='Messi'
for item in my_list:
    if search_string in item:
        print(search_string)
    