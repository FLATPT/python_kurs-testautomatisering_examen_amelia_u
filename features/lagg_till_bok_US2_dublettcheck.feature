Feature: Felmeddelande saknas vid tillägg av bok som redan finns i katalogen

Scenario: Användaren försöker lägga till en bok som redan finns i katalogen
    Given Användaren är på Lägg till bok-sidan
    And att katalogen innehåller boken "Why Your Tests Are Lying to You" av "Kent Backdoor"
    When användaren fyller i "Titel" med "Why Your Tests Are Lying to You"
    And användaren fyller i "Författare" med "Kent Backdoor"
    And användaren klickar på "Lägg till ny bok"-knappen
    Then boken "Why Your Tests Are Lying to You" sparas i katalogen igen
    And felmeddelande om att boken redan finns i katalogen visas inte
