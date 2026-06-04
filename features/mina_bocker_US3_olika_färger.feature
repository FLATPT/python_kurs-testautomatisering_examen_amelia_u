Feature: Rader visas i olika färger i Mina böcker

  Scenario: Alternerade radfärger visas i listan
    Given att användaren har minst två favoritböcker
    When användaren klickar på fliken "Mina böcker"
    Then ska udda rader ha en ljusare bakgrundsfärg
    And ska jämna rader ha en mörkare bakgrundsfärg