#Printing Manga Banquet invitations.
guests = ['masashi kishimoto','eichiro oda','akira toriyama']
message = ', you have been invited to our "Greatest Manga-ka of All time Dinner"'
print("\tGuest List: " + str(guests))
print("--------------------------------------------")
print(guests[0].title() + message + "!!!!")
print(guests[1].title() + message + "!!!!")
print(guests[2].title() + message + "!!!!")

print("--------------------------------------------")
print('\tGuest: ' + guests[0].title() + ' is currently unavailable. He is currently fixing the "Boruto Issue".')
print("--------------------------------------------")

guests[0] = 'hiromu arakawa'
print("\tUpdated Guest List: " + str(guests))
print(guests[0].title() + message + "!!!!")
print(guests[1].title() + message + "!!!!")
print(guests[2].title() + message + "!!!!")

guests.insert(0, 'tite kubo')
guests.insert(2, 'satoshi tajiri')
guests.append('fuse')
print("--------------------------------------------")

print("\tUpdated Guest List: " + str(guests))
print(guests[0].title() + message + "!!!!")
print(guests[1].title() + message + "!!!!")
print(guests[2].title() + message + "!!!!")
print(guests[3].title() + message + "!!!!")
print(guests[4].title() + message + "!!!!")
print(guests[5].title() + message + "!!!!")

print("NOTICE: A bigger table was found to hold ye legends of the manga world. ")
print("--------------------------------------------")
print("--------------------------------------------")

print("NOTICE: The expected table will not arrive in time. Only Two guest will be chosen this year. ")
apology_message = ' I am sorry I am unable to invite you to this years dinner.'

popped_guest = guests.pop()
print(popped_guest.title() + apology_message)
print("--------------------------------------------")
print("\tUpdated Guest List: " + str(guests))
print("--------------------------------------------")
popped_guest = guests.pop()
print(popped_guest.title() + apology_message)
print("--------------------------------------------")
popped_guest = guests.pop()
print(popped_guest.title() + apology_message)
print("--------------------------------------------")
popped_guest = guests.pop()
print(popped_guest.title() + apology_message)
print("--------------------------------------------")
print("--------------------------------------------")
print(guests[0].title() + message + "!!!!")
print(guests[1].title() + message + "!!!!")
print("--------------------------------------------")
print("--------------------------------------------")
del guests[1]
del guests[0]
print("\tUpdated Guest List: " + str(guests))
print("--------------------------------------------")
print("--------------------------------------------")
print('Total amount of guest: ' + str(len(guests)))
print('\t\tAdding 2 guest')
guests.append('tite kubo')
guests.append('masashi kishimoto')
print('Current Guest List Members: ' + str(guests))
print('\tGuest 1: ' + str(guests[0].title()))
print('\tGuest 2: ' + str(guests[1].title()))
print('Total amount of guest: ' + str(len(guests)))
