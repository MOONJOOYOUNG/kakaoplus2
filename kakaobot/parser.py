import re

def dom_parser(string):
    parser = string.replace('아침 :', '◎아침◎\n')
    parser = parser.replace('점심 :', '◎점심◎\n')
    parser = parser.replace('저녁 :', '◎저녁◎\n')

    parser = parser.replace('(동태: 러시아산)', '')
    parser = parser.replace('(돈육.계육:국산) ', '')
    parser = parser.replace('(계육:국산)', '')
    parser = parser.replace('(돈육:국산)', '')
    parser = parser.replace('(국산육우)', '')
    parser = parser.replace('(오징어:국산)', '')
    parser = parser.replace('(수입호주산)', '')
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

def food_parser(string):
    parser = string.replace('			        ', '')
    parser = parser.replace('       ', '')
    parser = parser.replace(' 　 ', ' ')
    parser = parser.replace('    ', ' ')
    return parser

