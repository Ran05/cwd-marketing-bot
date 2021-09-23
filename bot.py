def greet(bot_name):
    print("Hello! My name is {0}.".format(bot_name))
    print("We'd like to help you with your digital marketing needs! We'll help you build your brand online by creating a website, SEO, Social media marketing and more!\nReady to take your business to the next level?")


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))


def count():
    print('Now I want to know how can I help you?')
    services= str(input())

    counter = 0
    while counter <= services:
        print("{0} !".format(counter))
        counter += 1

        print(output)
output = f"""
========== Please Select by choosing number ==========
"""

def test():
    print("Okay now Can you tell me what type of website you want to build?")
    print("Here is the ordered list: ")
    print("1. Informational ")
    print("2. E-commerce")
    print("3. Online Booking")
    print("4. Membership")
    print("5. Combination")



    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())

    print('Completed, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')


def end():
    print('Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()
    
greet('Randolfh')  # change it as you need
remind_name()
count()
test()
end()
