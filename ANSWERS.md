# TEORIFRÅGOR

### Fråga 1: Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
**Enhetstest:** Testar varje metod, klass eller funktion, i en specifik del av koden, för sig. Syftet med enhetstester är att verifiera att varje del fungerar som förväntat utan beroenden till andra delar av applikationen.  
**Integrationstest:** Testar hur olika moduler eller tjänster fungerar tillsammans för att säkerställa att applikationens olika delarna fungerar korrekt som en helhet.  
**Regressionstest:** Testar specifik funktionalitet antigen i förebyggande syfte eller efter att en bug har upptäckts. Syftet är att kontrollera att nya kodändringar inte har introducerat buggar eller problem i befintlig fungerande funktionalitet och säkerställer att applikationen fortsätter att fungera som den ska.  
**Prestandatest:** Testar hur snabbt, effektivt och stabilt ett system fungerar under olika belastningar och förhållanden. Prestationstester testar till exempel systemets svarstid, stabilitet vid högbelastning, minnesanvändning och skalbarhet.   
___


### Fråga 2:Beskriv hur det går till när man arbetar med TDD.
När man arbetar med TDD (Test-Driven Development) börjar man med att implementera testerna *innan* man skriver produktionskod. Arbetet görs iterativt genom "Red, Green, Refactor" processen.
Först skriver man en test fär en specifik funktionalitet som anny inte är implementerad och ser hur den misslyckas (Red), sedan skriver man tillräckligt med kod som uppfyller kravspecifikationen för att få testet att passera (Green), och slutligen förbättrar man koden utan att ändra dess beteende eller funktionalitet (Refactor). 
___


### Fråga 3:Beskriv hur BDD skiljer sig från TDD.
BDD skiljer sig från TDD genom att fokusera på systemets beteende ur ett användarperspektiv, för att säkerställa att det möter verksamhetens och användarnas behov.  
BDD använder användarberättelser och scenarier skrivna i ett naturligt, strukturerat språk enligt formatet Given, When, Then, istället för tekniska testfall som i TDD.  
BDD formatet gör att både tekniska och icke-tekniska intressenter kan förstå och samarbeta kring testfallen. 
TDD är tekniskt orienterat och fokuserar på att verifiera att enskilda kodfunktioner fungerar korrekt tekniskt.Testerna skrivs av och för utvecklare och beskriver hut koden ska fungera på en tekniks nivå.


___


### Fråga 4:Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt val.
Jag skulle vilja använda en kombination av enhetstester, integrationstester, end-to-end-tester och regressionstester för att säkerställa att både frontend och backend fungerar korrekt och att användarupplevelsen är smidig och stabil. 

**Enhetstester** för att testa enskilda funktioner i backend, till exempel logiken för att lägga till eller ta bort böcker. Det är ett enkelt sätt att snabbt hitta fel tidigt i utvecklingen.  

**Integrationstester** för att kontrollera att frontend och backend pratar med varandra på rätt sätt, till exempel att ett API-anrop faktiskt hämtar rätt data från databasen.

**End-to-end-tester (E2E)** för att simulera hur en riktig användare använder applikationen, till exempel att logga in, lägga till en bok och sedan ta bort den. Här skulle jag använda ett verktyg som Playwright.

**Regressionstester** för att upptäcka snabbt verifiera om något slutar fungera efter en uppdatering.

Jag skulle prioritera **enhetstester** och **integrationstester** och sedan komplettera med **E2E-tester** för de viktigaste flödena i applikationen. 
