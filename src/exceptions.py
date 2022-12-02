
class ParserFindTagException(Exception):
    '''Вызывается, когда парсер не может найти тег.'''
    pass


class BadMode(Exception):
    '''Вызывается, когда неправильно указали режим работы парсера'''
    pass
