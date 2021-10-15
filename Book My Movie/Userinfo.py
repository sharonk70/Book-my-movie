class User_Info(dict): 
    def __init__(self): 
        self.d = dict()
          
     
    def add_Details(self,name1,age1,gender1,phone1,price1): 
        self['Name:-'] = name1
        self['Age:-'] = age1
        self['Gender:-'] = gender1
        self['Phone:-'] = phone1
        self['Price:-'] = price1
    
    def Create_User(self,key):
        self.d[key]=self
        return self.d
