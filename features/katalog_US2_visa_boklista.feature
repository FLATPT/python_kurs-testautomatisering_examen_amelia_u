Feature: Visa boklista i katalogen

Scenario: Boklistan visas när användaren klickar på Katalog knappen
    Given Användaren är på Läslistan
    When Användaren klickar på Katalog
    Then ska boklistan visas på skärmen
    And varje rad innehåller titel och forfattare information

