Feature: Working with todolist

  @addTask
  Scenario: Adding a task
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  @listTasks
  Scenario: List all tasks in the to-do list
    Given the to-do list contains a task "Buy groceries" added today
    When the user lists all tasks
    Then the output should contain "Buy groceries --- {current_date} --- {current_time} --- No realizado"

  @markTask
  Scenario: Mark a task as completed
    Given the to-do list contains a task "Buy groceries" added today
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show "Buy groceries" as completed

  @clearList
  Scenario: Clear the entire to-do list
    Given the to-do list contains a task "Buy groceries" added today
    When the user clears the to-do list
    Then the to-do list should be empty
  
  @markAllCompleted
  Scenario: Mark all tasks as completed
    Given the to-do list contains a task "Buy groceries" added today
    When the user marks all tasks as completed
    Then all tasks in the to-do list should be completed
