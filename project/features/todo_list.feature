Feature: Working with todolist
  @addTask
  Scenario: Adding a task
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  @listTasks
  Scenario: List all tasks in the to-do list
    Given the to-do list contains
    |Buy groceries --- 2024-06-31 --- 13:45 --- No realizado|
    |Pay bills --- 2024-06-31 --- 13:45 --- No realizado|
    When the user lists all tasks
    Then the output should contain
    |Buy groceries --- 2024-06-31 --- 13:45 --- No realizado|
    |Pay bills --- 2024-06-31 --- 13:45 --- No realizado|

  @markTast
  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
    |Buy groceries --- 2024-06-31 --- 13:45 --- No realizado|
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show "Buy groceries" as completed

  @clearList
  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
    |Buy groceries --- 2024-06-31 --- 13:45 --- No realizado|
    |Pay bills --- 2024-06-31 --- 13:45 --- No realizado|
    When the user clears the to-do list
    Then the to-do list should empty