Feature: Visa lista på favoritböcker

Scenario: Välkomstmeddelande och favoritlista visas
    Given användaren är på sidan "Mina böcker"
    And att användaren har markerat minst en bok som favorit i katalogen
    Then ett välkomstmeddelande visas på skärmen
    And en ordnade lista över favoritböcker visas