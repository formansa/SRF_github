import student_class as sc

class st_group():
    def __init__(self,ls=None):
        if (ls != None):
            for s in ls:
                self.add_student(s)
        else:
            self.lstudents = []
                
    def add_student(self,s):
        self.lstudents.append(s)
        
    def print_group(self):
        print('Number of students: ',len(self.lstudents))
        for s in self.lstudents:
            print(s.print_info())
            
    def __repr__(self):
        print('Number of students: %r' %(len(self.lstudents)))
        
    