# Command-line Python Contact-book 

The command-line python contact-book is a 
simple application which manages user 
contacts by providing features for adding,
deleting, viewing, searching and editing 
contacts.

## Features of the contact-book
1. Add contact: You can add contacts by providing
contact details in the format 'name,number,address,email'.
Contact details should be separated by commas
with no spaces.
2. Edit contact: You can edit contacts by providing
the name of the person whose details you want edited.
Press enter to skip on contact detail you do not want
edited, these details will maintain their 
original values, that is the value before the
edit.
3. View contact: You can view all contacts using
the command "view" which lists out all contacts.
4. Search contact: You can search a contact by
providing the correct name of person whose contact
you want to find.
5. Delete contact: You can delete contacts by
providing the name of the person whose contact
you want deleted.

## Getting started
1. Clone the repository to your machine 
```shell
git clone https://github.com/EmmanuelBronyah/Contact-book-modified.git
```

2. Navigate to project directory
```shell
cd contact-book
```

3. Run the program
```shell
python contact_book.py
```

4. Follow the on-screen instructions to manage
your contacts.

## Usage
* When you run the code you will be prompted to
enter a command.
* Supported commands are: '"add", "view", "delete"
"edit", "search"'
* The add command requires you to input contact
details in the format 'name,number,address,email'.
A contact information you want to leave empty
should be filled in as "None".

## Example
1. Adding contact
```shell
Enter a command > add
How many contacts do you want to add: 1
Enter contact details of contact 1 in the form "name,number,address,email": Amos,0554089278,CAPER-ST,amos@email.com
```

2. View contacts
```shell
Enter a command > view
Amos - 0554089278 - CAPER-ST - amos@email.com
```

3. Edit contacts
* Leaving any of the inputs empty will not change the
original value of that contact information. The
command line below shows 'Enter new address: '
was skipped.
```shell
Enter a command: edit
Enter the name of the person whose contact you want to edit > Amos
Enter new name: Max
Enter new number: 0234679854
Enter new address: 
Enter new email: max@email.com
```

4. Search contacts
```shell
Enter a command > search
Enter the name of the person whose contact you want to find: Max
Max - 0234679854 - CAPER-ST - max@email.com
```

5. Delete contacts
```shell
Enter a command > delete
Enter the name of the person whose contact you want to delete: Max
Cnntact deleted 
```

## Acknowledgement
* Built by Bronyah Emmanuel 
