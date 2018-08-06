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
        #self.input_list = [self.f_name, self.l_name, self.phone_number, self.email, self.password, self.submit]
        #inputs = [x for x in input_list if input_list[x] == 'submit']
        #inn = [x for x in self.input_list if x == None]
        #print(inn)
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
            exit

    #combines f_name and l_name to form one name
    def combined_name(self):
        name = self.f_name+' '+self.l_name
        print(name)
    #validates the phone number entered
    def validate_phone(self):
        if not len(str(self.phone_number)) == 9:
            print("Enter correct phone number")
    #validates the email entered
    def validate_email(self):
        if re.search("[@]", self.email) is None:
            print('@ missing in email')
        elif re.search("[.]", self.email) is None:
            print('"." missing in  email')
        else:
            return True
    #checks whether the password is correct
    def validate_password(self):
        if not self.password == self.pass_w:
            print('Enter correct password')
        #submits the form inputs
    def submit(self):
        pass

login = Login(f_name = "kalyango", l_name = "john", phone_number = 752067415, email = 'johnkal24@gmail.com.com', password = 'kalyango1')
login.validate_phone()
login.validate_email()
login.validate_password()

