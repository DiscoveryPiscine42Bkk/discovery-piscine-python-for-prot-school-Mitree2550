import sys
def downcase_it(str):
    return str.lower()
if len(sys.argv) > 1:
    for para in sys.argv[1:]:
        print(downcase_it(para))
else:
    print("none")
