Feature: Välkomstmeddelande på Katalog sidan

Scenario: Välkomstmeddelande visas när användaren är på Katalog-knappen
    Given Användaren är på hemsidan Läslistan
    When Katalog-knappen är inaktiverad
    Then Användaren är på Katalog-sidan
    And ett välkomstmeddelande visas på skärmen