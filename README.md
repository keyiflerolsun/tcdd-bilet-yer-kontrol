# 🚉 TCDD Bilet Kontrol

![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/tcdd_bilet_kontrol)
![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/tcdd_bilet_kontrol&title=Görüntülenme)
<a href="https://KekikAkademi.org/Kahve" target="_blank"><img src="https://img.shields.io/badge/☕️-Kahve Ismarla-ffdd00" title="☕️ Kahve Ismarla" style="padding-left:5px;"></a>

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tcdd-bilet-kontrol)
![PyPI - Status](https://img.shields.io/pypi/status/tcdd-bilet-kontrol)
![PyPI](https://img.shields.io/pypi/v/tcdd-bilet-kontrol)
![PyPI - Downloads](https://img.shields.io/pypi/dm/tcdd-bilet-kontrol)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/tcdd-bilet-kontrol)
![PyPI - License](https://img.shields.io/pypi/l/tcdd-bilet-kontrol)

*TCDD Bilet Kontrol Etme Arayüzü*

![Ekran Goruntusu](Resimler/EkranGoruntusu.png)

[![ForTheBadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Doğrudan Kullanım

```bash
pip install -U tcdd-bilet-kontrol

tcdd_bilet_kontrol
```

## <img src="https://www.akashtrehan.com/assets/images/emoji/terminal.png" height="42" align="center"> Manuel Paketleme Seçenekleri

### 🐍 Python

```bash
git clone https://github.com/keyiflerolsun/tcdd_bilet_kontrol.git
cd tcdd_bilet_kontrol

# Paketle
pip install .

# Artıkları Temizle
rm -rf build/ dist/ *.egg-info/ .eggs/ && find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Çalıştır
tcdd_bilet_kontrol

# Paketi Kaldır
pip uninstall tcdd_bilet_kontrol
```

### 📦 Flatpak

```bash
git clone https://github.com/keyiflerolsun/tcdd_bilet_kontrol.git
cd tcdd_bilet_kontrol

# Paketle
flatpak-builder --user --install --force-clean build-dir org.kekikakademi.tcdd_bilet_kontrol.yml

# Artıkları Temizle
rm -rf .flatpak* .vscode build-dir && find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Çalıştır
flatpak run org.kekikakademi.tcdd_bilet_kontrol

# Paketi Kaldır
flatpak uninstall org.kekikakademi.tcdd_bilet_kontrol
```

### ⚠️ Bilinen Olumsuzluklar

- **Flet** varsayılan başlık ve ikonu henüz değişemiyor.
    - > https://github.com/flet-dev/flet/discussions/378

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2022 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/tcdd_bilet_kontrol/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/KekikKahve)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*
