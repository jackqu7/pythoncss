class Style(object):
    @classmethod
    def get_target(cls):
        meta = getattr(cls, 'Meta', None)
        if meta:
            return meta.target
        else:
            return cls.__name__.lower()
    pass
    
class Mixin():
    pass
    
def _parse_style(style):
    print '%s {' % style.get_target()
    for attribute in dir(style):
        if not attribute.startswith('__') and \
            attribute not in ['Private', 'Meta']:
            value = getattr(style, attribute)
            if not callable(value):
                if type(value) == property:
                    value = value.__get__(style())
                if type(value) == int:
                    value = '%ipx' % value
                name = attribute.replace('_', '-')
                print '\t%s: %s;' % (name, value)
    print '}'    
    
def run():
    import main
    styles = Style.__subclasses__()
    for style in styles:
        _parse_style(style)
