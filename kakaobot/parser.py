import re

def ser(string):
    parser = string.replace('(부대햄-돈육:국내산/돈육:국내산,우육:호주산,스모크햄,후랑크햄-계육,돈육:국내산,김치-배추,고춧가루:중국산,두부-콩:외국산,사골육수-쇠고기:호주산)', ' ')
    parser = parser.replace('(부대햄-돈육:국내산/돈육:국내산,우육:호주산)',' ')
    parser = re.sub('[★]', '', parser)
    return parser

def dong(string):
    parser = string.replace('부대햄-돈육:국내산/돈육:국내산,우육:호주산 스모크햄,후랑크햄-계육,돈육:국내산 김치-배추,고춧가루:중국산 사골육수-쇠고기:호주산 두부-콩:외국산','')
    parser = parser.replace('부대햄-돈육:국내산/돈육:국내산,우육:호주산 스모크햄,후랑크햄-계육,돈육:국내산김치-배추,고춧가루:중국산,사골육수-쇠고기:호주산두부-콩:외국산', '')
    parser = re.sub('[★]', '', parser)
    return parser

def kik(string):
    parser = string.replace('(돈,계육:국내산)', ' ')
    parser = parser.replace('(배추:중국산,고추분:중국산)', ' ')
    parser = re.sub('[★]', '', parser)
    return parser