import baroque, classical, romantic

all_composers = {}
all_composers.update(baroque.COMPOSERS)
all_composers.update(classical.COMPOSER)
all_composers.update(romantic.COMPOSERS)

def show_list():
    print("List of composers:")
    for composer in all_composers:
        print("-", composer)

def show_composer(name):
    info = all_composers[name]
    print()
    print(name, "(", info["years"], ")")

    print ("Fun Facts:")
    for fact in info["fun_facts"]:
        print(" *", fact)

    print("Pieces:")
    for piece in info["pieces"]:
        print(" *", piece["title"], "(", piece["year"], "):", piece["piece_feel"])
    print()

show_list()

while True:
    choice = input("\nType a composer's name (or q to quit): ").strip().lower()

    if choice == "q":
        break

    found = False
    for name in all_composers:
        if choice != "" and choice in name.lower():
            show_composer(name)
            found = True
            break
    if not found:
        print("Composer not found! Did you mean any of these?")
        show_list()
