import sys 
if len(sys.argv) > 1 :
    for para in reversed(sys.argv[1:]):
        print(para)

else:
    print("none")