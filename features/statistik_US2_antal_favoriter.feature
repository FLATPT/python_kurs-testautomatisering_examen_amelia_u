Feature: Visa statistik över antal favoritböcker

  Scenario: Antal favoritböcker visas korrekt på statistiksidan
    Given att 2 böcker är markerade som favoriter i katalogen
    When användaren är på sidan "Statistik"
    Then ska texten "Våra användare har hjärtmarkerat 2 böcker." visas på sidan