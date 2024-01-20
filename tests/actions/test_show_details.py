#  Here is how I got date in the format
#  https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python

from pro_filer.actions.main_actions import show_details  # NOQA
import pytest
from datetime import datetime


@pytest.mark.parametrize(
    "filename, expected_output",
    [
        (
            "file.json",
            (
                "File name: file.json\n"
                "File size in bytes: 0\n"
                "File type: file\n"
                "File extension: .json\n"
                f"Last modified date: {datetime.today().strftime('%Y-%m-%d')}"
            )
        ),
        (
            "file",
            (
                "File name: file\n"
                "File size in bytes: 0\n"
                "File type: file\n"
                "File extension: [no extension]\n"
                f"Last modified date: {datetime.today().strftime('%Y-%m-%d')}"
            )
        )
    ]
)
def test_show_details(capsys, tmp_path, filename, expected_output):
    fake_file_path = tmp_path / filename
    fake_file_path.touch()
    fake_file_path = str(fake_file_path)
    context = {"base_path": fake_file_path}

    show_details(context)
    captured_output = capsys.readouterr()

    assert captured_output.out.strip() == expected_output.strip()


def test_show_details_nonexistent_file(capsys):
    context = {"base_path": "/home/trybe/?????"}

    expected_output = "File '?????' does not exist"

    show_details(context)
    captured_output = capsys.readouterr()
    assert captured_output.out.strip() == expected_output.strip()
