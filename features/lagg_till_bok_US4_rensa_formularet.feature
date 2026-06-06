Feature: Formuläret återställs efter att en bok har lagts till

Scenario: Formuläret rensas när en bok har lagts till
    Given Användaren är på Lägg till bok-sidan
    And Användaren filler i titel och författare i formuläret
    When användaren klickar på knappen "Lägg till ny bok"
    Then boken sparas i katalogen
    And Formuläret rensas/återställs så att fälten "Titel" och "Författare" är tomma