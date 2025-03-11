import sys

if len(sys.argv) == 2:
    para = sys.argv[1]
    user = input("Enter a word:")
    if user ==para:
        print("Good job")
    else:
        print("Nope, sorry...")
else:
    print("none")