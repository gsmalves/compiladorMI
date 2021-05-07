class Firsts:
    def __init__(self):
        self.firsts = {
            'Program': ['const',
                        'procedure',
                        'function',
                        'struct',
                        'var',
                        'typedef'],

            'Decls': ['function',
                      'procedure',
                      'struct',
                      'typedef'],

            'Decl': ['function',
                     'procedure',
                     'struct',
                     'typedef'],

            'Structs': ['struct',
                        'typedef'],

            'StructBlock': ['struct',
                            'typedef'],

            'Extends': ['extends'],

            'ConstBlock': ['const'],

            'VarBlock': ['var'],

            'Type': ['string',
                     'boolean',
                     'int',
                     'struct',
                     'real'],

            'Typedef': ['typedef'],

            'VarDecls': ['string',
                         'typedef',
                         'local',
                         'boolean',
                         'int',
                         'struct',
                         'real',
                         'global',
                         'IDE'],

            'VarDecl': ['string',
                        'typedef',
                        'local',
                        'boolean',
                        'int',
                        'struct',
                        'real',
                        'global',
                        'IDE'],

            'Var':  ['IDE'],

            'VarList':  [',', '='],

            'ConstDecls': ['string',
                           'typedef',
                           'local',
                           'boolean',
                           'int',
                           'struct',
                           'real',
                           'global',
                           'IDE'],

            'ConstDecl': ['string',
                          'typedef',
                          'local',
                          'boolean',
                          'int',
                          'struct',
                          'real',
                          'global',
                          'IDE'],







            'FuncDecl': ['function'],

            'StartBlock': ['procedure'],

            'ProcDecl': ['procedure'],





        }

    def get_first(self, production: str, lexema):
        production_firsts = self.firsts.get(production)

        if production_firsts:
            "print(production_firsts)"

            return production_firsts.__contains__(lexema)
