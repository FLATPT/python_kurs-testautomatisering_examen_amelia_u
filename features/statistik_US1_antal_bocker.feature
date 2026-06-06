Feature: Visa statistik över antal böcker i boklistan

 Scenario: Antal böcker visas korrekt på statistiksidan
    Given att katalogen innehåller 13 böcker
    When användaren är på sidan "Statistik"
    Then ska texten "Listan har 13 böcker." visas
