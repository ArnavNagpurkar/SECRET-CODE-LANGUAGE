# Start
print("---------------------Welcome--------------------")

# Code or Decode?
choice = input('Code or Decode?(Enter "C" to and "D" to decode): ')

r1 = "adg"  # 3 Random characters at starting
r2 = "qwe"  # 3 Random characters at ending

# Exit if input is sentence
def codeSen():
    if " " in st:
        print("Enter a word not a sentence to convert! \nExiting...!")
        exit()
    if len(st)>=20:
        print("Please enter a small value under 20 characters \nExiting..!")
        exit()

# Code
if choice == "C" or choice == "c" or choice == "code":
    st = input("Enter the word to code: ")
    codeSen()
    st = st[1:] + st[0]
    code = (r1) + (st) + (r2)
    print(f"Secret code word is '{code}'")

# Decode
elif choice == "D" or choice == "d" or choice == "decode":
    st = input("Enter the word to decode: ")
    codeSen()
    st = st[-4] + st[3:-4]
    print(f"Secret word was '{st}'")

# Exit
elif choice == "E" or choice == "e" or choice == "exit":
    print("Exiting...!")
    exit()

# Invalid Input
else:
    print("Invalid Input \nExiting..!")

# End...!
