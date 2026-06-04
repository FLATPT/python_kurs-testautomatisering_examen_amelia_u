Feature: Välkomstmeddelande på katalogfliken

Scenario: Välkomstmeddelande visas när användaren klickar på Katalog
    Given Användaren är på Läslistan
    When Användaren klickar på Katalog-fliken
    Then Ett välkomstmeddelande visas på skärmen