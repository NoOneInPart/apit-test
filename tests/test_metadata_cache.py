from pathlib import Path

from apit.metadata_cache import generate_cache_filename, save_to_cache


def test_generate_cache_filename(test_song):
    assert generate_cache_filename(Path('.'), test_song) == Path('./Album_Artist-Test_Album_Namè-12345.json')


def test_cache_file_creation(tmp_path, test_metadata):
    cache_file = tmp_path / 'test-file.json'
    assert not cache_file.exists()

    save_to_cache(test_metadata, cache_file)

    assert cache_file.exists()
    assert cache_file.read_text() == test_metadata


def test_cache_file_creation_creates_folder_hierarchy(tmp_path, test_metadata):
    cache_file = tmp_path / 'test-folder/test-file.json'
    assert not cache_file.exists()

    save_to_cache(test_metadata, cache_file)

    assert cache_file.exists()
    assert cache_file.read_text() == test_metadata
