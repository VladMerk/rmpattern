import pytest
import os

from main import remove_prefix


@pytest.fixture()
def create_test_dir(tmp_path):
    test_dir = tmp_path
    os.makedirs(os.path.join(test_dir, "prefix-dir"))
    os.makedirs(os.path.join(test_dir, "prefix-dir2"))
    os.makedirs(os.path.join(test_dir, "prefix-dir2", "prefix-dir5"))
    with open(os.path.join(test_dir, "prefix-file"), "w") as f:
        f.write("test content")
    with open(os.path.join(test_dir, "prefix-file2"), "w") as f:
        f.write("test content")
    with open(os.path.join(test_dir, "prefix-dir2", "prefix-dir5", "prefix-file-5"), "w") as f:
        f.write("test content")
    return test_dir


@pytest.fixture()
def create_ru_dir(tmp_path):
    test_dir = tmp_path
    os.makedirs(os.path.join(test_dir, "префикс 001 папка"))
    os.makedirs(os.path.join(test_dir, "префикс 002 папка2"))
    os.makedirs(os.path.join(test_dir, "префикс 002 папка2", "префикс 003 папка5"))
    with open(os.path.join(test_dir, "префикс файл"), "w") as file:
        file.write("Тест контент")
    with open(os.path.join(test_dir, "префикс 001 папка", "префикс файл2"), "w") as file:
        file.write("Тест контент")
    with open(os.path.join(test_dir, "префикс 002 папка2", "префикс 003 папка5", "префикс файл3"), "w") as file:
        file.write("Тест контент")
    return test_dir


def test_remove_prefix(create_test_dir):
    test_dir = create_test_dir
    remove_prefix(test_dir, "prefix-")

    assert os.path.exists(os.path.join(test_dir, "dir"))
    assert os.path.exists(os.path.join(test_dir, "dir2"))
    assert os.path.exists(os.path.join(test_dir, "file"))
    assert os.path.exists(os.path.join(test_dir, "file2"))
    assert os.path.exists(os.path.join(test_dir, "dir2", "dir5", "file-5"))


def test_remove_ru_prefix(create_ru_dir):
    test_dir = create_ru_dir
    remove_prefix(test_dir, "префикс")

    assert os.path.exists(os.path.join(test_dir, "001 папка"))
    assert os.path.exists(os.path.join(test_dir, "002 папка2"))
    assert os.path.exists(os.path.join(test_dir, "002 папка2", "003 папка5"))
    assert os.path.exists(os.path.join(test_dir, "файл"))
    assert os.path.exists(os.path.join(test_dir, "002 папка2", "003 папка5", "файл3"))
