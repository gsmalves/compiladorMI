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

            'formalParameterList': ['decLiteral',
                                    'octLiteral',
                                    'hexLiteral',
                                    'floatLiteral',
                                    'global.',
                                    'local.',
                                    '(',
                                    'IDE',
                                    'CAD',
                                    'true',
                                    'false',
                                    '-'],
            'formalParameterListRead': ['IDE'],

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

            'value': ['decLiteral',
                     'octLiteral',
                     'hexLiteral',
                     'floatLiteral',
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
             

            'index': ['decLiteral',
                     'octLiteral',
                     'IDE'],

            'vector': ['['],

            'matrix': ['['],


            'assignmentVector': ['='],

            'assignmentVectorAux': ['='],

            'valueAssignedVector': ['decLiteral',
                                    'octLiteral',
                                    'hexLiteral',
                                    'floatLiteral',
                                    'true',
                                    'false',
                                    'CAD'],

            'assignmentMatrix': ['='],

            'assignmentMatrixAux': ['='],

            'dimensionMatrix' : [ ','],

            'valueAssignedMatrix': ['decLiteral',
                                    'octLiteral',
                                    'hexLiteral',
                                    'floatLiteral',
                                    'true',
                                    'false',
                                    'CAD'],
            
            'while': ['while'],

            'whileProcedure': ['while'],

            'boolenaLiteral': ['true',
                              'false'],

            'conditionalExpression':['decLiteral',
                                    'octLiteral',
                                    'hexLiteral',
                                    'floatLiteral',
                                    'true',
                                    'false',
                                    '(',
                                    'global.',
                                    'local.',
                                    'CAD',
                                    '!',
                                    '-'],

            'if': ['if'],

            'then': [')'],

            'else': ['else'],

            'ifProcedure': ['if'],

            'thenProcedure': [')'],

            'elseProcedure': ['else'],

            'read': ['read'],

            'print': ['print'],

            'body': ['decLiteral',
                     'octLiteral',
                     'hexLiteral',
                     'floatLiteral',
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

            'bodyItem': ['decLiteral',
                     'octLiteral',
                     'hexLiteral',
                     'floatLiteral',
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

            'bodyProcedure':['decLiteral',
                            'octLiteral',
                            'hexLiteral',
                            'floatLiteral',
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

            'bodyItemProcedure':['decLiteral',
                            'octLiteral',
                            'hexLiteral',
                            'floatLiteral',
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

        
            'logicalDenied': ['!'],

            'logical': ['&&',
                       '||'],

            'expressionValueLogical':['decLiteral',
                                      'octLiteral',
                                      'hexLiteral',
                                      'floatLiteral',
                                      'true',
                                      'false',
                                      'global.',
                                      'local.',
                                      '-',
                                      'CAD',
                                      'IDE'],     

            'logicalExpression':    ['decLiteral',
                                      'octLiteral',
                                      'hexLiteral',
                                      'floatLiteral',
                                      'true',
                                      'false',
                                      'global.',
                                      'local.',
                                      '-',
                                      'CAD',
                                      'IDE'],  

            'relacionalExpression':  ['decLiteral',
                                      'octLiteral',
                                      'hexLiteral',
                                      'floatLiteral',
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

            'assign':['decLiteral',
                    'octLiteral',
                    'hexLiteral',
                    'floatLiteral',
                    'true',
                    'false',
                    '('
                    'global.',
                    'local.',
                    '-'],                                                

            'exp':['decLiteral',
                    'octLiteral',
                    'hexLiteral',
                    'floatLiteral',
                    'true',
                    '('
                    'false',
                    'global.',
                    'local.',
                    '-'],       

            'addExp': ['+',
                      '-'],
        
            
            'term':['decLiteral',
                    'octLiteral',
                    'hexLiteral',
                    'floatLiteral',
                    '(',
                    'IDE',
                    'CAD',
                    'true',
                    'false',
                    '-'],     

            'expressionValue':['decLiteral',
                    'octLiteral',
                    'hexLiteral',
                    'floatLiteral',
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
