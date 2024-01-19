from pro_filer.actions.main_actions import show_details  # NOQA

import pytest
from datetime import date


def test_show_details_existing_file(capsys):
    context = {"base_path": "/home/trybe/Downloads/Trybe_logo.png"}

    expected_output = (
        "File name: Trybe_logo.png\n"
        "File size in bytes: 22438\n"
        "File type: file\n"
        "File extension: .png\n"
        "Last modified date: 2023-06-13"
    )

    with pytest.raises(SystemExit):
        show_details(context)
        captured_output = capsys.readouterr()
        assert captured_output.out.strip() == expected_output.strip()


def test_show_details_nonexistent_file(capsys):
    context = {"base_path": "/home/trybe/?????"}

    expected_output = "File '?????' does not exist"

    with pytest.raises(SystemExit):
        show_details(context)
        captured_output = capsys.readouterr()
        assert captured_output.out.strip() == expected_output.strip()


def test_show_details_directory(capsys):
    context = {"base_path": "/home/trybe/Documents"}

    expected_output = (
        "File name: Documents\n"
        "File size in bytes: [no size for directories]\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        f"Last modified date: {date.today()}"
    )

    with pytest.raises(SystemExit):
        show_details(context)
        captured_output = capsys.readouterr()
        assert captured_output.out.strip() == expected_output.strip()
