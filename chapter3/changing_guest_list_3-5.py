#Printing Manga Banquet invitations.
guests = ['masashi kishimoto','eichiro oda','akira toriyama']
message = ', you have been invited to our "Greatest Manga-ka of All time Dinner"'
print("Guest List: " + str(guests))
print("--------------------------------------------")
print(guests[0].title() + message + "!!!!")
print(guests[1].title() + message + "!!!!")
print(guests[2].title() + message + "!!!!")

print("--------------------------------------------")
print('Guest: ' + guests[0].title() + ' is currently unavailable. He is currently fixing the "Boruto Issue".')
print("--------------------------------------------")

guests[0] = 'hiromu arakawa'
print("Updated Guest List: " + str(guests))
print(guests[0].title() + message + "!!!!")
print(guests[1].title() + message + "!!!!")
print(guests[2].title() + message + "!!!!")

