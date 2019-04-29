
from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(_name_)
ask = Ask(app, '/')

"""def look(elem, input):
    fin = []
    for i in range(9):
        for j in range(7):
            if (elem[i][j] == input):
                fin.append(elem[i])
    return fin"""

@ask.launch
def start():
    return question('Que voulez vous pour votre film ?')


@ask.intent('FilmIntent')
def film(nom):
    lst = [['Avengers', '2019', 'joe russo', 'chris evans', 'action', '3h01', '5'],
           ['Simetierre', '2019', 'dennis widmyer', 'jason clarke', 'horreur', '1h41', '2'],
           ['Les crevettes pailletées', '2019', 'cédric le gallo', 'nicolas gob', 'comédie', '1h40', '0'],
           ['Victor et Célia', '2017', 'pierre jolivet', 'alice belaïdi', 'comédie', '1h30', '3']
        ,  ['Mais vous êtes fous', '2003', 'audrey diwan', 'pio marmai,drame', '1h35', '4'],
           ['90s', '2005', 'jonah hill', 'sunny suljic', 'comédie dramatique', '1h24', '2'],
           ['L adieu à la nuit', '2005', 'andré téchiné', 'catherine deneuve', 'drame', '1h43', '3'],
           ['Nous finirons ensemble', '2007', 'guillaume canet', 'françois Cluzet', 'comédie dramatique', '2h15', '4'],
           ['Dumbo', '2019', 'tim burton', 'colin farrell', 'aventure', '1h52', '3']]
    if nom is None:
        return statement('Je ne connais pas ce nom, désolé')

    fin = []
    for i in range(9):
        for j in range(6):
            if (lst[i][j] == nom):
                fin.append(lst[i])

    if len(fin)==0:
        return statement ('Désolé aucun films ne correspond à votre recherche')

    elif len(fin)==1:
        nom_film = 'J ai trouvé un film correspondant à votre demande : '
        nom_film += fin[0][0]
        return statement (nom_film)

    nom_film = 'Voici la liste des flims qui corresponde à votre demande : '
    for i in range(len(fin)):
        nom_film += fin[i][0] + ', '
    return statement (nom_film)



if _name_ == '_main_':
    app.run()
