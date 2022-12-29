# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from setuptools import setup
from io         import open

setup(
    # ? Genel Bilgiler
    name         = "tcdd_bilet_kontrol",
    version      = "0.1",
    url          = "https://github.com/keyiflerolsun/tcdd_bilet_kontrol",
    description  = "TCDD Bilet Kontrol Etme Arayüzü",
    keywords     = ["tcdd_bilet_kontrol", "KekikAkademi", "keyiflerolsun"],

    author       = "keyiflerolsun",
    author_email = "keyiflerolsun@gmail.com",

    license      = "GPLv3+",
    classifiers  = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3"
    ],

    # ? Paket Bilgileri
    packages         = ["tcdd_bilet_kontrol"],
    python_requires  = ">=3.10",
    install_requires = [
        "pip",
        "setuptools",
        "wheel",
        "Kekik",
        "SelSik",
        "flet",
        "pandas",
        "regex",
        "tabulate",
        "notify-py"
    ],

    # ? Konsoldan Çalıştırılabilir
    entry_points = {
        "console_scripts": [
            "tcdd_bilet_kontrol = tcdd_bilet_kontrol:basla",
        ]
    },

    # ? Masaüstü Paketi
    setup_requires = ["install_freedesktop"],
    data_files     = [
        ("share/icons/hicolor/scalable/apps", ["tcdd_bilet_kontrol/Assets/Logo.png"]),
        ("share/applications", ["org.kekikakademi.tcdd_bilet_kontrol.desktop"])
    ],

    # ? PyPI Bilgileri
    long_description_content_type = "text/markdown",
    long_description              = "".join(open("README.md", encoding="utf-8").readlines()),
    include_package_data          = True
)