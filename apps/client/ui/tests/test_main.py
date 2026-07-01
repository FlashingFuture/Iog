from main import WEB_DIR


def test_web_dir_points_to_existing_folder():
    assert WEB_DIR.is_dir()


def test_index_html_exists():
    assert (WEB_DIR / "index.html").is_file()
