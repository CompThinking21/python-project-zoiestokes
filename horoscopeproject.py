import requests
import json
#import request allows for the api to be implemented
#import json allows for the aztro data to be stored in a dictionary
sign_list = ["capricorn", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "aries", "aquarius"]
#create list that stores all horoscope signs
def getsign():
    get_sign = str(input("please enter your sign: ")).lower()
    if get_sign in sign_list:
        return get_sign
#create a function that contains a varible that allows the user to imput their sign, the if statement allows for the program to get the sign in the list
    else:
        print("imput not applicable please try again")
        getsign()
#the else statment accounts for if the user imputs anything other then a sign from the list
user_sign = getsign()
params = (
('sign', user_sign),
 ('day', 'today'))
aztrodata = requests.post('https://aztro.sameerkumar.website/', params=params)
# def findhoroscope():
aztrodictionary = aztrodata.json()
def description():
    print(aztrodictionary['description'])
def compatibility():
    print(aztrodictionary['compatibility'])
#call back to main menu and edit the main menu when you come back to the code(personal note)
def mainmenu():
    menu ={}
    menu['1']="find horoscope"
    menu['2']="find compatibility"
    menu['3']="change sign"
    menu['4']="exit"
    while True:
        options=menu.keys()
        #options.sort()
        for entry in options:
            print(entry, menu[entry])
        selection=input("Please Select:")
        if selection =='find horoscope':
              description()
              #call description function instead 0f print add
        elif selection == 'find compatibility':
              compatibility()
              # call function for finding compatibility not yet made
        elif selection == 'change sign':
            getsign()
        elif selection == 'exit':
            break
        else:
              print("Unknown Option Selected!")
mainmenu()
#
# #input allows for the user to enter their sign. I will create a statment that raises an error if the user imputs something other then a sign
# def horo():
# #created a function that stores all of the horoscopes
#     if signs == 'capricorn':
#         print('Capricorns are the ultimate worker bees; they are ambitious, organized, practical, goal-oriented, and they do not mind the hustle. They are ready to give up a lot in order to achieve that goal, Verk says. They also love making their own rules, which means they strive to reach high career positions.')
#     elif signs == 'taurus':
#         print('Practical and well-grounded, Taurus is the sign that harvests the fruits of labor. They feel the need to always be surrounded by love and beauty, turned to the material world, hedonism, and physical pleasures. People born with their Sun in Taurus are sensual and tactile, considering touch and taste the most important of all senses. Stable and conservative, this is one of the most reliable signs of the zodiac, ready to endure and stick to their choices until they reach the point of personal satisfaction.')
#     elif signs == 'gemini':
#         print('Expressive and quick-witted, Gemini represents two different personalities in one and you will never be sure which one you will face. They are sociable, communicative and ready for fun, with a tendency to suddenly get serious, thoughtful and restless. They are fascinated with the world itself, extremely curious, with a constant feeling that there is not enough time to experience everything they want to see.')
#     elif signs == 'cancer':
#         print('Deeply intuitive and sentimental, Cancer can be one of the most challenging zodiac signs to get to know. They are very emotional and sensitive, and care deeply about matters of the family and their home. Cancer is sympathetic and attached to people they keep close. Those born with their Sun in Cancer are very loyal and able to empathize with other peoples pain and suffering.')
#     elif signs == 'leo':
#         print('People born under the sign of Leo are natural born leaders. They are dramatic, creative, self-confident, dominant and extremely difficult to resist, able to achieve anything they want to in any area of life they commit to. There is a specific strength to a Leo and their "king of the jungle" status. Leo often has many friends for they are generous and loyal. Self-confident and attractive, this is a Sun sign capable of uniting different groups of people and leading them as one towards a shared cause, and their healthy sense of humor makes collaboration with other people even easier.')
#     elif signs == 'virgo':
#         print('Virgos are always paying attention to the smallest details and their deep sense of humanity makes them one of the most careful signs of the zodiac. Their methodical approach to life ensures that nothing is left to chance, and although they are often tender, their heart might be closed for the outer world. This is a sign often misunderstood, not because they lack the ability to express, but because they won’t accept their feelings as valid, true, or even relevant when opposed to reason. The symbolism behind the name speaks well of their nature, born with a feeling they are experiencing everything for the first time.')
#     elif signs == 'libra':
#         print('People born under the sign of Libra are peaceful, fair, and they hate being alone. Partnership is very important for them, seeking someone with the ability to be the mirror to themselves. These individuals are fascinated by balance and symmetry, they are in a constant chase for justice and equality, realizing through life that the only thing that should be truly important to themselves in their own inner core of personality. This is someone ready to do nearly anything to avoid conflict, keeping the peace whenever possible')
#     elif signs == 'scorpio':
#         print('Scorpios are passionate and assertive people with determination and focus you rarely see in other zodiac signs. They will turn to in-depth research to reach the truth behind anything they find important. Great leaders and guides, Scorpios are resourceful, dedicated and fearless when there is challenge to be overcome. They will hold on to other people’s secrets, even when they aren’t very fond of them to begin with and do anything they can for those they tie themselves to.')
#     elif signs == 'sagittarius':
#         print('Curious and energetic, Sagittarius are the travelers of the zodiac. Their open mind and philosophical view motivate them to wander around the world in search of the meaning of life. Sagittarius is an extrovert, always optimistic, full of enthusiasm, and ready for changes. This is a Sun sign of individuals who are often preoccupied with mental work, but when they find grounding, they show their ability to transform visions and thoughts into concrete actions and circumstances.')
#     elif signs == 'aries':
#         print('As the first sign in the zodiac, the presence of Aries always marks the beginning of something energetic and turbulent. They are continuously looking for dynamic, speed and competition, always being the first in everything - from work to social gatherings. Thanks to its ruling planet Mars and the fact it belongs to the element of Fire (just like Leo and Sagittarius), Aries is one of the most active zodiac signs. It is in their nature to take action, sometimes before they think about it.')
#     elif signs == 'aquarius':
#         print('Aquarius is the sign different from the rest of the zodiac and people born with their Sun in it feel special. This makes them eccentric and energetic in their fight for freedom, or at times shy and quiet, afraid to express their true personality. In both cases they are deep thinkers and highly intellectual people who love to fight for idealistic causes. They are able to see people without prejudice and this makes them truly special. Although they can easily adapt to the energy that surrounds them, Aquarius representatives have a deep need to have some time alone and away from everything in order to restore power.')
#the if statements allow for the user to get information about the sign they imputed
