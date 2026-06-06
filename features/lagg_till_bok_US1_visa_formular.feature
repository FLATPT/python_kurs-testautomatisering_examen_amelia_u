Feature: Visa formulär för att lägga till en ny bok

Scenario: Formuläret visas när användaren klickar på Lägg till bok
    Given Användaren är på hemsidan Läslistan
    When Användaren klickar på Lägg till bok-knappen
    Then formulär med fält etiketten "Titel" och "Författare" visas
    And knappen med texten "Lägg till ny bok" visas