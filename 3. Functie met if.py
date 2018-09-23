i = int(input('Geef je lengte in centimeters: '))


def lang_genoeg(i):
    if i > 119:
        print('Je bent lang genoeg voor de attractie!')
    else:
        print('Sorry, je bent te klein!')


lang_genoeg(i)
