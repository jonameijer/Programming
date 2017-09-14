x = eval(input('Hoe lang ben je: '))
def lang_genoeg(x):
    return x

if lang_genoeg(x) >= 120:
    print('Je bent lang genoeg voor de attractie!')
else:
    print('Sorry, je bent te klein!')