import os
import shutil
import stat
import subprocess
import sys


# Fix: some .git directory files cannot be deleted due to readonly attribute
def ignore_errors(func, path, exc_info):
    if type(exc_info[1]) == PermissionError and '.git' in exc_info[1].filename:
        if not os.access(path, os.W_OK):
            os.chmod(path, stat.S_IWUSR)
            func(path)
    else:
        raise exc_info[1]


def remove_file(path):
    os.remove(path)


def remove_dir(path):
    shutil.rmtree(path, onerror=ignore_errors)


def install(package):
    subprocess.call(f'"{sys.executable}" -m pip install --user "{package}"', shell=True)


def join_files(file_names, output_path):
    with open(output_path, 'w') as outfile:
        for file_name in file_names:
            with open(file_name) as infile:
                for line in infile:
                    outfile.write(line)


def single_checkout(url, remote_path, local_path):
    subprocess.call(f'git clone -n "{url}" --depth 1', shell=True)
    temp = url.split('/')[-1]
    if not temp.endswith('.git'):
        raise Exception('Given url is not git-like!')
    dir_name = temp[:-4]
    subprocess.call(f'git checkout HEAD "{remote_path}"', shell=True, cwd=dir_name)
    shutil.move(os.path.join(dir_name, remote_path), local_path)
    remove_dir(dir_name)


if __name__ == "__main__":
    PYCHARM = True

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if 'nopycharm' in map(str.lower, sys.argv):
        PYCHARM = False

    install('short_url')
    install('django')

    single_checkout('https://github.com/github/gitignore.git', 'Global/JetBrains.gitignore', 'JetBrains.gitignore')
    if PYCHARM:
        join_files(['base.gitignore', 'JetBrains.gitignore'], '../.gitignore')
        remove_file('JetBrains.gitignore')
    else:
        join_files(['base.gitignore', 'no_pycharm.gitignore'], '.gitignore')

    single_checkout('https://github.com/necolas/normalize.css.git', 'normalize.css',
                    '../shortener_app/static/shortener_app/css/normalize.css')
