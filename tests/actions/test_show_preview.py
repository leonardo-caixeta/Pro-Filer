from pro_filer.actions.main_actions import show_preview


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
        """First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\n"""
        "First 5 directories: ['src', 'src/utils']\n"
    )

    show_preview(context)
    captured_output = capsys.readouterr()
    assert captured_output.out == expected_output
    assert captured_output.err == ""


def test_show_preview_with_empty_files_and_dirs(capsys):
    context = {"all_files": [], "all_dirs": []}

    expected_output = "Found 0 files and 0 directories\n"

    show_preview(context)
    captured_output = capsys.readouterr()
    assert captured_output.out == expected_output
    assert captured_output.err == ""


def test_show_preview_with_more_than_5_files_and_dirs(capsys):
    context = {
        "all_files": [
            f"file_{i}.txt" for i in range(1, 10)
        ],
        "all_dirs": [
            f"dir_{i}" for i in range(1, 10)
        ],
    }

    expected_output = (
        "Found 9 files and 9 directories\n"
        "First 5 files: ['file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt', 'file_5.txt']\n"
        "First 5 directories: ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5']\n"
    )

    show_preview(context)
    captured_output = capsys.readouterr()
    assert captured_output.out == expected_output
    assert captured_output.err == ""
