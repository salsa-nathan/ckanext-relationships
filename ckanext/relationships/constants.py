# TODO: Needs to load the vocabulary service for 'nature of relationship' and parse it into forward/reverse relationship types somehow before overriding the PackageRelationship.types variable
# Implement after this story has completed https://it-partners.atlassian.net/browse/DDCI-40
RELATIONSHIP_TYPES = [
    (u'unspecified relationship', u'unspecified relationship'),
    (u'isPartOf', u'hasPart'),
    (u'isFormatOf', u'hasFormat'),
    (u'isVersionOf', u'hasVersion'),
    (u'replaces', u'isReplacedBy'),
    (u'references', u'isReferencedBy'),
    (u'requires', u'isRequiredBy'),
    (u'wasDerivedFrom', ''),
    (u'wasInfluencedBy', ''),
    (u'wasQuotedFrom', ''),
    (u'wasRevisionOf', ''),
    (u'hadPrimarySource', ''),
    (u'alternateOf', ''),
    (u'specialisationOf', ''),
    (u'conformsTo', ''),
]
