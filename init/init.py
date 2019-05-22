import os
import shutil
import stat
import subprocess
import sys

PYCHARM = True


def ignore_errors(func, path, exc_info):
    print('Was ignored: ', exc_info)
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)


def remove_file(path):
    os.remove(path)


def remove_dir(path):
    shutil.rmtree(path, onerror=ignore_errors)


def install(package):
    subprocess.call([sys.executable, '-m', 'pip', 'install', package])


def join_files(file_names, output_path):
    with open(output_path, 'w') as outfile:
        for file_name in file_names:
            with open(file_name) as infile:
                for line in infile:
                    outfile.write(line)


def single_checkout(url, remote_path, local_path):
    subprocess.call(f'git clone -n {url} --depth 1')
    temp = url.split('/')[-1]
    if not temp.endswith('.git'):
        raise Exception('Given url is not git-like!')
    dir_name = temp[:-4]
    subprocess.call(f'git checkout HEAD {remote_path}', cwd=dir_name)
    shutil.move(os.path.join(dir_name, remote_path), local_path)
    remove_dir(dir_name)


if __name__ == "__main__":
    install('short_url')
    install('django')

    if PYCHARM:
        single_checkout('https://github.com/github/gitignore.git', 'Global/JetBrains.gitignore', 'JetBrains.gitignore')
        join_files(['base.gitignore', 'JetBrains.gitignore'], '../.gitignore')
        remove_file('JetBrains.gitignore')
    else:
        join_files(['base.gitignore', 'no_pycharm.gitignore'], '.gitignore')

    single_checkout('https://github.com/necolas/normalize.css.git', 'normalize.css',
                    '../shortener_app/static/shortener_app/css/normalize.css')
