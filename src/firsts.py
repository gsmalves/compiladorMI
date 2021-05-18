class Firsts: #ANCHOR verificar vazio nas produções, se precisa ou não!
    def __init__(self):
        self.firsts = {

                        
            'prefixGlobalLocal':  ['global.',
                                    'local.'],

            'program': ['start',
                        'IDE',
                        'const',
                        'procedure',
                        'function',
                        'struct',
                        'var',
                        'typedef'],

            'globalDecl': ['const'
                            'var',],

            'boolean': ['true',
                        'false'],
                        
            'start': ['start'],

            'decls': ['function',
                      'procedure',
                      'struct',
                      'typedef'
                      'IDE'],

            'decl': ['function',
                     'procedure',
                     'struct',
                     'typedef'
                     'IDE'],

            'formalParameterList': ['NRO',
                                    'global.',
                                    'local.',
                                    '(',
                                    'IDE',
                                    'CAD',
                                    'true',
                                    'false',
                                    '-'],
            'formalParameterListRead': ['IDE',
                                        'CAD'],

            'functionDeclaration': ['function'],
                                                
            'procDecl': ['IDE',
                        'procedure'],

            'params': ['IDE',
                       'const',
                       'struct',
                       'int',
                       'real',
                       'boolean',
                       'string'],

            'param': ['IDE',
                       'const',
                       'struct',
                       'int',
                       'real',
                       'boolean',
                       'string'],
            
            'functionCall': ['IDE'],

            'typedefDecl': ['typedef'],

            'base': ['IDE',
                    'struct',
                    'int',
                    'real',
                    'boolean',
                    'string'],

            'structDecl': ['struct'],
                        
            'extends': ['extends'],

            'constDecl': ['const'],

            'const': ['IDE'],

            'delimiter': [',',
                         ';'],

            'type': ['struct',
                    'int',
                    'real',
                    'boolean',
                    'string'],

            'value': ['NRO',
                     'true',
                     'false',
                     'NRO'],

            'var': ['var'],

            'variablesList': ['IDE',
                              'struct'
                              'int',
                              'real',
                              'boolean',
                              'string'],     
                              
            'variable': ['IDE'],

            'aux': [',',
                   ';',
                   '='
                   '['],
             

            'index': ['NRO',
                     'IDE'],

            'vector': ['['],

            'matrix': ['['],


            'assignmentVector': ['='],

            'assignmentVectorAux': ['='],

            'valueAssignedVector': ['NRO',
                                    'true',
                                    'false',
                                    'CAD'],

            'assignmentMatrix': ['='],

            'assignmentMatrixAux': ['='],

            'dimensionMatrix' : [ ','],

            'valueAssignedMatrix': ['NRO',
                                    'true',
                                    'false',
                                    'CAD'],
            
            'while': ['while'],

            'whileProcedure': ['while'],

            'boolenaLiteral': ['true',
                              'false'],

            'conditionalExpression':['true',
                                    'false',
                                    'CAD',
                                    'IDE'],

            'if': ['if'],

            'then': [')'],

            'else': ['else'],

            'ifProcedure': ['if'],

            'thenProcedure': [')'],

            'elseProcedure': ['else'],

            'read': ['read'],

            'print': ['print'],

            'body': ['var',
                     'if',
                     'while',
                     'print',
                     'read'],

            'bodyItem': ['NRO',
                     'true',
                     'false',
                     'global.',
                     'local.',
                     '(',
                     'IDE',
                     'while',
                     'read',
                     'print',
                     'return',
                     '-',
                     'CAD',
                     'if'],

            'returnStetement': ['return'],

            'bodyProcedure':['NRO',
                            'true',
                            'false',
                            'global.',
                            'local.',
                            '(',
                            'IDE',
                            'while',
                            'read',
                            'print',
                            'return',
                            '-',
                            'CAD',
                            'if'], 

            'bodyItemProcedure':['NRO',
                            'true',
                            'false',
                            'global.',
                            'local.',
                            '(',
                            'IDE',
                            'while',
                            'read',
                            'print',
                            'return',
                            '-',
                            'CAD',
                            'if'], 

            'conditionalOperator': ['&&',
                                   '||'],

        

            'logical': ['&&',
                       '||'],

            'expressionValueLogical':['NRO',
                                      'true',
                                      'false',
                                      'global.',
                                      'local.',
                                      'CAD',
                                      'IDE'],     

            'logicalExpression':    ['NRO',
                                      'true',
                                      'false',
                                      'global.',
                                      'local.',
                                      '-',
                                      'CAD',
                                      'IDE'],  

            'relacionalExpression':  ['NRO',
                                      'true',
                                      'false',
                                      'global.',
                                      'local.',
                                      '-',
                                      'CAD',
                                      'IDE'],   

            'relational': ['<',
                          '>',
                          '<=',
                          '>=',
                          '==',
                          '!='],

            'assign':['NRO',
                    'true',
                    'false',
                    '('
                    'global.',
                    'local.',
                    '-'],                                                

            'exp':['NRO',
                    'true',
                    '('
                    'false',
                    'global.',
                    'local.',
                    '-'],       

            'addExp': ['+',
                      '-'],
        
            
            'term':['NRO',
                    '(',
                    'IDE',
                    'CAD',
                    'true',
                    'false',
                    '-'],     

            'expressionValue':['NRO',
                    '(',
                    'IDE',
                    'CAD',
                    'true',
                    'false',
                    '-'],    

            'multExp': ['*',
                        '/'],
                         
        }

    def get_first(self, production: str, lexema):
        production_firsts = self.firsts.get(production)

        if production_firsts:
            "print(production_firsts)"

            return production_firsts.__contains__(lexema)
