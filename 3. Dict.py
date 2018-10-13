
cijferlijst = {'Adriaan' : '9',
               'Francien' : '8',
               'Henk' : '6',
               'Marieke' : '9',
               'Piet': '10',
               'Harry' : '4',
               'Manon' : '7',
               'Peter' : '10'}

def negenplus(cijferlijst):
    regel = {}
    for item in cijferlijst.items():
        if int(item[1]) >= 9:
           regel[item[0]] = item[1]
    return print(regel)


negenplus(cijferlijst)
