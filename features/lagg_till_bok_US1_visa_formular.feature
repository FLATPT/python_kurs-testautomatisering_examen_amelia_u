Feature: Visa formulär för att lägga till en ny bok

Scenario: Formuläret visas när användaren klickar på Lägg till bok
    Given att användaren är på sidan Läslistan
    When användaren klickar på "Lägg till bok"
    Then ska ett formulär med fält etiketten "Titel" och "Författare" visas
    And ska knappen med texten"Lägg till ny bok" visas