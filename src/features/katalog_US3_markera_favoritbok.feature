Feature: Markera favoritbok med hjärtikon

Scenario: Användaren markerar en bok som favoriter
    Given att katalogen visas med en lista av böcker
    Adn boken ""The Bugs are Coming"" inte är markerad som favorit
    When Användaren klickar på raden där "The Bugs are Coming" står på listan
    Then ett hjärtikon visas bredvid "The Bugs are Coming" i boklistan
    Adn markerar på så sätt boken "The Bugs are Coming" som favorit
