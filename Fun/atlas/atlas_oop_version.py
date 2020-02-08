import random

class player:
    played = []
    countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua & Deps', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Rep', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea North', 'Korea South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'St Kitts & Nevis', 'St Lucia', 'Saint Vincent & the Grenadines', 'Samoa', 'San Marino', 'Sao Tome & Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad & Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
    def clear_game():
        player.played = []
        #greedy_player.clearMoves()
        #random_player.clearMoves()

class greedy_player(player):
    __moves = 0
    __lastplayed=None
    __playerName=''
    def __init__(self,name):
        self.__playerName=name
    def getName(self):
        return self.__playerName
    def move(self,letter):
        self.__moves = self.__moves + 1
        match = []
        for i in player.countries:
            if(letter.upper() == i[0].upper()) and (i not in player.played):
                match.append(i)
        if len(match)==0:
            return None
        c = dict()
        for i in match:
            count = 0
            for j in player.countries:
                if(i[-1].upper()==j[0].upper()) and (j not in player.played):
                    count = count + 1
            c[i] = count
        x =  min(c.items(), key = lambda x: x[1])[0]
        (player.played).append(x)
        self.__lastplayed = x[-1]
        return x

    def getMoves(self):
        return self.__moves

    def getLastPlayed(self):
        return self.__lastplayed

    def clearMoves(self):
        self.__moves=0

class random_player(player):
    __moves=0
    __lastplayed=None
    __playerName=''
    def __init__(self,name):
        self.__playerName=name
    def getName(self):
        return self.__playerName
    def move(self,letter):
        self.__moves = self.__moves + 1
        match = []
        for i in player.countries:
            if (letter.upper() == i[0].upper() ) and  (i not in player.played):
                match.append(i)
        if len(match)==0:
            return None
        x = random.choice(match)
        (player.played).append(x)
        self.__lastplayed = x[-1]
        return x

    def getMoves(self):
        return self.__moves

    def getLastPlayed(self):
        return self.__lastplayed

    def clearMoves(self):
        self.__moves=0

'''class master_player(player):
    __moves=0
    __lastplayed=None
    __playerName=''
    def __init__(self,name):
        self.__playerName=name
    def getName(self):
        return self.__playerName
    '''

def game_2(player1,player2,r=False):
    if(r==True):
        lst = [player1,player2]
        random.shuffle(lst)
        player1,player2 = lst

    start='s'
    while(True):
        x = player1.move(start)
        #print('{} : {} {}'.format(player1.getName(),x,player1.getMoves()))
        if(x==None):
            return [player2.getName(),min(player1.getMoves(),player2.getMoves())]
        y = player2.move(x[-1])
        #print('{} : {}'.format(player2.getName(),y))
        if(y==None):
            return [player1.getName(),min(player1.getMoves(),player2.getMoves())]
        start = y[-1]

'''p1 = greedy_player('greedy_Player 1')
p2 = greedy_player('greedy_Player 2')
p3 = random_player('random_player 1')
p4 = random_player('random_player 2')
print(game_2(p1,p4))'''

N = int(input('Enter Number of games: '))
print('p1: greedy_player1, p2:greedy_player2, p3:random_player1, p4:random_player2')
players = input('Enter 2 players: ').split()
p1 = greedy_player('p1')
p2 = greedy_player('p2')
p3 = random_player('p3')
p4 = random_player('p4')

if(players[0]=='p1'):
    player1 = p1
elif(players[0]=='p2'):
    player1 = p2
elif(players[0]=='p3'):
    player1 = p3
else:
    player1 = p4

if(players[1]=='p1'):
    player2 = p1
elif(players[1]=='p2'):
    player2 = p2
elif(players[1]=='p3'):
    player2 = p3
else:
    player2 = p4

winners = []
moves = []
print()

for i in range(0,N):
    game = game_2(player1,player2)
    #print(game)
    winners.append(game[0])
    moves.append(game[1])
    player.clear_game()
    player1.clearMoves()
    player2.clearMoves()

counts = dict()
counts[player1.getName()]=0
counts[player2.getName()]=0
for i in winners:
    counts[i] = counts.get(i,0) + 1
x =  max(counts.items(), key = lambda x: x[1])[0]
avg_moves = sum(moves)/N
print('{} : won- {}% times'.format(player1.getName(),(counts[player1.getName()]/N)*100))
print('{} : won- {}% times'.format(player2.getName(),(counts[player2.getName()]/N)*100))
print("Average game lenght = ",avg_moves)
