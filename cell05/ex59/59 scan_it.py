import sys
if len(sys.argv) == 3:
    key = sys.argv[1]
    text = sys.argv[2]
    count = text.count(key)
    if count > 0 :
        print(count)
    else:
        print("none")
else:
    print("none")
    
