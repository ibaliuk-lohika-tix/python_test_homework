import pytest
from assertpy import assert_that, soft_assertions

from app.app import AppData
from facade import facade


@pytest.mark.parametrize("lines_from_end, file_path, expected", [
        (0, facade.context.profile.file_path, ""),
        (1, facade.context.profile.file_path, "01"),
        (10, facade.context.profile.file_path, "12\n23\n34\n45\n56\n67\n78\n89\n90\n01"),
        (5, facade.context.profile.file_path, "".join("67\n78\n89\n90\n01")),
        (-5, facade.context.profile.file_path, ""),
        ('A', facade.context.profile.file_path, facade.context.profile.error_message),
        (None, facade.context.profile.file_path, facade.context.profile.error_message),
        (5, "./file_arg/file_arg1111", facade.context.profile.error_message),
        (5.0, facade.context.profile.file_path, "".join("67\n78\n89\n90\n01")),
        (5, "", "".join("67\n78\n89\n90\n01")),
        (91111, facade.context.profile.file_path, "".join("12\n23\n34\n45\n56\n67\n78\n89\n90\n01")),
        (None, None, facade.context.profile.error_message),
        ("", "", facade.context.profile.error_message)
        ])
def test_check_job(lines_from_end, file_path, expected):
    assert_that(AppData().file_func(lines_from_end, file_path).get("message")).is_equal_to(expected)


def test_check_job_second_solution():
    error_message = facade.context.profile.error_message
    with soft_assertions():
        assert_that(AppData().file_func(0, facade.context.profile.file_path).get("message")).is_equal_to("")
        assert_that(AppData().file_func(1, facade.context.profile.file_path).get("message")).is_equal_to("01")
        assert_that(AppData().file_func(10, facade.context.profile.file_path).get("message")).is_equal_to(
            "".join("12\n23\n34\n45\n56\n67\n78\n89\n90\n01"))
        assert_that(AppData().file_func(5, facade.context.profile.file_path).get("message")).is_equal_to(
            "".join("67\n78\n89\n90\n01"))
        assert_that(AppData().file_func(-5, facade.context.profile.file_path).get("message")).is_equal_to("")
        assert_that(AppData().file_func('A', facade.context.profile.file_path).get("message")).is_equal_to(
            error_message)
        assert_that(AppData().file_func(None, facade.context.profile.file_path).get("message")).is_equal_to(
            error_message)
        assert_that(AppData().file_func(5, "./file_arg/file_arg1111").get("message")).is_equal_to(error_message)
        assert_that(AppData().file_func(5.0, facade.context.profile.file_path).get("message")).is_equal_to(
            "".join("67\n78\n89\n90\n01"))
        assert_that(AppData().file_func(5, "").get("message")).is_equal_to("".join("67\n78\n89\n90\n01"))
        assert_that(AppData().file_func(91111, facade.context.profile.file_path).get("message")).is_equal_to(
            "".join("12\n23\n34\n45\n56\n67\n78\n89\n90\n01"))
        assert_that(AppData().file_func("", "").get("message")).is_equal_to(error_message)
        assert_that(AppData().file_func(None, None).get("message")).is_equal_to(error_message)


# TODO Remove if print aren't mandatory condition
@pytest.mark.parametrize("lines_from_end, file_path, expected, result", [
        (0, facade.context.profile.file_path, "", facade.context.profile.result),
        (1, facade.context.profile.file_path, "01", facade.context.profile.result),
        (10, facade.context.profile.file_path, "12\n23\n34\n45\n56\n67\n78\n89\n90\n01", facade.context.profile.result),
        (5, facade.context.profile.file_path, "".join("67\n78\n89\n90\n01"), facade.context.profile.result),
        (-5, facade.context.profile.file_path, "", facade.context.profile.result),
        ('A', facade.context.profile.file_path, facade.context.profile.error_message, facade.context.profile.result),
        (None, facade.context.profile.file_path, facade.context.profile.error_message, facade.context.profile.result),
        (5, "./file_arg/file_arg1111", facade.context.profile.error_message, facade.context.profile.result),
        (5.0, facade.context.profile.file_path, "".join("67\n78\n89\n90\n01"), facade.context.profile.result),
        (5, "", "".join("67\n78\n89\n90\n01"), facade.context.profile.result),
        (91111, facade.context.profile.file_path, "".join("12\n23\n34\n45\n56\n67\n78\n89\n90\n01"),
         facade.context.profile.result),
        (None, None, facade.context.profile.error_message, facade.context.profile.result),
        ("", "", facade.context.profile.error_message, facade.context.profile.result)
        ])
def test_check_job_through_the_print_func(lines_from_end, file_path, expected, result):
    with soft_assertions():
        with open(f"{facade.context.root_path}{result}", "r") as result_file:
            assert_that(AppData().if_print_are_mandatory_condition(lines_from_end, file_path)).is_equal_to(expected)
            assert_that(result_file.read().strip()).is_equal_to(expected)
