from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_with_files_and_dirs(capsys):
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }
    show_preview(context)
    captured = capsys.readouterr()
    assert "Found 3 files and 2 directories" in captured.out
    assert "First 5 files:" in captured.out
    assert "src/__init__.py" in captured.out
    assert "src/app.py" in captured.out
    assert "src/utils/__init__.py" in captured.out
    assert "First 5 directories:" in captured.out
    assert "src" in captured.out
    assert "src/utils" in captured.out


def test_show_preview_with_empty_files_and_dirs(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    captured = capsys.readouterr()
    assert "Found 0 files and 0 directories" in captured.out
