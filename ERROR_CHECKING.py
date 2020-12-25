#PANSE
import re
from scanner import Scanner
scanner_output=[]
f = open("scanner output.txt","r") 
scanner_output = f.read().splitlines()
tokens=[]
tokens=scanner_output

tokens_values=[]
tokenss=[]

x=[]
for token in tokens:
    a=token.index(",")
    x=token[a+1:]
    y=token[:a]
    tokens_values.append(x)
    tokenss.append(y)
#print(tokens_values)
#print(tokenss)


class parser:

   
    def __init__(self):
         self.pointer=0
         f = open("scanner output.txt","r") 
         self.scanner_output = f.read().splitlines()

    def adv(self):
        if self.pointer!=len(tokens_values)-1:
              self.pointer=self.pointer+1  
         
       

    
    def stmt(self):
         
        if tokens_values[self.pointer]=="IF":
            self.match(tokens_values[self.pointer])
            self.IF()
    
        elif tokens_values[self.pointer]=="REPEAT":
            self.match(tokens_values[self.pointer])
            self.repeat()
         
        elif tokens_values[self.pointer]=="IDENTIFIER":
            self.assign()
         
        elif  tokens_values[self.pointer]=="READ":
            self.match(tokens_values[self.pointer])
            self.read()
          
        elif  tokens_values[self.pointer]=="WRITE":
             self.match(tokens_values[self.pointer])
             self.write()
            
        else:
            print ("ERROR stmt")

       
    
    
    def stmt_seq(self):
        while(1):
            self.stmt()
            if tokens_values[self.pointer]=="SEMICOLON": # at2kd find wala == 3latol
              self.adv()
              print(tokens_values[self.pointer])
              continue
            else:
                 break
        
           

    def assign(self):
        if tokens_values[self.pointer]=="IDENTIFIER" and tokens_values[self.pointer+1] =="ASSIGN":
            self.adv()
            self.adv()
            self.exp()
       

        
    def IF(self):
            self.exp() 
            if tokens_values[self.pointer]=="THEN":
                    self.match( tokens_values[self.pointer])
                    self.stmt_seq()
                    #self.adv()
                    if tokens_values[self.pointer]=="ELSE":
                        self.match( tokens_values[self.pointer])
                        self.stmt_seq()
                        #self.adv()
                    if tokens_values[self.pointer]=="END":
                        self.adv()
                    else:
                        print("ERROR end ") 
                    
            else:
                print("ERROR then")
                


                                
                      
    
    def repeat(self):
        self.stmt_seq()
        #self.adv()
        if tokens_values[self.pointer]=="UNTIL":
            self.match(tokens_values[self.pointer])
            self.exp()
        else:
            print("ERROR Repeat")
    
    def read(self):
        if tokens_values[self.pointer]=="IDENTIFIER":
            self.adv()
        else:
            print("ERROR read")

    def write(self):
        self.exp()
        #self.adv()

    def simple_exp(self):
        #self.adv()
        self.term()
        while(tokens_values[self.pointer]=="PLUS" or tokens_values[self.pointer]=="MINUS"):
            self.match(tokens_values[self.pointer])
            #self.adv()
            self.term()
            #self.adv()
    def exp(self):
        self.simple_exp()
        if tokens_values[self.pointer]=="LESSTHAN" or tokens_values[self.pointer]=="EQUAL":
             self.match(tokens_values[self.pointer])
             self.simple_exp()

       
           

    
    def term(self):
        #self.adv()
        self.factor()
        while(tokens_values[self.pointer]=="MULT" or tokens_values[self.pointer]=="DIV"):
            self.match(tokens_values[self.pointer])
            self.factor()
    
    def factor(self):
        if tokens_values[self.pointer]=="OPENBRACKET":
            self.match("OPENBRACKET")
        
            self.exp()
      
            self.match("CLOSEBRACKET")
         
        elif tokens_values[self.pointer]=="NUMBER":
            self.match("NUMBER")
            
        elif tokens_values[self.pointer]=="IDENTIFIER":
            self.match("IDENTIFIER")
           

        else:
           print( "ERROR factor")


    

        
      
        
    
    
    def match(self,s):
        if tokens_values[self.pointer]==s:
            self.adv()
        else:
            print("ERROR.............")

      
   #def get_next_token(self):
    #     if len(tokens_values[tokens.index(token)+1])==-1:
     #       return False
      #   else:
       #     next_token=tokens_values[tokens.index(token)+1]
        #    return next_token
     




if __name__ == "__main__" :
    p=parser()
    p.stmt_seq()
    

    


