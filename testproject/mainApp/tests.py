from django.test import TestCase

class myData():
    
    def __init__(self,linkedin,github,my_website,medium,created=None):

        self.linkedin = linkedin
        self.github = github
        self.my_website = my_website
        self.medium = medium