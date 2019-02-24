word = list(input("Enter any word:"))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
cap_alphabet = alphabet.upper()
correct_start_symbals = list(str(alphabet) + str(cap_alphabet) + '_')
nums = ['0','1','2','3','4','5','6','7','8','9']
correct_symbals = correct_start_symbals + nums
if word[0] in correct_start_symbals:
    print("Identificator")
    for letter in word[1:]:
        if letter not in correct_symbals:
            print("NOT Identificator")
            break
else:
    print("NOT Identificator")
