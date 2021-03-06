class Follows:    #ANCHOR rever a parte de number
    #ANCHOR verificar se global e local englobam o delimitador
    def __init__(self):
        self.follows = {
            'number': ['$',
                       ')',
                       '}',
                       ',',
                       ';',
                       '&&',
                       '||',
                       '>',
                       '<',
                       '<=',
                       '>=',
                       '==',
                       '!=',
                       '+',
                       '-',
                       '/',
                       '*',
                       '┤'],

                       
            'prefixGlobalLocal':['NRO',
                                '(',
                                'IDE',
                                'CAD',
                                'true',
                                'false',
                                '-'],    

            'globalDecl': ['IDE',
                        'start'
                        'procedure',
                        'function',
                        'struct',
                        'typedef'],

            'decls': ['start'],

            'decl': ['IDE',
                    'start'
                    'procedure',
                    'function',
                    'struct',
                    'typedef'],

            'formalParameterList' : [')'],

            'formalParameterListRead' : [')'
                                    ','],

            'functionDeclaration' :['IDE',
                                    'start'
                                    'procedure',
                                    'function',
                                    'struct',
                                    'typedef'],

            'procDecl' :['IDE',
                        'start'
                        'procedure',
                        'function',
                        'struct',
                        'typedef'],

            'params' : [')'],

            'param' : [')', 
                      ','],

            'functionCall' : [')',
                            ',',
                            ';',
                            '>',
                            '<',
                            '<=',
                            '>=',
                            '==',
                            '!=',
                            '+',
                            '-',
                            '/',
                            '*'],

            'typedefDecl': ['IDE',
                            'start'
                            'procedure',
                            'function',
                            'struct',
                            'typedef'],

            'base' : ['IDE'],

            'structDecl' : ['IDE',
                            'start'
                            'procedure',
                            'function',
                            'struct',
                            'typedef'],

            'extends' : ['{'],

            'constDecl' :  ['IDE',
                            'start',
                            'real',
                            'procedure',
                            'function',
                            'struct',
                            'typedef',
                            'var'],

            'constList': ['}'],

            'const' : ['}',
                      'IDE',
                      'struct',
                      'int',
                      'real',
                      'boolean',
                      'string'],               

            'delimiterConst' :  ['IDE',
                                'start'
                                'procedure',
                                'function',
                                'struct',
                                'typedef'],

            'type' : ['IDE'],

            'value' : ['}',
                      ',',
                      ';'],

            'varDecl' : ['NRO',
                        'global.',
                        'local.',
                        'start',
                        '(',
                        '}',
                        'IDE',
                        'function',
                        'procedure',
                        'typedef',
                        'struct',
                        'CAD',
                        'var',
                        'while',
                        'true',
                        'false',
                        'if',
                        'read',
                        'print',
                        'return',
                        '-'],

            'variableList' : ['}'],

            'variable' :['IDE',
                        'start'
                        'procedure',
                        'function',
                        'struct',
                        'typedef'],  

            'aux' : ['IDE',
                    'start'
                    'procedure',
                    'function',
                    'struct',
                    'typedef',
                     'CAD',
                     'true',
                     'false',
                     'NRO'
                     '}'],               

            'index' : [']'],

            'vector': [',',
                      ';',
                      '='],

            'matrix' : [',',
                      ';',
                      '='],

            'assignmentVector': [',',
                                ';'],

            'assignmentVectorAux': [',',
                                    ';'],

            'valueAssignedVector': ['}'],

            'assignmentMatrix': [',',
                                ';'],

            'assignmentMatrixAux': [',',
                                   ';'],

            'dimensionMatrix' : [',',
                                 ';'],

            'valueAssignedMatrix': ['}'],
            
            'while': ['NRO',
                      'global.',
                      'local.',
                      '(',
                      '}',
                      'IDE',
                      'CAD',
                      'var',
                      'while',
                      'true',
                      'false',
                      'if',
                      'read',
                      'print',
                      'return',
                      '-'],

            'whileProcedure' : ['NRO',
                                'global.',
                                'local.',
                                '(',
                                '}',
                                'IDE',
                                'CAD',
                                'var',
                                'while',
                                'true',
                                'false',
                                'if',
                                'read',
                                'print',
                                '-'],

            'boolenaLiteral': [')',
                             ',',
                             ';',
                             '>',
                             '<',
                             '<=',
                             '>=',
                             '==',
                             '!=',
                             '+',
                             '-',
                             '/',
                             '*',
                             '}',
                             '&&',
                             '||'],


            'conditionalExpression':[')'],

            'if': ['NRO',
                    'global.',
                    'local.',
                    '(',
                    '}',
                    'IDE',
                    'CAD',
                    'var',
                    'while',
                    'true',
                    'false',
                    'if',
                    'read',
                    'print',
                    'return',
                    '-'],

            'then': ['NRO',
                      'global.',
                      'local.',
                      '(',
                      '}',
                      'IDE',
                      'CAD',
                      'var',
                      'while',
                      'true',
                      'false',
                      'if',
                      'read',
                      'print',
                      'return',
                      '-'],

            'else': ['NRO',
                      'global.',
                      'local.',
                      '(',
                      '}',
                      'IDE',
                      'CAD',
                      'var',
                      'while',
                      'true',
                      'false',
                      'if',
                      'read',
                      'print',
                      'return',
                      '-'],

            'ifProcedure': ['NRO',
                            'global.',
                            'local.',
                            '(',
                            '}',
                            'IDE',
                            'CAD',
                            'var',
                            'while',
                            'true',
                            'false',
                            'if',
                            'read',
                            'print',
                            '-'],

            'thenProcedure': ['NRO',
                            'global.',
                            'local.',
                            '(',
                            '}',
                            'IDE',
                            'CAD',
                            'var',
                            'while',
                            'true',
                            'false',
                            'if',
                            'read',
                            'print',
                            '-'],

            'elseProcedure': ['NRO',
                            'global.',
                            'local.',
                            '(',
                            '}',
                            'IDE',
                            'CAD',
                            'var',
                            'while',
                            'true',
                            'false',
                            'if',
                            'read',
                            'print',
                            '-'],

            'read': ['NRO',
                      'global.',
                      'local.',
                      '(',
                      '}',
                      'IDE',
                      'CAD',
                      'var',
                      'while',
                      'true',
                      'false',
                      'if',
                      'read',
                      'print',
                      'return',
                      '-'],

            'print': ['NRO',
                      'global.',
                      'local.',
                      '(',
                      '}',
                      'IDE',
                      'CAD',
                      'var',
                      'while',
                      'true',
                      'false',
                      'if',
                      'read',
                      'print',
                      'return',
                      '-'],

            'body': ['}'],

            'bodyItem': ['NRO',
                        'global.',
                        'local.',
                        '(',
                        '}',
                        'IDE',
                        'CAD',
                        'var',
                        'while',
                        'true',
                        'false',
                        'if',
                        'read',
                        'print',
                        'return',
                        '-'],

            'returnStetement':['NRO',
                                'global.',
                                'local.',
                                '(',
                                '}',
                                'IDE',
                                'CAD',
                                'var',
                                'while',
                                'true',
                                'false',
                                'if',
                                'read',
                                'print',
                                'return',
                                '-'],

            'bodyProcedure':['}'], 

            'bodyItemProcedure':['NRO',
                                'global.',
                                'local.',
                                '(',
                                '}',
                                'IDE',
                                'CAD',
                                'var',
                                'while',
                                'true',
                                'false',
                                'if',
                                'read',
                                'print',
                                '-'], 

            'conditionalOperator': ['NRO',
                                    'global.',
                                    'local.',
                                    '(',
                                    'IDE',
                                    'CAD',
                                    'true',
                                    'false',
                                    '!',
                                    '-'],

        
            'logicalDenied': [')'],

            'logical': [')'],

            'expressionValueLogical':[')',
                                      '&&',
                                      '||'],     

            'logicalExpression':    [')'],  

            'relacionalExpression': [')',
                                    '&&',
                                    '||'],     
 
            'relational': [')',
                           '&&',
                           '||'],     


            'assign':['NRO',
                    'global.',
                    'local.',
                    '(',
                    '}',
                    'IDE',
                    'CAD',
                    'var',
                    'while',
                    'true',
                    'false',
                    'if',
                    'read',
                    'print',
                    'return',
                    '-'],                                               

            'exp': [')',
                    ',',
                    ';',
                    '&&',
                    '||',
                    '>',
                    '<',
                    '<=',
                    '>=',
                    '==',
                    '!='], 

            'addExp' : [')',
                        ',',
                        ';',
                        '&&',
                        '||',
                        '>',
                        '<',
                        '<=',
                        '>=',
                        '==',
                        '!='], 
        
            
            'term':[')',
                    ',',
                    ';',
                    '&&',
                    '||',
                    '>',
                    '<',
                    '<=',
                    '>=',
                    '==',
                    '!=',
                    '+',
                    '-'], 

            'expressionValue' : [')',
                                ',',
                                ';',
                                '&&',
                                '||',
                                '>',
                                '<',
                                '<=',
                                '>=',
                                '==',
                                '!=',
                                '+',
                                '-',
                                '*',
                                '/'],    

            'multExp': [')',
                    ',',
                    ';',
                    '&&',
                    '||',
                    '>',
                    '<',
                    '<=',
                    '>=',
                    '==',
                    '!=',
                    '+',
                    '-'], 
                         



           
        }

    def get_follows(self, production: str, lexema):
        production_follows = self.follows.get(production)

        if production_follows:
            "print(production_follows)"

            return production_follows.__contains__(lexema)
