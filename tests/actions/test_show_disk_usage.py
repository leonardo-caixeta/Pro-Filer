from pro_filer.actions.main_actions import show_disk_usage
from pro_filer.cli_helpers import _get_printable_file_path


def test_show_disk_usage(capsys, tmp_path):
    all_files_paths = []

    fake1_file_path = tmp_path / "fake1.txt"
    fake1_file_path.write_text("se inscreva, quero 50 inscrito")
    fake1_file_path.touch()
    fake1_file_path = str(fake1_file_path)
    all_files_paths.append(fake1_file_path)
    satanas = f"'{_get_printable_file_path(fake1_file_path)}':".ljust(70) + " 30 (41%)"  # NOQA

    fake2_file_path = tmp_path / "fake2.txt"
    fake2_file_path.write_text("se inscreva, quero vários inscritos papai")
    fake2_file_path.touch()
    fake2_file_path = str(fake2_file_path)
    all_files_paths.append(fake2_file_path)
    lucifer = f"'{_get_printable_file_path(fake2_file_path)}':".ljust(70) + " 42 (58%)"  # NOQA

    expected_output = "\n".join([lucifer, satanas]) + "\nTotal size: 72\n"

    context = {"all_files": all_files_paths}
    show_disk_usage(context)
    captured_output = capsys.readouterr().out
    assert captured_output == expected_output

    context = {"all_files": []}
    show_disk_usage(context)
    captured_output = capsys.readouterr().out
    assert captured_output == "Total size: 0\n"
