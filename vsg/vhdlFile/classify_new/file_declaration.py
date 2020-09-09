
from vsg.token import file_declaration as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import file_open_information
from vsg.vhdlFile.classify_new import identifier_list
from vsg.vhdlFile.classify_new import subtype_indication


'''
    file_declaration ::=
        file identifier_list : subtype_indication [ file_open_information ] ;
'''


def detect(iToken, lObjects):

    if utils.is_next_token('file', iToken, lObjects):
        return classify(iToken, lObjects)    

    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required('file', token.file_keyword, iToken, lObjects)
    iCurrent = identifier_list.classify(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(':', token.colon, iCurrent, lObjects)
    sEnd = utils.find_earliest_occurance([';', ':=', 'open', 'is'], iCurrent, lObjects)
    iCurrent = utils.classify_subelement_until(sEnd, subtype_indication, iCurrent, lObjects) 
    iCurrent = file_open_information.detect(iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(';', token.semicolon, iCurrent, lObjects)
    return iCurrent 
