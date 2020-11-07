import json
import os


class AppData:
    def __init__(self):
        self.app_path = os.path.abspath(os.path.dirname(__file__))
        self.profile_path = f"{self.app_path}/app_profile.json"
        with open(self.profile_path, "r") as app_profile:
            data = json.load(app_profile)
            self.file_path = data.get('file_path')
            self.error_message = data.get("error_message")
            self.result = data.get('result')

    # TODO Remove if print aren't mandatory condition
    def if_print_are_mandatory_condition(self, lines_from_end: int, file_path: str, file_result_path: str = ""):
        """
        Function which will read specified last lines from specified file, and return them in correct order.
        Through the print method
        :param lines_from_end: Amount of line you needed.
        :param file_path: Path to file we will use.
        :param file_result_path: path to file where last result will be stored
        :return:
        """
        file_result_path = file_result_path if file_result_path else self.result
        file_path = file_path if file_path else self.file_path
        if isinstance(lines_from_end, (int, float)) and os.path.isfile(f"{self.app_path}/.{file_path}"):
            with open(f"{self.app_path}/.{file_path}", "r") as file:
                lines = "".join(line for line in file.readlines()[-int(lines_from_end):]) if lines_from_end > 0 else ""
        else:
            lines = self.error_message
        with open(f"{self.app_path}/.{file_result_path}", "w+") as file_result:
            print(lines, file=file_result)
            return lines

    def file_func(self, lines_from_end: int, file_path: str):
        """
        Function which will read specified last lines from specified file, and return them in correct order.
        :param lines_from_end: Amount of line you needed.
        :param file_path: Path to file we will use.
        :return:
        """
        file_path = file_path if file_path else self.file_path
        if isinstance(lines_from_end, (int, float)) and os.path.isfile(f"{self.app_path}/.{file_path}"):
            with open(f"{self.app_path}/.{file_path}", 'r') as file:
                return {"message":
                        ''.join(line for line in file.readlines()[-int(lines_from_end):]) if lines_from_end > 0 else ""}
        else:
            return ({"message": self.error_message,
                     "causedBy": "expected Int and Str, got {type(lines_from_end)} and "
                     f"{type(file_path)} instead. With argument values lines amount:{lines_from_end} and "
                     f"path to file:{file_path}"})