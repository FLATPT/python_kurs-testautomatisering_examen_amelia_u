Feature: Formuläret sparas inte vid tomma fält

Scenario: Användaren skickar formuläret utan titel
    Given Användaren är på Lägg till bok-sidan
    When användaren fyller i "Författare" med "Kent Backdoor"
    Then Lägg till ny bok-knappen ska vara inaktiverad


Scenario:  Användaren skickar formuläret utan författare
    Given Användaren är på Lägg till bok-sidan
    When användaren fyller i "Titel" med "Why Your Tests Are Lying to You"
    Then Lägg till ny bok-knappen ska vara inaktiverad