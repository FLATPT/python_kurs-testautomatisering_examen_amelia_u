Feature: Felmeddelande vid tomma fält

Scenario:  Användaren skickar formuläret utan titel
    Given att användaren är på fliken "Lägg till bok"
    When användaren fyller i "Författare" med "Kent Backdoor"
    And användaren klickar på "Lägg till ny bok"
    Then ska ett felmeddelande visas om att fältet "Titel" inte får vara tomt
    And ska boken inte läggas till i katalogen

Scenario:  Användaren skickar formuläret utan författare
    Given att användaren är på fliken "Lägg till bok"
    When användaren fyller i "Titel" med "Why Your Tests Are Lying to You"
    And användaren klickar på "Lägg till ny bok"
    Then ska ett felmeddelande visas om att fältet "Författare"