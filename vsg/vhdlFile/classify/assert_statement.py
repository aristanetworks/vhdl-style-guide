
import re


def assert_statement(self, dVars, lTokens, lObjects, oLine):
    '''
    [ label : ] assert condition
      [ report expression ]
      [ severity expression ] ;
    '''

    if re.match('^\s*assert', oLine.line, re.IGNORECASE):
        oLine.isAssertKeyword = True
        oLine.insideAssert = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']
        dVars['iCurrentIndentLevel'] += 1
    if oLine.insideAssert and not oLine.isAssertKeyword:
        oLine.indentLevel = dVars['iCurrentIndentLevel']
    if oLine.insideAssert and ';' in oLine.line:
        oLine.isAssertEnd = True
        dVars['iCurrentIndentLevel'] -= 1
