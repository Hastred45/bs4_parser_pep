from pathlib import Path

BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
MAIN_DOC_URL = 'https://docs.python.org/3/'
MAIN_PEP_URL = 'https://peps.python.org/'
EXPECTED_STATUS = {
        'A': ('Active', 'Accepted'),
        'D': ('Deferred'),
        'F': ('Final'),
        'P': ('Provisional'),
        'R': ('Rejected'),
        'S': ('Superseded'),
        'W': ('Withdrawn'),
        '': ('Draft', 'Active'),
    }
RESULTS_WHATS_NEW = [('Ссылка на статью', 'Заголовок', 'Редактор, Автор')]
RESULTS_LATEST = [('Ссылка на документацию', 'Версия', 'Статус')]
