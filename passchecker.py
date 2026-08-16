user_pass=input('Enter password ')
has_number=False
has_alphabet=False

if len(user_pass)<6:
    print('password you enter is weak')

else:
    for character in user_pass:
        if character.isdigit():
            has_number=True

        if character.isupper():
            has_alphabet=True

    if has_number and has_alphabet:
        print('PASSWORD IS STRONG')
    else:
        print('password is meduim')

   

    



