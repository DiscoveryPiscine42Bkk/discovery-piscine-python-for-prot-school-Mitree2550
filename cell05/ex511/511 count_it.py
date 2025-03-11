import sys
if len(sys.argv)>1:
    print("parameters:", len(sys.argv) - 1)
    for para in sys.argv[1:]:
        print(f"{para} {len(para)}")

else:
    print("none")