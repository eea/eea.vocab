# Geographical coverage vocabulary
COUNTRIES_DICTIONARY_ID = 'european_countries'
def getCountriesDictionary():
    res = {}

    #european countries
    data = getCountries()
    for key in data.keys():
        res[(key.lower(), data[key])] = {}

    # country groups
    res[('eu15', 'EU15')] = EU15
    res[('eu25', 'EU25')] = EU25
    res[('eu27', 'EU27')] = EU27
    return res

EU15 = {('at', 'at'): {},
        ('be', 'be'): {},
        ('de', 'de'): {},
        ('dk', 'dk'): {},
        ('es', 'es'): {},
        ('fi', 'fi'): {},
        ('fr', 'fr'): {},
        ('gb', 'gb'): {},
        ('gr', 'gr'): {},
        ('ie', 'ie'): {},
        ('it', 'it'): {},
        ('lu', 'lu'): {},
        ('nl', 'nl'): {},
        ('pt', 'pt'): {},
        ('se', 'se'): {},
}
EU25 = {('at', 'at'): {},
        ('be', 'be'): {},
        ('cy', 'cy'): {},
        ('cz', 'cz'): {},
        ('de', 'de'): {},
        ('dk', 'dk'): {},
        ('ee', 'ee'): {},
        ('es', 'es'): {},
        ('fi', 'fi'): {},
        ('fr', 'fr'): {},
        ('gb', 'gb'): {},
        ('gr', 'gr'): {},
        ('hu', 'hu'): {},
        ('ie', 'ie'): {},
        ('it', 'it'): {},
        ('lt', 'lt'): {},
        ('lu', 'lu'): {},
        ('lv', 'lv'): {},
        ('mt', 'mt'): {},
        ('nl', 'nl'): {},
        ('pl', 'pl'): {},
        ('pt', 'pt'): {},
        ('se', 'se'): {},
        ('si', 'si'): {},
        ('sk', 'sk'): {},
}
EU27 = {('at', 'at'): {},
        ('be', 'be'): {},
        ('bg', 'bg'): {},
        ('cy', 'cy'): {},
        ('cz', 'cz'): {},
        ('de', 'de'): {},
        ('dk', 'dk'): {},
        ('ee', 'ee'): {},
        ('es', 'es'): {},
        ('fi', 'fi'): {},
        ('fr', 'fr'): {},
        ('gb', 'gb'): {},
        ('gr', 'gr'): {},
        ('hu', 'hu'): {},
        ('ie', 'ie'): {},
        ('it', 'it'): {},
        ('lt', 'lt'): {},
        ('lu', 'lu'): {},
        ('lv', 'lv'): {},
        ('mt', 'mt'): {},
        ('nl', 'nl'): {},
        ('pl', 'pl'): {},
        ('pt', 'pt'): {},
        ('ro', 'ro'): {},
        ('se', 'se'): {},
        ('si', 'si'): {},
        ('sk', 'sk'): {},
}

def getCountries():
    """ return European countries """
    # In case we need all countries:
    #from Products.PloneLanguageTool.availablelanguages import getCountries
    #return getCountries()

    return {
        'ad':'ad',
        'al':'al',
        'am':'am',
        'at':'at',
        'az':'az',
        'ba':'ba',
        'be':'be',
        'bg':'bg',
        'by':'by',
        'ch':'ch',
        'cs':'cs',
        'cy':'cy',
        'cz':'cz',
        'de':'de',
        'dk':'dk',
        'ee':'ee',
        'es':'es',
        'fi':'fi',
        'fo':'fo',
        'fr':'fr',
        'gb':'gb',
        'ge':'ge',
        'gr':'gr',
        'hr':'hr',
        'hu':'hu',
        'ie':'ie',
        'il':'il',
        'is':'is',
        'it':'it',
        'kz':'kz',
        'li':'li',
        'lt':'lt',
        'lu':'lu',
        'lv':'lv',
        'mc':'mc',
        'md':'md',
        'mk':'mk',
        'mt':'mt',
        'nl':'nl',
        'no':'no',
        'pl':'pl',
        'pt':'pt',
        'ro':'ro',
        'ru':'ru',
        'se':'se',
        'si':'si',
        'sk':'sk',
        'sm':'sm',
        'tr':'tr',
        'ua':'ua',
        }

