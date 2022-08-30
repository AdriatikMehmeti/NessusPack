import json,os,random

try:
    import pymailtm

except:

    os.system('clear')

    a = input('[!] Missing "pymailtm" \n[?] Do you want to install y/n: ')

    if a.lower() == 'y': os.system('python -m pip install pymailtm')
    else: exit('[-] Exiting.')


class InvalidDbAccountException(Exception):
    """Raised if an account could not be recovered from the db file."""

class EmailManage:

    def __init__(self, email = None, password = None, account = None):
        self.email = email
        self.password = password
        self.account = account
        self.passw_length = 20
        # simple db
        self.db_file = 'nessus_activate.pymailtm'
        self.text_style = {'HEADER': '\033[95m',
                           'OKBLUE': '\033[94m',
                           'OKCYAN': '\033[96m',
                           'OKGREEN': '\033[92m',
                           'WARNING': '\033[93m',
                           'FAIL': '\033[91m',
                           'ENDC': '\033[0m',
                           'BOLD': '\033[1m',
                           'UNDERLINE': '\033[4m'}

    def generate_password(self, uppercase = False, lowercase = True , digit = False, length = None):
        if length is None:
            length = self.passw_length

        chars = ''

        if uppercase == True:
            chars += 'string.ascii_uppercase +'

        if lowercase == True:
            chars += 'string.ascii_lowercase +'

        if digit == True:
            chars += 'string.digits'

        return ''.join(random.choices(chars, k = length))

    def INIT(self):
        pm = pymailtm
        if self.password is None:
            self.password = self.generate_password(lowercase=True,uppercase=True,digit=True)
        self.account = pm.MailTm().get_account(self.password)
        self.email = self.account.address

        # Save email account detail to prevent duplicate and failed request for activation code

    def read_message(self):
        print('[#] Message box:\n'.upper(),self.account.get_messages(),'\n[#] ============= end  ============= \n'.upper())

    def wait_message(self):
        print('[#] Waiting for Message!'.upper(),'\n{}[~]{} Email:{} {}\n'.format(self.text_style.get('WARNING'),self.text_style.get('OKBLUE'),self.email,self.text_style.get('ENDC')))
        self.account.wait_for_message()
        print('\n[#] ============= end  ============= \n'.upper())

    def _save_account(self,):
        """Save the account data for later use."""
        data = {
            "id": self.account.id_,
            "address": self.account.address,
            "password": self.account.password
        }
        with open(self.db_file, "a+") as db:
            json.dump(data, db)

        print('[+] Successfuly saved email account.\n')

    def _load_account(self):
        """Return the last used account."""
        with open(self.db_file, "r") as db:
            data = json.load(db)
        # send a /me request to ensure the account is there
        if "address" not in data or "password" not in data or "id" not in data:
            # No valid db file was found, raise
            raise InvalidDbAccountException()
        else:
            self.email = data["address"]
            self.password = data["password"]
            self.id = data["id"]
            self.account = pymailtm.Account(self.id, self.email, self.password)

            print('[+] Successfuly loaded email account.\n')

            return self.account

    def get_info(self):
        print('[+] email: ' + str(self.email),'\n[+] password: ' + str(self.password),'\n[+] Account: ' + str(self.account))
        return {'email':str(self.email),'password':str(self.password)}
