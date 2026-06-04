Feature: Formuläret återställs efter att en bok har lagts till

Scenario: Formuläret rensas när en bok har lagts till
    Given att användaren är på fliken "Lägg till bok"
    And att formuläret innehåller titel och författare
    When användaren klickar på knappen "Lägg till ny bok"
    Then boken sparas i katalogen
    And formuläret rensas/återställs så att fälten "Titel" och "Forfattare" är tomma