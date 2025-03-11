import sys
def shrink(str):
    print(str[:8])
def enlarge(str):
    print(str.ljust(8, 'Z'))
if len(sys.argv) < 2:
    print("none")
else:    
    for para in sys.argv[1:]:
        if len(para) > 8:
            shrink(para)  
        elif len(para) < 8:
            enlarge(para) 
        else:
            print(para)  