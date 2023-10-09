from typing import Union, List, Dict


class Formatter:
    @staticmethod
    def format_string(arg: Union[str, List[str], Dict]):
        if isinstance(arg, list):
            for item in arg:
                Formatter.format_string(item)

        elif isinstance(arg, dict):
            for item in arg.values():
                if isinstance(item, str):
                    Formatter.format_string(item)
        else:
            arg.lower()
