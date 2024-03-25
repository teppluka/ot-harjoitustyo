# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on Scrabble-peli, jonka tavoitteena on muodostaa sanoja 15x15 kokoiselle pelilaudalle. Peliä voi pelata 2-4 pelaajaa.

## Perusversion toiminnallisuus

- Kaikille pelaajille arvotaan aluksi seitsemän kirjainta
- Kukin pelaaja voi vuorollaan muodostaa jonkin sanan asettamalla kirjaimiaan pelilaudalle
- Kaikilla kirjaimilla on oma pistearvonsa, ja muodostetusta sanasta saa näiden arvojen summan verran pisteitä
- Kun sana on muodostettu, pelaajalle arvotaan lisää kirjaimia, kunnes niitä on taas seitsemän
- Kirjainlaattoja on pelissä varastossa rajallinen määrä, ja niiden loppuessa pelaajat eivät enää saa lisää kirjaimia
- Pelaaja voi myös ohittaa vuoronsa
- Peli loppuu, kun joku pelaaja saa käytettyä kaikki laattansa eikä niitä ole enää pelin varastossa
- Peli loppuu myös silloin, jos kaikki pelaajat ohittavat vuoronsa kahdella peräkkäisellä kierroksella
- Pelin voittaa se pelaaja, joka on kerännyt eniten pisteitä

### Sanojen vaatimukset

- Sanat ovat englanninkielisiä
- Pelin ensimmäisen sanan tulee osua pelilaudan keskimmäiseen ruutuun
- Kaikkien seuraavien sanojen täytyy yhdistyä johonkin jo laudalla olevaan sanaan
- Sanat kirjoitetaan joko vasemmalta oikealle tai ylhäältä alas
- Laudalle ei saa muodostua yli yhden merkin pituisia merkkijonoja, jotka eivät ole sanoja

## Mahdollinen jatkokehitys

- Laudalla on erikoisruutuja, jotka joko kaksin- tai kolminkertaistavat kirjaimesta tai koko sanasta saatavat pisteet
- Pelaajat voivat luoda pysyviä käyttäjiä, joilla säilyvät tiedot voittojen ja haviöiden määrästä sekä ennätyspistemääristä
- Vuoroilla on aikaraja, jonka ylittyessä vuoro ohitetaan automaattisesti
