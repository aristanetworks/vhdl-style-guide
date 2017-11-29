
from vsg.rules.instantiation import instantiation_rule
from vsg import fix
from vsg import check

import re


class rule_009(instantiation_rule):
    '''
    Instantiation rule 009 checks the entity name is uppercase in the instantiation declaration line.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Change entity name to all uppercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration:
                if re.match('^\s*\w+\s+:\s+\w+', oLine.line):
                    check.is_uppercase(self, oLine.line.split()[2], iLineNumber)
                elif re.match('^\s*\w+:\w+', oLine.line):
                    lLine = oLine.line.split(':')[1].split()
                    check.is_uppercase(self, lLine[0], iLineNumber)
                else:
                    check.is_uppercase(self, oLine.line.split()[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line.split(':')[1].split()[0]
            fix.upper_case(self, oFile.lines[iLineNumber], sLine)
