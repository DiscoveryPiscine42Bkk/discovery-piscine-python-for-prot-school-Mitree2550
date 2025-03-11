import sys
if len(sys.argv) == 3:
    try:
       
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = list(range(num1, num2))
        print(result)
        
    except ValueError:
        print("none")
else:
    print("none")