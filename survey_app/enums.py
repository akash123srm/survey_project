class TimeConstraint(object):
    HARD_CONSTRAINT = 'Hard'
    SOFT_CONSTRAINT = 'Soft'
    INDEPENDENT = 'Independent'

class AnswerValidity(object):
     SHORT = 'Short'
     MEDIUM = 'Medium'
     LONG = 'Long'

class AbstractEnum(object):
    HIGH = 'High'
    LOW = 'Low'

    class Meta:
        abstract = True

class GeneralityApplicability(AbstractEnum):
    MEDIUM = 'Medium'

class LocationConstraint(AbstractEnum):
    pass

class DegreeKnowledge(AbstractEnum):
    pass

class CostsParameters(object):
    FEE_BASED = 'Fee Based'
    PARTIALLY_FREE = 'Partially Free'
    FREE = 'Free'

"""class InformationProviderParameters(object):
    EXPERT = 'Expert'
    OPERATOR = 'Operator'
    LAYMAN = 'Layman'"""
