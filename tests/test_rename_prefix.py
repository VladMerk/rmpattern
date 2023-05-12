import pytest
import os

from main import remove_prefix

@pytest.fixture()
def create_test_dir(tmp_path):
    test_dir = tmp_path
    os.makedirs(os.path.join(test_dir, 'prefix-dir'))
    os.makedirs(os.path.join(test_dir, 'prefix-dir2'))
    os.makedirs(os.path.join(test_dir, 'prefix-dir2', 'prefix-dir5'))
    with open(os.path.join(test_dir, 'prefix-file'), 'w') as f:
        f.write('test content')
    with open(os.path.join(test_dir, 'prefix-file2'), 'w') as f:
        f.write('test content')
    with open(os.path.join(test_dir, 'prefix-dir2', 'prefix-dir5', 'prefix-file-5'), 'w') as f:
        f.write('test content')
    return test_dir


def test_remove_prefix(create_test_dir):
    test_dir = create_test_dir
    remove_prefix(test_dir, 'prefix-')

    assert os.path.exists(os.path.join(test_dir, 'dir'))
    assert os.path.exists(os.path.join(test_dir, 'dir2'))
    assert os.path.exists(os.path.join(test_dir, 'file'))
    assert os.path.exists(os.path.join(test_dir, 'file2'))
    assert os.path.exists(os.path.join(test_dir, 'dir2', 'dir5', 'file-5'))
