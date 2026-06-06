Feature: Markera favoritbok med hjärtikon

Scenario: Användaren markerar en bok som favoriter
    Given att en boklista lista visas på Katalog-sidan
    And boken "The Bugs are Coming" inte är markerad som favorit
    When Användaren klickar på raden där "The Bugs are Coming" finns på listan
    Then ett hjärtikon visas bredvid "The Bugs are Coming" i boklistan
    And markerar på så sätt boken "The Bugs are Coming" som favorit
