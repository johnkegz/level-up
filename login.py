import re
class Login(object):
    def __init__(self, f_name = None, l_name = None, phone_number = None, email = None, password = None, submit = None):
        """
        constructor for initializing input values
        """
        self.f_name = f_name
        self.l_name = l_name
        self.phone_number = phone_number
        self.email = email
        self.password = password
        self.submit = submit
        self.pass_w = 'kalyango1'
    def empty_feilds(self):
        """
        checking for the empty feilds
        """
        if self.f_name == None:
            print("Enter first name")
        elif self.l_name == None:
            print("Enter Last name")
        elif self.phone_number == None:
            print("Enter phone number")
        elif self.email == None:
            print("Enter email")
        elif self.password == None:
            print("Enter password")
        else:
            return True

    #combines f_name and l_name to form one name
    def combined_name(self):    
        name = self.f_name+' '+self.l_name
        return name      
    #validates the phone number entered
    def validate_phone(self):
        if not len(str(self.phone_number)) == 10:
            return "Enter correct phone number"
        else:
            return True
    #validates the email entered
    def validate_email(self):
        if re.search("[@]", self.email) is None:
            return '@ missing in email'
        elif re.search("[.]", self.email) is None:
            return '"." missing in  email'
        else:
            return True
    #checks whether the password is correct
    def validate_password(self):
        if not self.password == self.pass_w:
            return 'Enter correct password'
        else:
            return True
        #submits the form inputs
    def submit_inputs(self):
        feilds = self.empty_feilds()      
        valid_phone = self.validate_phone()
        valid_email = self.validate_email()
        valid_password = self.validate_password()
        name = self.combined_name()
        if (feilds == True) and (valid_email ==True) and (valid_phone == True) and (valid_password == True):
            final_input = [name, self.phone_number, self.email, self.password]
            print(final_input)
            print("YOU HAVE LOGGED IN SUCCESS FULLY")
        else:
            error_list = [feilds, valid_phone, valid_email, valid_password]
            error = [x for x in error_list if x != True]
            print(error) 
login = Login(f_name = "kalyango", l_name = "john", phone_number = '0752067415', email = 'johnkal24@gmail.com', password = 'kalyango1', submit = 'submit')
login.submit_inputs()

