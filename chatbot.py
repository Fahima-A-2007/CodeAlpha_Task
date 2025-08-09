def hello():
    print("Hi")

def howareyou():
    print("I'm fine, thanks!")

def bye():
    print("Goodbye!")

 
inp = input("Enter 'hello!', 'how are you?', 'bye' or type 'exit' to quit: ")

while inp.lower() != "exit":
    if inp.lower() == "hello!":
        hello()
    elif inp.lower() == "how are you?":
        howareyou()
    elif inp.lower() == "bye":
        bye()
    else:
        print("I can't understand.")

    
    inp = input("Enter 'hello!', 'how are you?', 'bye' or type 'exit' to quit: ")
