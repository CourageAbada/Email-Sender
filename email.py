#An SMS Simulation
#Creating the class for the email
class emailinfo():
    def __init__(self, email_contents,from_address):
        self.email_contents = email_contents
        self.from_address = from_address
        self.has_been_read = False
        self.is_spam = False
#Function that will be used to mark emails as read
    def mark_as_read(self):
        self.has_been_read = True
#Fuction that will allow the user to mark their emails as spam
    def mark_as_spam(is_spam):
        is_spam = True
    def __repr__(self):
        return f"{self.from_address}, {self.email_contents}"

#Creating a list to append all the new email contents and address into them
inbox = []

temp_email = emailinfo("yesssirrr", "serge@mail.com")
inbox.append(temp_email)

#Fuction that is being used to take in the new emails and content then append it into the list
def add_email(conts, address):
    email = emailinfo(conts,address)
    inbox.append(email)

#Function that is used to count the amount of content in the inbox list
def get_count():
    return len(inbox)
#Function that is being used to get the email contents
def get_email(i):    
    print(inbox[i].email_contents)
#Function that is being used to get all the unread emails 
def get_unread_emails():
    unread_emails = []
    for x in inbox:
        if x.has_been_read == False:
            unread_emails.append(x)
    return unread_emails
#Funtion that is used to mark emails as spam
def get_spam_emails():
    spam_emails = []
    for i in inbox:
        if i.spam_fales == False:
            spam_emails.append(i)
    return spam_emails
#Function that is used to delete emails
def delete(i):
    inbox.pop(i)


user_choice = ""

# This is a while loop that will keep running until the user types quit.
while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/unread messages/Delete/quit? \n").lower()
    
# This is a try and except statement. It is trying to read the email and if it fails it will print "This email has been deleted"
#using the for loop to run through the emails and pick the specific index that the user inputs
    if user_choice == "read":
        try:

            for count, x in enumerate (inbox):
                print(count, x)
            i = int(input('Please enter the index: '))
            get_email(i)
        except:
            print("This email has been deleted")
            
# This is a function that allows the user to mark an email as spam.
    elif user_choice == "mark spam":
        spam_email_index = int(input('Please enter the index of the email that you would like to mark as spam:\n'))
        spam_email = inbox[spam_email_index]
        spam_email.mark_as_spam
        print(f'Your Spam emails are:\n{spam_email}')
        pass

# This is a function that allows the user to send an email.
    elif user_choice == "send":
        email_cont = input('Please add the email content:\n')
        email_addy = input('Please enter the email address:\n')
        add_email(email_cont, email_addy)
        pass


# This is a function that allows the user to see their unread emails.
    elif user_choice == 'unread messages':
        x = input('Would you like to see your unread emails? ').lower()
        if x == 'yes':
            get_unread_emails()

# This is a function that allows the user to delete an email.
    elif user_choice == 'delete':
        delete_emails = int(input('Please enter the index of the email that you want to delete:\n'))
        delete(delete_emails)
        print('The email has been deleted:')

            
# This is a function that allows the user to quit the program.
    elif user_choice == "quit":
        print("Goodbye")

# This is a function that allows the user to quit the program.
    else:
        print("Oops - incorrect input")
