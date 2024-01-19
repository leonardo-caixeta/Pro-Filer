from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_existing_file(capsys):
    context = {"base_path": "/home/leonardo/Trybe"}

    expected_output = (
        "File name: Trybe\n"
        "File size in bytes: 4096\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        "Last modified date: 2024-01-15"
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


def test_show_details_directory(capsys):
    context = {"base_path": "/home/leonardo/Trybe"}

    expected_output = (
        "File name: Trybe\n"
        "File size in bytes: 4096\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        "Last modified date: 2024-01-15"
    )

    show_details(context)
    captured_output = capsys.readouterr()
    assert captured_output.out.strip() == expected_output.strip()
