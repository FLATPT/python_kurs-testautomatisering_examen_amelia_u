Feature: Listan uppdateras när en bok markeras eller avmarkeras som favorit

Scenario:  En ny bok läggs till i listan när den markeras som favorit
    Given Användaren är på Katalog-sidan
    And boken "Python för folk som hatar ormar" inte är markerad som favorit
    When användaren markerar "Python för folk som hatar ormar" som favorit
    And användaren navigerar till fliken "Mina böcker"
    Then boken "Python för folk som hatar ormar" visas i favoritlistan


Scenario: En bok försvinner från listan när favorit avmarkeras
    Given Användaren är på Katalog-sidan
    And att boken "Python för folk som hatar ormar" är markerad som favorit
    When användaren avmarkerar "Python för folk som hatar ormar" som favorit
    And användaren navigerar till fliken "Mina böcker"
    Then ska "Python för folk som hatar ormar" inte visas i favoritlistan