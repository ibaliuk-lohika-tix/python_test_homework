from assertpy import assert_that, soft_assertions
import os.path


def file_func(lines_from_end: int, file_path: str = "./file_arg/file_arg"):
    """
    Function which will read specified last lines from specified f

    ile, and return them in correct order.
    :param lines_from_end: Amount of line you needed.
    :param file_path: Path to file we will use.
    :return:
    """
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as file:
                return ''.join(line for line in file.readlines()[-int(lines_from_end):]) if lines_from_end else ""
        except:
            return(f"Check argument values, expected Int and Str, got {type(lines_from_end)} and {type(file_path)} "
                   f"instead. With argument values {lines_from_end} and {file_path}")
    else:
        return "File doesn't exist, please check file path."


def test_check_job():
    with soft_assertions():
        assert_that(file_func(0)).is_equal_to("")
        assert_that(file_func(5)).is_equal_to(''.join("6\n7\n8\n9\n0"))
        assert_that(file_func(-5)).is_equal_to(''.join("6\n7\n8\n9\n0"))
        assert_that(file_func('A')).is_equal_to("Check argument values, expected Int and Str, got <class 'str'> and "
                                                "<class 'str'> instead. With argument values A and ./file_arg/file_arg")
        assert_that(file_func(None)).is_equal_to("")
        assert_that(file_func(5, "./file_arg/file_arg1111")).is_equal_to("File doesn't exist, please check file path.")
        assert_that(file_func(5.0, "./file_arg/file_arg")).is_equal_to(''.join("6\n7\n8\n9\n0"))
        assert_that(file_func(5, "")).is_equal_to("File doesn't exist, please check file path.")
        assert_that(file_func(91111)).is_equal_to(''.join("6\n7\n8\n9\n0"))
