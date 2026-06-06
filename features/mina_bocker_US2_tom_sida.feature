Feature: Tom sida när inga favoritböcker har markerats

Scenario: Inga favoriter markerade - tom lista visas
    Given användaren är på sidan "Mina böcker"
    When att inga böcker är markerade som favoriter i katalogen
    Then ska favoritlistan vara tom