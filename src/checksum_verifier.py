from tqdm import tqdm
from os.path import isfile
from urllib.request import urlretrieve, urlopen
import problem_unittests as tests
import os


# user input
download_link = 'https://download.jetbrains.com/python/pycharm-professional-2018.1.4.tar.gz'  # put file download link
download_folder = 'data/output'  # where to keep the downloaded file
# different checksum formats: cksum, md5sum, shasum, sha1sum, sha256sum, sha512sum, sha224sum, sha384sum
checksum_format = 'sha256sum'  # choose the checksum format according to the checksum file link
checksum_file_link = 'https://download.jetbrains.com/python/pycharm-professional-2018.1.4.tar.gz.sha256'


# download the file
class DownloadProgress(tqdm):
    """
      Decorate an iterable object, returning an iterator which acts exactly
      like the original iterable, but prints a dynamically updating
      progressbar every time a value is requested.
      """
    last_block = 0

    def hook(self, block_num=1, block_size=1, total_size=None):
        self.total = total_size
        self.update((block_num - self.last_block) * block_size)
        self.last_block = block_num


if not isfile(download_link):
    with DownloadProgress(unit='B', unit_scale=True, miniters=1, desc='File downloaded') as progress_bar:
        urlretrieve(download_link, download_folder + 'my_file.tar.gz', progress_bar.hook)
tests.test_folder_path(download_folder)  # to test if the file downloaded properl


def main():
    given_checksum_output = urlopen(checksum_file_link).read().decode('UTF-8').split()[0]
    file_checksum_output = os.popen(checksum_format + ' ' + download_folder + '/' + 'my_file.tar.gz').read().split()[0]
    if file_checksum_output == given_checksum_output:
        print('Congratulations, the file you have downloaded is identical to the source!')
    else:
        print('Sorry, the file you have downloaded is not identical to the source!')


if __name__ == "__main__":
    main()
