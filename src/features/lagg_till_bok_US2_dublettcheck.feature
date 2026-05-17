Feature: Felmeddelande vid tillägg av bok som redan finns i katalogen

Scenario: Användaren försöker lägga till en bok som redan finns i katalogen
    Given att katalogen innehåller boken "Why Your Tests Are Lying to You" av "Kent Backdoor"
    And att användaren är på fliken "Lägg till bok"
    When användaren fyller i "Titel" med "Why Your Tests Are Lying to You"
    And användaren fyller i "Författare" med "Kent Backdoor"
    And användaren klickar på "Lägg till ny bok"
    Then ska ett felmeddelande visas om att boken redan finns i katalogen
    And ska katalogen inte innehålla två exemplar av "Why Your Tests Are Lying to You"