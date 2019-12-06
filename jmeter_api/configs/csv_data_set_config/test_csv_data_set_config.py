from jmeter_api.configs.csv_data_set_config.elements import CsvDataSetConfig, ShareMode
from jmeter_api.basics.utils import FileEncoding
import pytest


class TestCsvDataSetConfigFilePath:
    def test_type_check(self):
        with pytest.raises(FileNotFoundError, match=r".*is not file*"):
            CsvDataSetConfig(file_path='ErrorPath',
                             variable_names=['var1', 'var2'])

    def test_type_check2(self):
        with pytest.raises(FileNotFoundError, match=r".*is not file*"):
            CsvDataSetConfig(file_path='./ErrorPath',
                             variable_names=['var1', 'var2'])

    def test_positive(self):
        csvdata = CsvDataSetConfig(
            file_path='main.py', variable_names=['var1', 'var2'])
        assert csvdata.file_path == 'main.py'

    def test_positive2(self):
        file_path = './main.py'
        csvdata = CsvDataSetConfig(
            file_path=file_path, variable_names=['var1', 'var2'])
        assert csvdata.file_path == file_path


class TestCsvDataSetConfigVariableNames:
    def test_type_check(self):
        with pytest.raises(TypeError, match=r".*file_encoding must be List[str]*"):
            CsvDataSetConfig(file_path='main.py', variable_names={
                'randkey': 'randvalue'})

    def test_content_type_check(self):
        with pytest.raises(TypeError, match=r".*All elements must be str*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'asdfg', 123, 'qwerty'])

    def test_content_type_check2(self):
        with pytest.raises(TypeError, match=r".*must contain chars*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'asdfg', '123', 'qwerty'])

    def test_variable_names(self):
        csvdata = CsvDataSetConfig(file_path='main.py', variable_names=[
            'asdfg', 'vbn', 'qwerty'])
        assert csvdata.variable_names == 'asdfg,vbn,qwerty'


class TestCsvDataSetConfigDelimiter:
    def test_positive(self):
        csvdata = CsvDataSetConfig(file_path='main.py', variable_names=[
            'asdfg', 'vbn', 'qwerty'], delimiter='|')
        assert csvdata.variable_names == 'asdfg|vbn|qwerty'


class TestCsvDataSetConfigFileEncoding:
    def test_type_check(self):
        with pytest.raises(TypeError, match=r".*must be FileEncoding*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'var1', 'var2'], file_encoding='UTF-8')

    def test_type_check2(self):
        with pytest.raises(TypeError, match=r".*must be FileEncoding*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'var1', 'var2'], file_encoding=100)

    def test_positive(self):
        csvdata = CsvDataSetConfig(file_path='main.py', variable_names=[
            'var1', 'var2'], file_encoding=FileEncoding.ISO8859)
        assert csvdata.file_encoding == FileEncoding.ISO8859


class TestCsvDataSetConfigIgnoreFirstLine:
    def test_type_check(self):
        with pytest.raises(TypeError, match=r".*must be bool.*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'var1', 'var2'], ignore_first_line='True')

    def test_type_check2(self):
        with pytest.raises(TypeError, match=r".*must be bool.*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'var1', 'var2'], ignore_first_line=123456)

    def test_positive(self):
        csvdata = CsvDataSetConfig(file_path='main.py', variable_names=[
            'var1', 'var2'], ignore_first_line=True)
        assert csvdata.ignore_first_line == 'true'


class TestCsvDataSetConfigRecycle:
    def test_type_check(self):
        with pytest.raises(TypeError, match=r".*must be bool.*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'var1', 'var2'], recycle='True')

    def test_type_check2(self):
        with pytest.raises(TypeError, match=r".*must be bool.*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'var1', 'var2'], recycle=123456)

    def test_positive(self):
        csvdata = CsvDataSetConfig(file_path='main.py', variable_names=[
            'var1', 'var2'], recycle=True)
        assert csvdata.recycle == 'true'


class TestCsvDataSetConfigStopThread:
    def test_type_check(self):
        with pytest.raises(TypeError, match=r".*must be bool.*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'var1', 'var2'], stop_thread='True')

    def test_type_check2(self):
        with pytest.raises(TypeError, match=r".*must be bool.*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'var1', 'var2'], stop_thread=123456)

    def test_positive(self):
        csvdata = CsvDataSetConfig(file_path='main.py', variable_names=[
            'var1', 'var2'], stop_thread=True)
        assert csvdata.stop_thread == 'true'


class TestCsvDataSetConfigSharedMode:
    def test_type_check(self):
        with pytest.raises(TypeError, match=r".*must be ShareMode*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'var1', 'var2'], share_mode='True')

    def test_type_check2(self):
        with pytest.raises(TypeError, match=r".*must be ShareMode*"):
            CsvDataSetConfig(file_path='main.py', variable_names=[
                'var1', 'var2'], share_mode=123456)

    def test_positive(self):
        csvdata = CsvDataSetConfig(file_path='main.py', variable_names=[
            'var1', 'var2'], share_mode=ShareMode.ALL)
        assert csvdata.share_mode == ShareMode.ALL
