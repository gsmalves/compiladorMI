class Firsts: #ANCHOR verificar vazio nas produções, se precisa ou não!
    def __init__(self):
        self.firsts = {
           
           
            'number': ['decLiteral',
                        'octLiteral',
                        'hexLiteral',
                        'floatLiteral',],
                        
            'prefixGlobalLocal':  ['global.',
                                    'local.'],

            'program': ['start',
                        'identifier',
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
                      'identifier'],

            'decl': ['function',
                     'procedure',
                     'struct',
                     'typedef'
                     'identifier'],

            'formalParameterList': ['decLiteral',
                                    'octLiteral',
                                    'hexLiteral',
                                    'floatLiteral',
                                    'global.',
                                    'local.',
                                    '(',
                                    'identifier',
                                    'stringLiteral',
                                    'true',
                                    'false',
                                    '-'],
            'formalParameterListRead': ['identifier'],

            'functionDeclaration': ['function'],
                                                
            'procDecl': ['identifier',
                        'procedure'],

            'params': ['identifier',
                       'const',
                       'struct',
                       'int',
                       'real',
                       'boolean',
                       'string'],

            'param': ['identifier',
                       'const',
                       'struct',
                       'int',
                       'real',
                       'boolean',
                       'string'],
            
            'functionCall': ['identifier'],

            'typedefDecl': ['typedef'],

            'base': ['identifier',
                    'struct',
                    'int',
                    'real',
                    'boolean',
                    'string'],

            'structDecl': ['struct'],
                        
            'extends': ['extends'],

            'constDecl': ['const'],

            'constList': ['identifier',
                         'struct',
                         'int',
                         'real',
                         'boolean',
                         'string'],

            'const': ['identifier'],

            'delimiterConst': [',',
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
                     'false'],

            'var': ['var'],

            'variablesList': ['identifier',
                              'struct'
                              'int',
                              'real',
                              'boolean',
                              'string'],     
                              
            'variable': ['identifier'],

            'aux': [',',
                   ';',
                   '='
                   '['],

            'delimiterVar':[',',
                            ';'],               

            'index': ['decLiteral',
                     'octLiteral',
                     'identifier'],

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
                                    'stringLiteral'],

            'assignmentMatrix': ['='],

            'assignmentMatrixAux': ['='],

            'dimensionMatrix' : [ ','],

            'valueAssignedMatrix': ['decLiteral',
                                    'octLiteral',
                                    'hexLiteral',
                                    'floatLiteral',
                                    'true',
                                    'false',
                                    'stringLiteral'],
            
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
                                    'stringLiteral',
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
                     'identifier',
                     'while',
                     'read',
                     'print',
                     'return',
                     '-',
                     'stringLiteral',
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
                     'identifier',
                     'while',
                     'read',
                     'print',
                     'return',
                     '-',
                     'stringLiteral',
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
                            'identifier',
                            'while',
                            'read',
                            'print',
                            'return',
                            '-',
                            'stringLiteral',
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
                            'identifier',
                            'while',
                            'read',
                            'print',
                            'return',
                            '-',
                            'stringLiteral',
                            'if'], 

            'conditionalOperator': ['&&',
                                   '||'],

        
            'logicalDaned': ['!'],

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
                                      'stringLiteral',
                                      'identifier'],     

            'logicalExpression':    ['decLiteral',
                                      'octLiteral',
                                      'hexLiteral',
                                      'floatLiteral',
                                      'true',
                                      'false',
                                      'global.',
                                      'local.',
                                      '-',
                                      'stringLiteral',
                                      'identifier'],  

            'relacionalExpression':  ['decLiteral',
                                      'octLiteral',
                                      'hexLiteral',
                                      'floatLiteral',
                                      'true',
                                      'false',
                                      'global.',
                                      'local.',
                                      '-',
                                      'stringLiteral',
                                      'identifier'],   

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
                    'identifier',
                    'stringLiteral',
                    'true',
                    'false',
                    '-'],     

            'expressionValue':['decLiteral',
                    'octLiteral',
                    'hexLiteral',
                    'floatLiteral',
                    '(',
                    'identifier',
                    'stringLiteral',
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
