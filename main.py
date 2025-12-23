import csv #Comma Seperated Values. expalanation=>below
#csv is case sensitive so always use name phone email in lower case in whole program. 
file_name="contacts.csv"
#function to load contacts from csv file
def load_contacts():
    contacts=[]
    try:
        with open(file_name,"r") as file:
            reader=csv.DictReader(file)#expalanation=>below
            for row in reader:#row means dictionary in reader(above created object)
                contacts.append(row)#adds each dictionary(row) to that list
    except FileNotFoundError:
        contacts=[]
    return contacts
#function to save contacts
def save_contacts(contacts):
    with open(file_name,"w") as file:
        feildnames=["name","phone","email"]#expalanation=>below
        writer=csv.DictWriter(file,fieldnames=feildnames)#expalanation=>below
        writer.writeheader()#expalanation=>below
        writer.writerows(contacts)#expalanation=>below
#function to add new contacts
def add_contact(contacts):
    name=input("Enter name:")
    phone=input("Enter phone number:")
    email=input("Enter email:")
    contact={"name":name,"phone":phone,"email":email}#<=dictionary
    contacts.append(contact)#to add the contacts in the list
    save_contacts(contacts)#to save the added contacts
    print(f"\nContact '{name}' added successfully!!!")
def veiw_contacts(contacts):
    if not contacts:
        print("No contacts found!!!!")
    print("\n...Contact List...")
    for contact in contacts:
        print(f"name:{contact['name']}, phone#:{contact['phone']}, email:{contact['email']}")
    print()
#function to saerch contacts
def search_contacts(contacts):
    name=input("Enter name to search:")
    for contact in contacts:
        if name==contact['name']:
            print(f"\nContact found.\nname:{contact['name']}\nphone#:{contact['phone']}\nemail:{contact['email']}")
            break
        else:
            print("Invalid Name....Contact not found!!")
#Main functio
def main():
    contacts=load_contacts()
    while True:#explanation=>below
        print("===Contact Manager===")
        print("1.Add Contact")
        print("2.Veiw Contacts")
        print("3.Search Contacts")
        print("4.Exit")
        choice=input("Enter your choice(1-4):")
        if choice=='1':
            add_contact(contacts)
        elif choice=="2":
            veiw_contacts(contacts)
        elif choice=='3':
            search_contacts(contacts)
        elif choice=='4':
            print("Exiting Contact Manager, GoodBye!")
            break
        else:
            print("Invalid Choice")
if __name__=="__main__":#only run the main() if the file is being run directly
    main()              #don't print anything if it is imported
'''1.csv is a plain text file used to store data in table format(rows and 
columns).we use this file because all programs(excel,python,googlesheet etc)
can open and save csv file.
2.csv.DictReader is a special reader in python csv module which reads data 
from csv file and convert each row into a dictionary.
11.append()=>to add dictionaries in the list or file too.
18.fieldnames are headers in csv file to identify and label the data
19.csv.DictWriter is is used to write data to a csv file using dictionaries.
20.This writes(column names) the first row of csv as a header(name,phone,email)
21.contacts is a list of dictionaries, each dictionary is representing a row 
and it writes all datain rows to the csv
50.while True:to create an infinite loop until we break it manually like we used 
exit here.we used it in menue if we want the menue to keep showing again and 
again after user finishes the one action if we don't use it the program will
be closed after finishing one task. '''
