Feature: Visa boklista i katalogen

Scenario: Boklistan visas när användaren är på Katalog-sidan
    Given Användaren är på hemsidan Läslistan
    When Användaren är på Katalog-sidan
    Then en boklistan visas på skärmen


