contact_details = input()

phonebook = dict()

while len(contact_details) > 1:
    name, number = contact_details.split("-")

    if name not in phonebook:
        phonebook[name] = number

    phonebook[name] = number

    contact_details = input()

search_contacts = int(contact_details)

for contact in range(search_contacts):
    current_contact = input()

    if current_contact in phonebook:
        print(f"{current_contact} -> {phonebook[current_contact]}")

    else:
        print(f"Contact {current_contact} does not exist.")
