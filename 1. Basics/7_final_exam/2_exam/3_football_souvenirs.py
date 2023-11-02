team = input()
type_souvenir = input()
amount_souvenirs = int(input())

price = 0

if type_souvenir == "flags":

    if team == "Argentina":
        price = 3.25

    elif team == "Brazil":
        price = 4.20

    elif team == "Croatia":
        price = 2.75

    elif team == "Denmark":
        price = 3.10

elif type_souvenir == "caps":

    if team == "Argentina":
        price = 7.20

    elif team == "Brazil":
        price = 8.50

    elif team == "Croatia":
        price = 6.90

    elif team == "Denmark":
        price = 6.50

elif type_souvenir == "posters":

    if team == "Argentina":
        price = 5.10

    elif team == "Brazil":
        price = 5.35

    elif team == "Croatia":
        price = 4.95

    elif team == "Denmark":
        price = 4.80

elif type_souvenir == "stickers":

    if team == "Argentina":
        price = 1.25

    elif team == "Brazil":
        price = 1.20

    elif team == "Croatia":
        price = 1.10

    elif team == "Denmark":
        price = 0.90

if not team == "Argentina" and not team == "Brazil" and not team == "Croatia" and not team == "Denmark":
    print("Invalid country!")

elif not type_souvenir == "flags" and not type_souvenir == "caps" and not type_souvenir == "posters" and not type_souvenir == "stickers":
    print("Invalid stock!")

else:
    print(f"Pepi bought {amount_souvenirs} {type_souvenir} of {team} for {price * amount_souvenirs:.2f} lv.")
