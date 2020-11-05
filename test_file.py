import pytest
from assertpy import assert_that, soft_assertions
import os.path


def file_func(lines_from_end: int, file_path: str):
    """
    Function which will read specified last lines from specified file, and return them in correct order.
    :param lines_from_end: Amount of line you needed.
    :param file_path: Path to file we will use.
    :return:
    """
    if isinstance(lines_from_end, (int, float)) and os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            return {"message":
                    ''.join(line for line in file.readlines()[-int(lines_from_end):]) if lines_from_end > 0 else ""}
    else:
        return ({"message": "Check file path or lines_from_end value",
                 "causedBy": "expected Int and Str, got {type(lines_from_end)} and "
                 f"{type(file_path)} instead. With argument values lines amount:{lines_from_end} and "
                 f"path to file:{file_path}"})


@pytest.mark.parametrize("lines_from_end, file_path, expected", [
        (0, "./file_arg/file_arg", ""),
        (10, "./file_arg/file_arg", "12\n23\n34\n45\n56\n67\n78\n89\n90\n01"),
        (5, "./file_arg/file_arg", "".join("67\n78\n89\n90\n01")),
        (-5, "./file_arg/file_arg", ""),
        ('A', "./file_arg/file_arg", "Check file path or lines_from_end value"),
        (None, "./file_arg/file_arg", "Check file path or lines_from_end value"),
        (5, "./file_arg/file_arg1111", "Check file path or lines_from_end value"),
        (5.0, "./file_arg/file_arg", "".join("67\n78\n89\n90\n01")),
        (5, "", "Check file path or lines_from_end value"),
        (91111, "./file_arg/file_arg", ''.join("12\n23\n34\n45\n56\n67\n78\n89\n90\n01")),
        (None, None, "Check file path or lines_from_end value"),
        ("", "", "Check file path or lines_from_end value")
        ])
def test_check_job(lines_from_end, file_path, expected):
    assert_that(file_func(lines_from_end, file_path).get("message")).is_equal_to(expected)


def test_check_job_second_solution():
    error_message = "Check file path or lines_from_end value"
    with soft_assertions():
        assert_that(file_func(0, "./file_arg/file_arg").get("message")).is_equal_to("")
        assert_that(file_func(10, "./file_arg/file_arg").get("message")).is_equal_to(
            "".join("12\n23\n34\n45\n56\n67\n78\n89\n90\n01"))
        assert_that(file_func(5, "./file_arg/file_arg").get("message")).is_equal_to("".join("67\n78\n89\n90\n01"))
        assert_that(file_func(-5, "./file_arg/file_arg").get("message")).is_equal_to("")
        assert_that(file_func('A', "./file_arg/file_arg").get("message")).is_equal_to(error_message)
        assert_that(file_func(None, "./file_arg/file_arg").get("message")).is_equal_to(error_message)
        assert_that(file_func(5, "./file_arg/file_arg1111").get("message")).is_equal_to(error_message)
        assert_that(file_func(5.0, "./file_arg/file_arg").get("message")).is_equal_to("".join("67\n78\n89\n90\n01"))
        assert_that(file_func(5, "").get("message")).is_equal_to(error_message)
        assert_that(file_func(91111, "./file_arg/file_arg").get("message")).is_equal_to(
            "".join("12\n23\n34\n45\n56\n67\n78\n89\n90\n01"))
        assert_that(file_func("", "").get("message")).is_equal_to(error_message)
        assert_that(file_func(None, None).get("message")).is_equal_to(error_message)


# TODO Remove if print aren't mandatory condition
def if_print_are_mandatory_condition(lines_from_end: int, file_path: str):
    """
    Function which will read specified last lines from specified file, and return them in correct order.
    Through the print method
    :param lines_from_end: Amount of line you needed.
    :param file_path: Path to file we will use.
    :return:
    """
    error_message = "Check file path or lines_from_end value"
    file_result_path = "./file_arg/result"
    if isinstance(lines_from_end, (int, float)) and os.path.isfile(file_path):
        with open(file_path, "r") as file:
            lines = ''.join(line for line in file.readlines()[-int(lines_from_end):]) if lines_from_end > 0 else ""
    else:
        lines = error_message
    with open(f"{file_result_path}", "w+") as file_result:
        print(lines, file=file_result)
        return lines


# TODO Remove if print aren't mandatory condition
@pytest.mark.parametrize("lines_from_end, file_path, expected", [
        (0, "./file_arg/file_arg", ""),
        (10, "./file_arg/file_arg", "12\n23\n34\n45\n56\n67\n78\n89\n90\n01"),
        (5, "./file_arg/file_arg", "".join("67\n78\n89\n90\n01")),
        (-5, "./file_arg/file_arg", ""),
        ('A', "./file_arg/file_arg", "Check file path or lines_from_end value"),
        (None, "./file_arg/file_arg", "Check file path or lines_from_end value"),
        (5, "./file_arg/file_arg1111", "Check file path or lines_from_end value"),
        (5.0, "./file_arg/file_arg", "".join("67\n78\n89\n90\n01")),
        (5, "", "Check file path or lines_from_end value"),
        (91111, "./file_arg/file_arg", ''.join("12\n23\n34\n45\n56\n67\n78\n89\n90\n01")),
        (None, None, "Check file path or lines_from_end value"),
        ("", "", "Check file path or lines_from_end value")
        ])
def test_check_job_through_the_print_func(lines_from_end, file_path, expected):
    with soft_assertions():
        with open("./file_arg/result", "r") as result:
            assert_that(if_print_are_mandatory_condition(lines_from_end, file_path)).is_equal_to(expected)
            assert_that(result.read().strip()).is_equal_to(expected)
