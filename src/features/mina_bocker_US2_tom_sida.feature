Feature: Tom sida när inga favoritböcker har markerats

Scenario: Inga favoriter markerade - tom lista visas
    Given att inga böcker är markerade som favoriter i katalogen
    When användaren klickar på fliken "Mina böcker"
    Then ska favoritlistan vara tom