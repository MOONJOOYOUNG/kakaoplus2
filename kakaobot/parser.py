import re

def ser(string):
    parser = string.replace('아침 :', '◎아침◎\n')
    parser = parser.replace('점심 :', '◎점심◎\n')
    parser = parser.replace('저녁 :', '◎저녁◎\n')

    parser = parser.replace('B-', '\nB-')

    parser = parser.replace('	 				', '')
    parser = parser.replace('       ', '')
    parser = parser.replace('      ', '')
    parser = parser.replace('     ', '')
    parser = parser.replace('    ', '')
    parser = parser.replace('   ', '')
    parser = parser.replace('  ', '')

    parser = parser.replace(',', '')
    parser = parser.replace(', ', ' ')
    parser = re.sub('[★]', '', parser)
    return parser

def dong(string):
    parser = string.replace('아침 :', '◎아침◎\n')
    parser = parser.replace('점심 :', '◎점심◎\n')
    parser = parser.replace('저녁 :', '◎저녁◎\n')
    parser = parser.replace('B-', '\nB-')

    parser = parser.replace('	 				', '')
    parser = parser.replace('       ', '')
    parser = parser.replace('      ', '')
    parser = parser.replace('     ', '')
    parser = parser.replace('    ', '')
    parser = parser.replace('   ', '')
    parser = parser.replace('  ', '')

    parser = parser.replace(',', '')
    parser = parser.replace(', ', ' ')
    parser = re.sub('[★]', '', parser)
    return parser

def kik(string):
    parser = string.replace('아침 :', '◎아침◎\n')
    parser = parser.replace('점심 :', '◎점심◎\n')
    parser = parser.replace('저녁 :', '◎저녁◎\n')
    parser = parser.replace('B-', '\nB-')

    parser = parser.replace('	 				', '')
    parser = parser.replace('       ', '')
    parser = parser.replace('      ', '')
    parser = parser.replace('     ', '')
    parser = parser.replace('    ', '')
    parser = parser.replace('   ', '')
    parser = parser.replace('  ', '')

    parser = parser.replace(',', '')
    parser = parser.replace(', ', ' ')
    parser = re.sub('[★]', '', parser)
    return parser