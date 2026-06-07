# Examination: Testautomatisering och testverktyg, NBIHAK TAPHT25D
### Student: Amélia Uebel  
### Lärare: David Andersson


# Läslistan webbsida

Examen går ut på att testa för grundläggande funktionalitet för webbsidan ["Läslistan"](https://tap-ht25-testverktyg.github.io/exam/).
Uppgiften löstest genom arbetet med både frontend och backend, med fokus på att implementera TDD:enhetstester och integrationstester.
BDD har också använts för att implementera testfall i Gherkin-syntax, som sedan körs med hjälp av Behave.


1) Jag har använt mig av pytest som testverktyg för att implementera både enhetstester och integrationstester för följande klasser och metoder  

    klassen BookStore ska ha följande metoder:
    - addBook(author, title)
    - toggleFavorite(book_id)  

    klassen FavoriteBooks ska ha följande metoder:
    - add(book)
    - remove(book)  
   
    BDD har använts för att implementera testfall i Gherkin-syntax, som sedan körs med hjälp av Behave. Testfallen är skrivna i folder `features` och täcker stories i STORIES.md filen om vyn "Katalog", "Lägg till bok", "Mina böcker" och "Statistik".


2) Nedan följer instruktioner för hur man startar projektet och kör testerna:

För att starta:
```commandline
behave --format pretty
```
Projektet använder behave för att köra Gherkin-kodade testfall.


**Kör test case i terminalen:**
```bash
pytest -v -m unit
pytest -v -m integration
```

**Kör flake8(Linting) för testerna i terminalen:**
```bash
flake8 src tests

```


Filen `requirements.txt` innehåller alla paket som ska importeras.

Filen 'pythion-ci.yml' (.github/workflows/python-ci.yml) implementerar CI för projektet, så att alla tester körs automatiskt när man pushar en ny version till main-branchen i GitHub.


