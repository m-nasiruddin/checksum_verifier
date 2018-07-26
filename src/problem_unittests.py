import os


def _print_success_message():
    return print('Tests Passed')


def test_folder_path(download_folder):
    assert download_folder is not None, 'Data folder not set.'
    assert download_folder[-1] != '/', 'The "/" shouldn\'t be added to the end of the path.'
    assert os.path.exists(download_folder), 'Path not found.'
    assert os.path.isdir(download_folder), '{} is not a folder.'.format(os.path.basename(download_folder))
    downloaded_files = [download_folder + 'downloaded_file.tar.gz']
    missing_files = [path for path in downloaded_files if not os.path.exists(path)]
    assert not missing_files, 'Missing file in directory: {}'.format(missing_files)
    print('File found!')
    _print_success_message()
