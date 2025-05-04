# 🕷️ Scrapy Scraper

A **Scrapy Scraper** egy Python-alapú webes adatgyűjtő eszköz, amely a [Scrapy](https://scrapy.org/) keretrendszerre épül.

## 📰 Informácíó
### Kerítéselemenként:


```json
{
  "name": "Kerítésléc - íves / 1600mm hosszúság / Aranytölgy", 
    "image": "https://kallofem.hu/storage/product-color-gallery/278/4z9x3bYXMdBFo4j5PRlRKAuv5l16nmT5L0XNJr7L.jpg",
    "price": "1 734 Ft"
}
```

## 🛠️ Telepítés

### Előfeltételek

- Python 3.6 vagy újabb
- pip (Python csomagkezelő)

### 👣Lépések

1. **Tárhely klónozása**

   ```bash
   git clone https://github.com/Kzmkr/scrapy-scraper.git
   cd scrapy-scraper
   ```

2. **Virtuális környezet létrehozása (ajánlott)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows alatt: venv\Scripts\activate
   ```

3. **Függőségek telepítése**

   ```bash
   pip install scrapy
   ```

### 🕹️ Használat

   1. **Projekt könyvtárba lépés**

      ```bash
      cd scrapy-scraper
      ```

   2. **Spider futtatása**

      ```bash
      scrapy crawl keriteselem
      ```

## 🚀 Deploy

A scrapyd project Github Actions segítségével automatikusan lefuttatja a scapyd-deploy parancsot ami frissíti az AWS-en futó scrapyd serveren a projectet
A és egy beállított task runner naponta lefuttatja a spider-t

### 📦 Használt eszközök

- **AWS** EC2
- **Scrapyd** (Scrapy server)
- **Scrapydweb** (Scrapyd ui)
- **Apche** (for serving json files)

## ⚙️ Használata

### Webes felület

- Elérhető itt: [ScrapydWeb](http://ec2-16-16-171-241.eu-north-1.compute.amazonaws.com:5000/)

- Spider indítása:

    - Nyisd meg a webes felületet

   - Válaszd ki a **"Run Spider"** opciót

   - Válaszd ki a projectet és a spidert

   - Kattints a **"Check CMD"** és **"Run"** gombokra
  
- Időzített futtatás

   - A **"Timer Tasks"** menüpontban beállíthatod az automatikus futtatást


### Scrapyd api
Spider indítása API-n keresztül:

```bash
curl http://ec2-16-16-171-241.eu-north-1.compute.amazonaws.com:6800/schedule.json -d project=kallofem -d spider=keriteselem   
```
További API opciókért [lásd](https://scrapyd.readthedocs.io/en/stable/api.html)

# 📂 Mentések
A generált JSON fájlok elérhetők: [itt](http://ec2-16-16-171-241.eu-north-1.compute.amazonaws.com/files/)

Fájlok formátuma: .json


### AWS setup
A Scrapyd és Scrapydweb config fájlok nincsenek fent Githubon mert alap konfigurációkkal is működik.
    

