my_nouns = {
    'repère (m)':'marque ou objet permettant de s\'orienter dans l\'espace, de localiser quelque chose',
    'repère (m)':'ce qui permet de reconnaître ou de localiser quelque chose dans un ensemble',
    'étirement (m)':'une pratique corporelle destinée à développer la souplesse corporelle (raison pour laquelle on l\'appelle parfois assouplissement) ou à préparer le corps à l\'exercice et à favoriser la récupération consécutive à un effort physique',
    'déchirure (f)':'rupture, accroc; grande douleure morale causeé par une séparation',
    'clef (f)':'clé',
    'cahier (m)':'ensemble formé par plusieurs feuilles de papier réunies, et qui est destiné à l\'écriture',
    'fadaise (f)':'plaisanterie niaise ou chose insignifiante ; baliverne ; niaiserie, futilité (surtout pluriel)',
    'égard (m)':'marques de considération, d\'estime témoignées à quelqu\'un; respect, déférence, prévenance',
    'écart (m)':'distance entre deux choses/personnes; différence de valeur, de quantité, d\'intensité',
    'souricière (f)':'petit appareil pour prendre les souris',
    'piège (m)':'engin servant pout attirer/prendre des animaux; difficulté/problème volontairement dissimulé pour provoquer une erreur en cas d\'inattention/d\'ignorance'
    }
	
my_verbs = {
    'rédiger':'écrire un texte dans une forme élaborée et en respectant les règles du genre auquel il appartient',
    'éteindre':'faire cesser la combustion ou le fonctionnement; faire affaiblir, atténuer, our faire perdre l\'energie',
    'avouer':'reconnaître qu\'on a fait, pensé quelque chose de mal, de fâcheux, de regrettable; reconnaître l\'autre chose comme vrai',
    'navrer':'être attristé de quelque chose, désolé, confus',
    'jaillir':'sortir, sous forme de jet; se produire/manifester de façon soudaine et avec vivacité',
    'éprouver':'soumettre quelque chose à certaines expériences pour vérifier sa valeur; juger de la valeur intellectuelle/morale de quelqu\'un',
    'aborder':'arriver à un lieu par la mer, l\'atteindre; arriver à un carrefour, s\'y engager; commencer l\'étude d\'un sujet/question, commencer à en parler',
    's\'emparer':'conquérir; arrêter qualqu\'un; saisir quelque chose, le prendre pour son usage',
    'obnubiler':'obscurir les facultés mentales, fausser le jugement',
    'abreuver':'faire boire des animaux; imbiber (pénétrer d\'eau) profondement la terre',
    'craindre':'avoir peur de; être intimidé par quelqu\'un; èpreuver de l\'inquiétude devant les réactions de quelqu\'un, ses jugements possibles',
    'haïr':'abhorrer, exécrer quelqu\'un; avoir de la répugnance, de l\'horreur pour quelque chose',
    'vanter':'faire l\'éloge de quelque chose/quelqu\'un, en ènoncer les mérites; présenter quelque chose à quelqu\'un de façon très élogieuse, le metter en valor',
    'se vanter':'étaler son propre mérite, rèel ou imaginaire; tirer orgueil, vanité de quelque chose, en être fier',
    'débouter':'rejeter une demande en justice',
    'hocher':'remuer la tête de haut en bas en signe d\'approbation ou la remuer de gauche à droite en signe de refus'
    }

my_adjectives = {
    'maladroit':'qui manque d\'adresse, d\'aisance, d\'habileté dans ses mouvements, ces gestes; qui manque d\'experience, de sûreté, de savoir-faire',
    'vif':'qui est en vie',
    'toutefois (adverbe)':'néanmoins, cependant, pourtant',
    'dérisoire':'négligeable',
    'pendu':'suspendu dans l\'aire; mort par pendaison',
    'cinglé':'qui à l\'esprit dérangé; fou'
    }

import json
s = json.dumps(my_nouns)
with open("/Users/rvolosh/Documents/tools and old work/vocab quizzes/grepractice/my_words/my_nouns.txt","w") as f:
	f.write(s)

s = json.dumps(my_verbs)
with open("/Users/rvolosh/Documents/tools and old work/vocab quizzes/grepractice/my_words/my_verbs.txt","w") as f:
	f.write(s)
	
s = json.dumps(my_adjectives)
with open("/Users/rvolosh/Documents/tools and old work/vocab quizzes/grepractice/my_words/my_adjectives.txt","w") as f:
	f.write(s)
