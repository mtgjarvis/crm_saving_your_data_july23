



class CRM:

  def main_menu(self):
    while True: # repeat indefinitely
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)
  #
  #
  def print_main_menu(self):
    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')
  #
  #
  def call_option(self, user_selected):
    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      exit('Goodbye')
    else:
      print('Invalid Selection')
      print('')
  #
  #
  def add_new_contact(self):
    print('Enter First Name: ')
    first_name = input().lower()

    print('Enter Last Name: ')
    last_name = input().lower()

    print('Enter Email Address: ')
    email = input() 

    print('Enter a Note: ')
    note = input().lower() 

    contact = Contact.create(first_name, last_name, email, note)
    return contact
  #
  #
  def modify_existing_contact(self):
    contact_id = int(input('Which id would you like to change?'))
    # contact_to_modify = Contact.find(contact_id)
    attribute_to_update = input('Please enter which attribute you would like to update: first name, last name, email, or note: ').lower()
    new_data = input(f'Enter the new info for {attribute_to_update}: ').lower()
    Contact.contacts[contact_id - 1].update(attribute_to_update, new_data)
  #
  #
  def delete_contact(self):
    id_to_delete = int(input('Enter the index number you would like to delete: '))
    Contact.delete(id_to_delete - 1)

  def display_all_contacts(self):
    all_contacts = Contact.all()
    for contact in all_contacts:
      print(contact)
    print('')

  #
  def search_by_attribute(self):
    select_attribute = input('Enter the attribue you would like search by, first name, last name, email or note: ')
    select_term_to_search = input('Enter the term you would like to find: ')
    print(Contact.find_by(select_attribute, select_term_to_search))

crm_app = CRM()
crm_app.main_menu()
# CRM.add_new_contact(1)
# print(len(Contact.contacts))