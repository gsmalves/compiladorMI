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

                       
            'prefixGlobalLocal':['decLiteral',
                                'octLiteral',
                                'hexLiteral',
                                'floatLiteral',
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

            'varDecl' : ['decLiteral',
                        'octLiteral',
                        'hexLiteral',
                        'floatLiteral',
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
                    'typedef'],               

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
            
            'while': ['decLiteral',
                      'octLiteral',
                      'hexLiteral',
                      'floatLiteral',
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

            'whileProcedure' : ['decLiteral',
                                'octLiteral',
                                'hexLiteral',
                                'floatLiteral',
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

            'if': ['decLiteral',
                    'octLiteral',
                    'hexLiteral',
                    'floatLiteral',
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

            'then': ['decLiteral',
                      'octLiteral',
                      'hexLiteral',
                      'floatLiteral',
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

            'else': ['decLiteral',
                      'octLiteral',
                      'hexLiteral',
                      'floatLiteral',
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

            'ifProcedure': ['decLiteral',
                            'octLiteral',
                            'hexLiteral',
                            'floatLiteral',
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

            'thenProcedure': ['decLiteral',
                            'octLiteral',
                            'hexLiteral',
                            'floatLiteral',
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

            'elseProcedure': ['decLiteral',
                            'octLiteral',
                            'hexLiteral',
                            'floatLiteral',
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

            'read': ['decLiteral',
                      'octLiteral',
                      'hexLiteral',
                      'floatLiteral',
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

            'print': ['decLiteral',
                      'octLiteral',
                      'hexLiteral',
                      'floatLiteral',
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

            'bodyItem': ['decLiteral',
                        'octLiteral',
                        'hexLiteral',
                        'floatLiteral',
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

            'returnStetement':['decLiteral',
                                'octLiteral',
                                'hexLiteral',
                                'floatLiteral',
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

            'bodyItemProcedure':['decLiteral',
                                'octLiteral',
                                'hexLiteral',
                                'floatLiteral',
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

            'conditionalOperator': ['decLiteral',
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


            'assign':['decLiteral',
                    'octLiteral',
                    'hexLiteral',
                    'floatLiteral',
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
