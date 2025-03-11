import sys
def find_the_redheads(family_dict):
    redheads = list(filter(lambda name: family_dict[name] == "red", family_dict))
    return redheads
family = {
    "New": "black",
    "Drogba": "red",
}
redhead_names = find_the_redheads(family)
print(redhead_names)