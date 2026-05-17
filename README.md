# Examination: Testautomatisering och testverktyg, NBIHAK TAPHT25D
### Student: Amélia Uebel  
### Lärare: David Andersson


# Läslistan webbsida

Examen går ut på att testa för grundläggande funktionalitet för webbsidan ["Läslistan"](https://tap-ht25-testverktyg.github.io/exam/).
Uppgiften löstest genom arbetet med både frontend och backend, med fokus på att implementera TDD:enhetstester och integrationstester.

1) Jag har använt mig av pytest som testverktyg för att implementera både enhetstester och integrationstester för följande klasser och metoder
klassen BookStore ska ha följande metoder:
addBook(author, title)
toggleFavorite(book_id)
klassen FavoriteBooks ska ha följande metoder:
add(book)
remove(book)

Jag har försökt lösa samtliga punkter i Grundkraven men hann tyvärr inte göra klart steps delen. 

2) 
**Kör test case i terminalen:**
```bash
pytest -v -m unit
pytest -v -m integration
```

Filen `requirements.txt` innehåller alla paket som ska importeras.

Filen pythion-ci.yml Implementera CI för projektet, så att alla tester körs automatiskt när man pushar en ny version till main-branchen i GitHub.


# TODO:
 - Implementera steps för E2E-testning med Playwright och BDD
 - Implementera E2E-testning med Playwright och BDD