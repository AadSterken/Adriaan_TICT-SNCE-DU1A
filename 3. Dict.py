
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
    for cijfer in cijferlijst.values():
        if int(cijfer) >= 9:
            print(cijferlijst)
            regel[str(cijfer)] += cijferlijst[(cijfer)]
        return print(regel)


negenplus(cijferlijst)
