# 🕷️ Scrapy Scraper

A **Scrapy Scraper** egy Python-alapú webes adatgyűjtő eszköz, amely a [Scrapy](https://scrapy.org/) keretrendszerre épül.

___

## 📰 Informácíó
### Kerítéselemenként:


```json
{
  "name": "Kerítésléc - íves / 1600mm hosszúság / Aranytölgy", 
    "image": "https://kallofem.hu/storage/product-color-gallery/278/4z9x3bYXMdBFo4j5PRlRKAuv5l16nmT5L0XNJr7L.jpg",
    "price": "1 734 Ft"
}
```
___
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
      
___

## 🚀 Deploy

A scrapyd project Github Actions segítségével automatikusan lefuttatja a scapyd-deploy parancsot ami frissíti az AWS-en futó scrapyd serveren a projectet
A és egy beállított task runner naponta lefuttatja a spider-t

### 📦 Használt eszközök

- **AWS** EC2
- **Scrapyd** (Scrapy server)
- **Scrapydweb** (Scrapyd ui)
- **Apche** (for serving json files)
___
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

---
2
# 📂 Mentések
A generált JSON fájlok elérhetők: [itt](http://ec2-16-16-171-241.eu-north-1.compute.amazonaws.com/files/)

Fájlok formátuma: .json


### AWS setup
A Scrapyd és Scrapydweb config fájlok nincsenek fent Githubon mert alap konfigurációkkal is működik.


# 🪲Észrevételek / Bugs

A scraper fejlesztése közben találtam pár hibát az oldalon

---

## ⚙️ Rendezés (Dropdown)

**Probléma:**
A rendezési dropdow nem működik, kattintásra nem történik semmi. A böngésző konzoljában az alábbi hiba jelenik meg:

```
TypeError: t.createPopper is not a function
```

**Oka:**
A `Popper.js` könyvtár nem töltődik be megfelelően.

**Megoldás:**
Győződj meg róla, hogy a `Popper.js` könyvtár helyesen be van töltve. 

```html
<!-- Helyezd a HEAD szekcióba minden más script előtt -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.9.2/umd/popper.min.js"></script>
```
**a megoldás tesztelve** Chrome DevTools Override funkcióval 
___

## 🏠 Index oldal / Terméklista

Az alábbi két URL között jelentős eltérés van a megjelenített termékek számában:

| Oldal URL                          | Termékek száma | Lapok száma |
| ---------------------------------- | -------------- |-------------|
| `/shop/group/keriteselemek`        |   94      | 4           |
| `/shop/group/keriteselemek?page=1` |     1902            | 68          |

**Megfigyelés:**
Egy szűrés aktív lehet az alapoldalon, amely a lapozás vagy rendezés alkalmazásakor megszűnik (pl. `&sort=name_asc` esetén is). Ez **félrevezető** lehet a felhasználók számára.

**Javaslat:**

* Tegyük láthatóvá és vezérelhetővé a szűrést a felhasználó számára. 
  - vagy
* Vegyük ki a szűrés az alap oldaról.

---

## 🖼 Képnagyítás / Galéria hibák

1. **Több nagyításablak is egyszerre megnyitható**, és a görgetősáv eltűnik.
2. **Az `X` bezáró gomb nem minden esetben látható**, igy csak az `ESC` gombal lehet kilépni de a felhasználó nem feltétlenül tudja .
3. **Az `X` és a lapozógombok kurzora nem megfelelő** – szöveg kiemelő kurzor jelenik meg kattintható👆 ikon helyett.
4. A gombok mérete nem megfelelő főleg mobil eszközökön 

**Javasolt megoldás:**

* A classok alapján a kód [projecten](https://github.com/jestov/grid-gallery/tree/master) alapul egy ehhez közelebbi vagy teljesen megegyező implementáció megoldja a problémákat
* 
  vagy válts egy Bootstrap-alapú megoldásra (pl. **Carousel** vagy **Modal** komponens).
* vagy Fancybox-ra

---

## 📝 Termékleírás szakasz

1. **A `még több` gomb nem működik.**
   A gomb ugyan hozzáadja az `.expand` osztályt, de az ehhez tartozó CSS hiányzik.

   **Megoldás:**
   Adjunk hozzá megfelelő stílust:

   ```css
   .expand {
     max-height: none;
   }
   ```

2. **A táblázat nem teljesen látható** Az adott konténer fix magassága nem alkalmazkodik a tartalom méretéhez.
   
   **Lehetséges megoldások:**
    - JavaScript segítségével dinamikusan állítsuk a magasságot,
   - Bootsrap [**Tabs**](https://getbootstrap.com/docs/5.0/components/navs-tabs/#javascript-behavior) or [**Collapse**](https://getbootstrap.com/docs/4.0/components/collapse/#accordion-example)



