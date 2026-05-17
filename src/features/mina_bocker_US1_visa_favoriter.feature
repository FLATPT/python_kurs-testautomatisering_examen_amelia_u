Feature: Visa lista på favoritböcker

Scenario: Välkomstmeddelande och favoritlista visas
    Given att användaren har markerat minst en bok som favorit i katalogen
    And användaren är på sidan "Mina böcker"
    Then ska ett välkomstmeddelande visas
    And ska en ordnade lista över favoritböcker visas