#imports
#Importing the decoder function
from decoder import decode_secret

def main():
    #Grab url from user input -- assuming that it is a valid url, unless throw an error
    url = input("Please enter the url here: ")
    print() #print a new blank line
    decode_secret(url)

if __name__ == '__main__':
    main()