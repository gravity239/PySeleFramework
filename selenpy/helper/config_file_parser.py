import configparser
import os

# aspectsDefault = {'autotest.termination.seconds': 600}
aspects = {}


class dotdictify(dict):
    def __init__(self, value=None):
        if value is None:
            pass
        elif isinstance(value, dict):
            for key in value:
                self.__setitem__(key, value[key])
        else:
            raise TypeError('expected dict')

    def __setitem__(self, key, value):
        if '.' in key:
            myKey, restOfKey = key.split('.', 1)
            target = self.setdefault(myKey, dotdictify())
            if not isinstance(target, dotdictify):
                raise KeyError('cannot set "%s" in "%s" (%s)' % (restOfKey, myKey, repr(target)))
            target[restOfKey] = value
        else:
            if isinstance(value, dict) and not isinstance(value, dotdictify):
                value = dotdictify(value)
            dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        if '.' not in key:
            try:
                return dict.__getitem__(self, key)
            except:
                return None
        myKey, restOfKey = key.split('.', 1)
        target = dict.__getitem__(self, myKey)
        if not isinstance(target, dotdictify):
            raise KeyError('cannot get "%s" in "%s" (%s)' % (restOfKey, myKey, repr(target)))
        return target[restOfKey]

    def __contains__(self, key):
        if '.' not in key:
            return dict.__contains__(self, key)
        myKey, restOfKey = key.split('.', 1)
        target = dict.__getitem__(self, myKey)
        if not isinstance(target, dotdictify):
            return False
        return restOfKey in target

    def setdefault(self, key, default):
        if key not in self:
            self[key] = default
        return self[key]

    __setattr__ = __setitem__
    __getattr__ = __getitem__


def aspect(name):
    return getAspect(name)


def getAspect(name):
    try:
        return aspects[name]
    except Exception as ex:
        raise Exception('Error: '.format(ex.message))


def parseConfigFile(filename):
    '''Parse and store a standard configuration file to the aspect globals'''

    global aspects, aspectsDefault

    if not os.path.isfile(filename):
        print("configuration file does not exist: {0}".format(filename))
        '''raise'''

    # -- Set aspects to default value, merge with aspects from configuration file
    aspects = dotdictify()
    configConfig = configparser.ConfigParser()
    configConfig.read_file(open(filename))
    try:
        for k, v in configConfig.items('aspects'):
            aspects[k] = v
    except (Exception) as Er:
        if Er[2].find("\'%\' must be followed") != -1:
            raise Exception("\nERROR: Please replace all %23 to \'#\' in configuration file.\n")
        raise Exception(Er)

    return aspects
