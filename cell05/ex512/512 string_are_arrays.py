import sys 
if len(sys.argv) == 2:
    input_string = sys.argv[1]
    
    
    if 'z' in input_string:
        for char in input_string:
            if char == 'z':
                print('z')
    else:
        print("none")
else:
    print("none")