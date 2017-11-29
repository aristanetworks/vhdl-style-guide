
from vsg.rules.instantiation import instantiation_rule
from vsg import fix
from vsg import check


class rule_011(instantiation_rule):
    '''
    Instantiation rule 011 checks the port name is uppercase.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '011'
        self.solution = 'Uppercase port name.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortAssignment and not oLine.isInstantiationPortKeyword:
                check.is_uppercase(self, oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sPortName = oLine.line.split('=>')[0].split('(')[0].lstrip().rstrip()
            fix.upper_case(self, oLine, sPortName)
