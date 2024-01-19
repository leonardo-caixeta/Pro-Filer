# Arquivo: tests/actions/test_show_preview.py
from pro_filer.actions.main_actions import show_preview
import pytest


def test_show_preview_with_files_and_dirs(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }

    expected_output = (
        "Found 3 files and 2 directories\n"
        """First 5 files: [
            'src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\n"""
        "First 5 directories: ['src', 'src/utils']"
    )

    with pytest.raises(SystemExit):
        show_preview(context)
        captured_output = capsys.readouterr()
        assert captured_output.out == expected_output


def test_show_preview_with_empty_files_and_dirs(capsys):
    context = {"all_files": [], "all_dirs": []}

    expected_output = "Found 0 files and 0 directories\n"

    with pytest.raises(SystemExit):
        show_preview(context)
        captured_output = capsys.readouterr()
        assert captured_output.out == expected_output
