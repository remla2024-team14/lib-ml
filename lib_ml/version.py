TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Tuple, Union
    VERSION_TUPLE = Tuple[Union[int, str], ...]
else:
    VERSION_TUPLE = object

version: str
__version__: str
__version_tuple__: VERSION_TUPLE
version_tuple: VERSION_TUPLE
<<<<<<< HEAD

__version__ = version = '1.0.7'
__version_tuple__ = version_tuple = (1, 0, 7)
=======
__version__ = version = '0.1.dev1+g8ff73ac.d20240507'
__version_tuple__ = version_tuple = (0, 1, 'dev1', 'g8ff73ac.d20240507')
>>>>>>> 73c19b1c620bd999745d83f6e4a82aa7ebdd6c2c
