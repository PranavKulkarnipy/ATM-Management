class atm:
    def __init__ (self):
        self.pin=''
        self.balance=''
        self.menu()
    
    def menu(self):
        user_input=input(""""
        Welcome To our ATM
        1.Enter pin        
        2.Change pin
        3.cash withdrawl                                                  
        """)

        if user_input=='1':
            self.create_pin()
        elif user_input=='2':        
             self.change_pin()
        elif user_input=='3':
             self.cash_withdraw()
        
        else:
             exit()


    def create_pin(self):
         user_pin=int(input("Enter a pin"))
         self.pin=user_pin
         
         
         user_balance=int(input("Enter a balance"))
         self.balance=user_balance 

         print("pin created successufully")
         self.menu()


    def change_pin(self):
         old_pin=int(input("Enter old pin"))
          
         if old_pin==self.pin:
              new_pin=int(input("Enter a new pin"))
              print("new pin created successufully")
              self.menu()
         else:
              print("you have entered wrong pin") 
              self.menu()

    def cash_withdraw(self):
         user_pin=int(input("Enter a pin"))
         if user_pin==self.pin:
              amount=int(input("enter amount for cash withdraw"))
              
         if amount <= self.balance:
             self.balance=self.balance - amount
             print("cash withdraw successufully , Balance is", self.balance)
             
             self.menu()

                        
obj=atm()

    