import requests
import json
#import request allows for the api to be implemented
#import json allows for the aztro data to be stored in a dictionary, so we can grab certain parts of that data and use it when it is needed
sign_list = ["capricorn", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "aries", "aquarius"]
#create list that stores all horoscope signs, this is important because the user will be able to now imput any of these 12 signs
user_sign = ""
#user_sign is empty so it can be used in the program
aztrodictionary = {}
def getsign():
    get_sign = str(input("please enter your sign: ")).lower()
    if get_sign in sign_list:
        user_sign = get_sign
        params = (
        ('sign', user_sign),
        ('day', 'today'))
        aztrodata = requests.post('https://aztro.sameerkumar.website/', params=params)
        aztrodictionary = aztrodata.json()
#this function contains a varible that allows the user to imput their sign, the if statement allows for the program to get the sign in the list
    else:
        print("imput not applicable please try again")
        getsign()
#the else statment accounts for if the user imputs anything other then a sign from the list
getsign()
#I put in place the parameters necessary for aztrodata to be used throughout my program
#Created a dictionary to store the aztrodat
def description():
    print(aztrodictionary['description'])
#This function allows for the user to get a description of their sign, the user can access the capabilities of this function through the main menu that starts on line 31
def compatibility():
    print(aztrodictionary['compatibility'])
#This function allows for the user to find the capatibility of their sign and will also work through the main menu
def mainmenu():
#This function allows for the main menu to work
    menu ={}
#The curly brackets are necessary because of the dictionary
    menu['1']="find horoscope"
    menu['2']="find compatibility"
    menu['3']="change sign"
    menu['4']="exit"
#The main menu allows for the user to access the functions called description and compatibility
    while True:
        options=menu.keys()
        #options.sort()
        for entry in options:
            print(entry, menu[entry])
        selection=input("Please Select:")
        #Lets the user know that they have to select an option
        if selection =='find horoscope':
            description()
        elif selection == 'find compatibility':
            compatibility()
        #if and elif statements are necessary for the user to have multiple options on the menu
        elif selection == 'change sign':
            getsign()
        #Allows for the user to change the sign they previously imputed
        elif selection == 'exit':
            break
        else:
              print("Unknown Option Selected!")
mainmenu()
