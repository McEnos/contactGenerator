import random
import string

possible_digits = string.digits #all possible digital values

#function to generate a random contact
def generate_contact():
    contact = '07'
    contact_length = len(contact)
    while contact_length < 10:
        contact += random.choice(possible_digits)
        contact_length += 1
    return contact

#function to generate a number contacts
def number_of_contacts(number_of_contacts_to_generate):
    contacts = list()
    for contact in range(number_of_contacts_to_generate):
        contacts.append(generate_contact())
    return contacts

#function for filtering particular contacts
##def filter_contact(creterion,number_of_contacts_to_generate):
##    filtered = list()
##    for i in number_of_contacts(number_of_contacts_to_generate):
##        #print(i)
##        if i.endswith(str(creterion)):
##            filtered.append(i)
##    return filtered


#function for filtering particular contacts depending on creterion provided by the user
def filter_contact(value,number_of_contacts_to_generate,creteria='end'):
    filtered = list()
    start_position = 2
    for i in number_of_contacts(number_of_contacts_to_generate):
        #print(i)
        if creteria == 'contain':
            if i.find(str(value)) > -1:
                filtered.append(i)
        elif creteria == 'start':
            if i.startswith(str(value)):
                filtered.append(i)
        else:
            if i.endswith(str(value)):
                filtered.append(i)
        
    return filtered

