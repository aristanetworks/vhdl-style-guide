
import rule
import re


class signal_rule(rule.rule):
    
    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'signal'


class rule_001(signal_rule):
    '''Signal rule 001 checks for the proper indentation at the beginning of the line.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure there are only two spaces before signal keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if not re.match('^\s\ssignal', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_002(signal_rule):
    '''Signal rule 002 checks the "signal" keyword is lowercase.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove spaces before signal keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if not re.match('^\s*signal', oLine.line):
                    self.add_violation(iLineNumber)


class rule_003(signal_rule):
    '''Signal rule 003 checks there is a single space after the "signal" keyword.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '003'
        self.solution = 'Remove all but one space after the "signal" keyword.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if not re.match('^\s*signal\s\w', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_004(signal_rule):
    '''Signal rule 004 checks the signal name is lowercase.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Change signal name to lowercase.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if not self._isLowercase(oLine.line.split()[1]):
                    self.add_violation(iLineNumber)


class rule_005(signal_rule):
    '''Signal rule 005 checks there is a single space after the colon.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure only a signal space after the colon.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if not re.match('^\s*signal\s+.*\s*:\s\w', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_006(signal_rule):
    '''Signal rule 006 checks there is at least a single space before the colon.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Add a single space before the colon.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if re.match('^\s*signal\s+.*\w:', oLine.lineLower):
                    self.add_violation(iLineNumber)


class rule_007(signal_rule):
    '''Signal rule 007 checks for default assignments in signal declarations.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '007'
        self.solution = 'Remove default assignment.'

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSignal:
                if ':=' in oLine.line:
                    self.add_violation(iLineNumber)


class rule_008(signal_rule):
    '''Signal rule 008 checks for prefixes in signal names.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '008'
        self.solution = 'Remove default assignment.'
        self.prefixes = None

    def analyze(self, oFile):
        if not self.prefixes:
            return
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isSignal:
                continue
            for sSignalName in oLine.line.split(':')[0].split():
                if sSignalName.lower() == 'signal':
                    continue
                fPrefixFound = False
                for sPrefixName in self.prefixes:
                    if sSignalName.startswith(sPrefixName):
                        fPrefixFound = True
                        break
                if not fPrefixFound:
                    self.add_violation(iLineNumber)


class rule_009(signal_rule):
    '''Signal rule 009 checks the colons are in the same column for all signals.'''

    def __init__(self):
        signal_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Align colon with right most colon.'

    def analyze(self, oFile):
        iMaximumColumn = 0
        # Search for the largest column that contains the first colon
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isSignal:
                continue
            iCurrentColumn = oLine.line.find(':')
            if iMaximumColumn < iCurrentColumn:
                iMaximumColumn = iCurrentColumn
        self.solution = 'Align colon to column ' + str(iMaximumColumn + 1) + '.'
        # Compare each signals colon column to the largest found
        for iLineNumber, oLine in enumerate(oFile.lines):
            if not oLine.isSignal:
                continue
            iCurrentColumn = oLine.line.find(':')
            if not iMaximumColumn == oLine.line.find(':'):
                self.add_violation(iLineNumber)
