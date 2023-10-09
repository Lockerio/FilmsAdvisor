from typing import Union, List, Dict


class Validator:
    @staticmethod
    def assert_valid_string(arg: Union[str, List[str], Dict]):
        if isinstance(arg, list):
            for item in arg:
                Validator.assert_valid_string(item)

        if isinstance(arg, dict):
            for item in arg:
                if isinstance(item, str):
                    Validator.assert_valid_string(item)

        if arg and not arg.isspace():
            return
        raise Exception('Вы ввели пустую строку!')
