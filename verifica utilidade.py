def if_procedure(self):
        if self.token.lexema == 'if':
            self.add_token()
            if self.token.lexema == '(':
                self.add_token()
                self.conditional_expression()
                self.then_procedure()
            else:
                self.treatment_error('(', 'ifProcedure')        

    def then_procedure(self):
        if self.token.lexema == ')':
            self.add_token()
            if self.token.lexema == 'then':
                self.add_token()
                if self.token.lexema == '{':
                    self.add_token()
                    #chamar o bodyProcedure
                    if self.token.lexema == '}':
                        self.add_token()
                        self.else_procedure()
                    else:
                        self.treatment_error('}', 'thenProcedure') 
                else:
                    self.treatment_error('{', 'thenProcedure') 

            else: 
                self.treatment_error('then', 'thenProcedure')    

        else:
            self.treatment_error(')', 'thenProcedure')    

    
    def else_procedure(self):
        if self.token.lexema == 'else':
            self.add_token()
            if self.token.lexema == '{':
                self.add_token()
                #chamar o bodyProcedure
                if self.token.lexema == '}':
                    self.add_token()
                else:
                    self.treatment_error('}', 'elseProcedure') 
            else:
                self.treatment_error('{', 'elseProcedure') 
        else:
            self.treatment_error('else', 'elseProcedure') 
