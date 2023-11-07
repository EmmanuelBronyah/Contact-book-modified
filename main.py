def print_intro():
    print(f'Enter "add" to add a contact \n'
          f'Enter "edit" to edit a contact \n'
          f'Enter "search" to find a contact or contacts \n'
          f'Enter "view" to view contacts \n'
          f'Enter "delete" to delete a contact \n')


class Contact:
    def __init__(self, name, number, address, email):
        self.name = name
        self.number = number
        self.address = address
        self.email = email

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def __str__(self):
        return f'{self.name} - {self.number} - {self.address} - {self.email}'


def main():
    print_intro()
    correct_input = True
    while correct_input:
        user_input = get_user_input()
        match user_input:
            case None:
                print('Enter a valid command')
            case 'add':
                add_contact()
            case 'edit':
                edit_contact()
            case 'search':
                search_contact()
            case 'view':
                view_contact()
            case 'delete':
                delete_contact()
            case 'exit':
                correct_input = False


global contact_book
contact_book = []


def get_user_input():
    """
    Takes input from the user

    Input from the user is validated against allowed inputs.
    Input from the user upon passing validation is returned.
    None is returned if input from user fails validation.
    """
    allowed_inputs = ['add', 'edit', 'search', 'view', 'delete', 'exit']
    user_input = input('Enter a command > ').lower()
    if user_input in allowed_inputs:
        return user_input
    return None


def add_contact():
    """
    Adds contact to the globally declared contact book list

    Input contact detail in the form 'name,number,address,email', without spaces and separated by commas .
    """
    try:
        number_of_contacts = int(input('How many contacts do you want to add > '))
        if number_of_contacts > 0:
            for i in range(1, number_of_contacts+1):
                contact = input(f'Enter contact details of contact {i} '
                                f'in the form "name,number,address,email": ').lower().split(',')
                try:
                    name, number, address, email = contact
                    contact_book.append(Contact(name, number, address, email))
                except ValueError:
                    print('Fill in empty detail as "None"')
        else:
            print('Number should not be zero or less')
    except ValueError:
        print('Enter a valid number')


def edit_contact():
    """
    Makes changes to a contact detail.

    Name of person for contact edit is validated against person objects in the globally declared contact book.
    The attribute of person object is assigned the new value if the new value is not empty.
    The attribute of person object is assigned to its previous value if the new value is empty.
    """
    name = input('Enter the name of the person whose contact you want to edit: ').lower()
    for person in contact_book:
        if person.name == name:
            new_name = input('Enter new name: ')
            person.name = new_name if new_name != '' else person.name
            new_number = input('Enter new number: ')
            person.number = new_number if new_number != '' else person.number
            new_address = input('Enter new address: ')
            person.address = new_address if new_address != '' else person.address
            new_email = input('Enter new email: ')
            person.email = new_email if new_email != '' else person.email
            break
    else:
        print('There is no such contact')


def search_contact():
    """
    Finds contacts by the name provided as input from the user.

    """
    name_to_search = input('Enter the name of the person whose contact you want to find: ').lower()
    for person in contact_book:
        if person.name == name_to_search:
            print(person)
    else:
        print('There is no such contact.')


def view_contact():
    """
    Lists out all contacts from the globally declared contact book list.

    """
    if contact_book:
        for person in contact_book:
            print(person)
    else:
        print('Contact book is empty')


def delete_contact():
    """
    Deletes contact using name provided by the user.

    """
    if contact_book:
        name = input('Enter the name of the person whose contact you want to remove: ').lower()
        for person in contact_book:
            if person.name == name:
                contact_book.remove(person)
                print('Contact deleted')
        else:
            print(f'Contact with contact name {name} does not exist')
    else:
        print('Contact book is empty')


if __name__ == '__main__':
    main()
