class contact_management:
    
    def __init__(self):
        self.name=[]
        self.contact_no=[]
        self.email=[]

    def insert(self,name,contact_no,email):
        self.name.append(name)
        self.contact_no.append(contact_no)
        self.email.append(email)

    def display(self):
        contacts=[]
        for i in range(len(self.name)):
            contacts.append({
                'name':self.name[i],
                'email':self.email[i],
                'contact_no':self.contact_no[i],
                
            })
        return contacts

    def update(self,name,email,contact):
        
        for i in range(len(self.name)):
            if self.name[i].lower()==name.lower():
                self.contact_no[i]=contact
                self.email[i]=email
                return True
            
        return False

    def delete(self,name):
        for i in range(len(self.name)):
            if self.name[i].lower()==name.lower():
                self.name.remove(self.name[i])
                self.email.remove(self.email[i])
                self.contact_no.remove(self.contact_no[i])
                return True
        return False
    def search(self,name):
        for i in range(len(self.name)):
            if self.name[i].lower()==name.lower():
                return ({
                    'name':self.name[i],
                    'email':self.email[i],
                    'contact_no':self.contact_no[i],
                })
        return None
                



        


