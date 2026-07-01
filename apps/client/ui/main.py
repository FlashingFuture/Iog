from pathlib import Path

import webview

WEB_DIR = Path(__file__).parent / "web"


def main() -> None:
    webview.create_window(
        "IOG",
        url=str(WEB_DIR / "index.html"),
        width=420,
        height=640,
    )
    webview.start()


if __name__ == "__main__":
    main()
