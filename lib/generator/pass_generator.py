import random
import string
import pyperclip
from ..db.main import *
from ..db.password_table import Password



def create_pass(site):
    passw=Password.new_password(session)
    Password.save_pass(session,site, passw)

def copy_pass(site):
    pyperclip.copy(Password.search(session,site).password)


def site_list():
    return [row.site for row in Password.list_site(session)]

def delete_pass(site):
    Password.delete_pass(session,site)
    
