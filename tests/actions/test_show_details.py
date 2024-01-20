from pro_filer.actions.main_actions import show_details  # NOQA
import os
import pytest

images_dir = "images"


@pytest.fixture
def gif_path():
    return os.path.join(images_dir, "pro-filer-preview.gif")


@pytest.fixture
def broken_gif_path():
    return os.path.join(images_dir, "pro-filer-preview")


def test_show_details_existing_file(capsys, gif_path):
    context = {"base_path": gif_path}

    expected_output = (
        "File name: pro-filer-preview.gif\n"
        "File size in bytes: 270824\n"
        "File type: file\n"
        "File extension: .gif\n"
        "Last modified date: 2024-01-18"
    )

    show_details(context)
    captured_output = capsys.readouterr()
    assert captured_output.out.strip() == expected_output.strip()


def test_show_details_nonexistent_file(capsys):
    context = {"base_path": "/home/trybe/?????"}

    expected_output = "File '?????' does not exist"

    show_details(context)
    captured_output = capsys.readouterr()
    assert captured_output.out.strip() == expected_output.strip()


def test_show_details_directory(capsys, gif_path):
    context = {"base_path": gif_path}

    expected_output = (
        "File name: pro-filer-preview.gif\n"
        "File size in bytes: 270824\n"
        "File type: file\n"
        "File extension: .gif\n"
        "Last modified date: 2024-01-18"
    )

    show_details(context)
    captured_output = capsys.readouterr()
    assert captured_output.out.strip() == expected_output.strip()


def test_show_details_nonexistent_extension(capsys, broken_gif_path):
    context = {"base_path": broken_gif_path}

    expected_output = (
        "File name: pro-filer-preview\n"
        "File size in bytes: 12\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: 2024-01-20"
    )

    show_details(context)
    captured_output = capsys.readouterr()
    assert captured_output.out.strip() == expected_output.strip()
