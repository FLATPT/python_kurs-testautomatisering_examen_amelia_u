Feature: Rader ändrar färg vid mouseover

Scenario: En rad ändrar färg när musen förs över den
    Given att Katalog-sidan visar en lista av böcker
    When användaren för musen över en rad i boklistan
    Then raden ändrar bakgrundsfärg för att indikera att den är markerad

