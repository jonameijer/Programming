def new_password(newpassword,oldpassword):
    return newpassword != oldpassword and len(newpassword) >= 6
b = input('Old password: ')
a = input('New password: ')
print(new_password(a,b))

