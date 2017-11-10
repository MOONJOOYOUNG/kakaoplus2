import re

def ser(string):
    parser = string.replace('(부대햄-돈육:국내산/돈육:국내산,우육:호주산)',' ')
    parser = string.replace('(스모크햄,후랑크햄-계육,돈육:국내산,김치-배추,고춧가루:중국산,두부-콩:외국산)', ' ')
    parser = parser.replace('(카레용돈육:덴마크산,오징어:페루산)', ' ')
    parser = parser.replace('(카레용돈육:덴마크산,탕수육-돈육:국내산)', ' ')
    parser = parser.replace('(부대햄-돈육:국내산/돈육:국내산,우육:호주산)', ' ')
    parser = parser.replace('(돈육:국내산,김치-배추,고춧가루:중국산)', ' ')
    parser = parser.replace('(계육:국내산,김치-배추,고춧가루:중국산)', ' ')
    parser = parser.replace('(우육:호주산,사골육수-쇠고기:호주산)', ' ')
    parser = parser.replace('(카레용돈육:덴마크산,오징어:페루산) ', ' ')
    parser = parser.replace('(돈육:국내산,사골육수-쇠고기:호주산)', ' ')

    parser = parser.replace('(배추,고춧가루:중국산)', ' ')
    parser = parser.replace('(돈육:덴마크산)', ' ')
    parser = parser.replace('(돈육:국내산)', ' ')
    parser = parser.replace('(계육:국내산)', ' ')
    parser = parser.replace('(오징어:페루산)', ' ')
    parser = parser.replace('(잡채용돈육:국내산)', ' ')
    parser = parser.replace('(카레용돈육:덴마크산)', ' ')
    parser = parser.replace('(흑미:국내산)', ' ')
    parser = parser.replace('(두부-콩:외국산)', ' ')

    parser = parser.replace('"', ' ')
    parser = parser.replace('/', ' ')
    parser = re.sub('[★]', '', parser)
    return parser

def dong(string):
    parser = string.replace('부대햄-돈육:국내산/돈육:국내산,우육:호주산스모크햄,후랑크햄-계육,돈육:국내산김치-배추,고춧가루:중국산,사골육수-쇠고기:호주산두부-콩:외국산', '')
    parser = parser.replace('부대햄-돈육:국내산/돈육:국내산,우육:호주산', '')

    parser = parser.replace('김치-배추,고춧가루:중국산', '')
    parser = parser.replace('돈육:국내산,우육:호주산', '')
    parser = parser.replace('사골육수-쇠고기:호주산 ', '')
    parser = parser.replace('스모크햄-계육,돈육:국내산', '')
    parser = parser.replace('배추,고춧가루:중국산', '')
    parser = parser.replace('배추:국내산,고춧가루:중국산', '')
    parser = parser.replace('-배추,고춧가루:중국산', '')
    parser = parser.replace('계육:국내산, 브라질산', '')
    parser = parser.replace('돈육,계육:국내산', '')
    parser = parser.replace('-콩:외국산', '')
    parser = parser.replace('돈육:국내산', '')
    parser = parser.replace('돈육:덴마크', '')
    parser = parser.replace('계육:국내산,브라질산', '')
    parser = parser.replace('계육:국내산', '')
    parser = parser.replace('우육:호주산', '')
    parser = parser.replace('오징어:페루산 ', '')
    parser = parser.replace('흑미:국내산', '')
    parser = parser.replace('사골육수-', '')
    parser = parser.replace('쇠고기:호주산', '')


    parser = parser.replace('"', ' ')
    parser = parser.replace('/', ' ')
    parser = re.sub('[★]', '', parser)
    return parser

def kik(string):
    parser = string.replace('(돈,계육:국내산)', ' ')

    parser = parser.replace('(배추:국내산,고추분:중국산)', ' ')
    parser = parser.replace('(배추:국내산,고추분:중국산', ' ')
    parser = parser.replace('(돈,계육:국내산)(우육:호주산)', ' ')
    parser = parser.replace('(계,돈육:국내산)', ' ')
    parser = parser.replace('(오리:국내산)', ' ')
    parser = parser.replace('(계육:국내산)', ' ')
    parser = parser.replace('(돈육:국내산)', ' ')
    parser = parser.replace('(돈육:덴마크산)', ' ')
    parser = parser.replace('(돈,계육:국내산)', ' ')
    parser = parser.replace('(우육:호주산)', ' ')
    parser = parser.replace('(우육,육수:호주산)', ' ')
    parser = parser.replace('(우민찌;호주산)', ' ')
    parser = parser.replace('(오징어:페루산)', ' ')
    parser = parser.replace('(오징어:국내산)', ' ')

    parser = parser.replace('(대구:네덜란드산)', ' ')
    parser = parser.replace('(가자미:미국산)', ' ')

    parser = parser.replace('(대두:외국산)', ' ')

    parser = parser.replace('[DIY코너]', '\n[DIY코너]')
    parser = parser.replace('[일품 및 양식]', '\n[일품]')
    parser = parser.replace('[누들]', '\n[누들]')

    parser = re.sub('[★]', '', parser)
    parser = parser.replace('"', '')
    parser = parser.replace('/', '')

    return parser