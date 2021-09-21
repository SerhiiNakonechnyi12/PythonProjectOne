import pytest
import sys

# в названии файла добавить test_

# @pytest.mark.skip(reason="Not included in this build")
# def test_demo_1():
#     assert True
#
#
# @pytest.mark.skipif(sys.version_info < (3, 7),
#                     reason="requires python3.7 or higher")
# def test_demo_2():
#     assert True
#
#
# def test_demo_3():
#     assert True


@pytest.mark.windows
def test_windows_1():
    assert True


@pytest.mark.windows
def test_windows_2():
    assert True


@pytest.mark.mac
def test_mac_1():
    assert True


@pytest.mark.mac
def test_mac_2():
    assert True
