
from vsg.rules.instantiation import instantiation_rule
from vsg import fix

import re


class rule_006(instantiation_rule):
    '''
    Instantiation rule 006 checks the "port map" keywords are lower case.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Change "port map" keywords to lowercase.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortKeyword:
                if not re.match('^.*port\s+map', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'port')
            fix.lower_case(self, oFile.lines[iLineNumber], 'map')
