import subprocess
import sys
import shutil
import os
import stat


def ignore_errors(func, path, exc_info):
    print('Was ignored: ', exc_info)
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)


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


if __name__ == "__main__":
    install('short_url')
    install('django')

    if 'PyCharm' in sys.argv or True:
        subprocess.call('git clone -n https://github.com/github/gitignore.git --depth 1')
        subprocess.call('git checkout HEAD Global/JetBrains.gitignore', cwd='gitignore')
        join_files(['django.gitignore', 'gitignore/Global/JetBrains.gitignore'], '../.gitignore')
        remove_dir('gitignore')
    else:
        join_files(['django.gitignore'], '.gitignore')
        remove_dir('.idea')
