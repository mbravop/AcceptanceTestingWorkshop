from behave import given, when, then
from todo_list import addTask, clearList, listTasks, markTask, get_current_datetime, markAllCompleted

# Contexto global para la lista de tareas
to_do_list = {}
current_date, current_time = get_current_datetime()

@given('the to-do list is empty')
def step_impl(context):
    global to_do_list
    to_do_list = {}

@when('the user adds a task "{task}"')
def step_impl(context, task):
    global to_do_list
    addTask(to_do_list, task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert task in to_do_list, f'Task "{task}" not found in the to-do list'

@given('the to-do list contains a task "{task}" added today')
def step_impl(context, task):
    global to_do_list
    addTask(to_do_list, task)
    global current_date, current_time
    current_date, current_time = get_current_datetime()

@when('the user lists all tasks')
def step_impl(context):
    global to_do_list
    context.output = listTasks(to_do_list)

@then('the output should contain "{expected_output}"')
def step_impl(context, expected_output):
    # Replace placeholders with actual values
    expected_output = expected_output.format(current_date=current_date, current_time=current_time)
    assert context.output == expected_output, f'Expected "{expected_output}", but got "{context.output}"'

@given('the to-do list contains tasks:')
def step_impl(context):
    global to_do_list
    for row in context.table.rows:
        task, date, time, status = row[0].split(' --- ')
        status = 0 if status == "No realizado" else 1
        to_do_list[task] = [date, time, status]

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    global to_do_list
    markTask(to_do_list, task)

@then('the to-do list should show "{task}" as completed')
def step_impl(context, task):
    assert task in to_do_list and to_do_list[task][2] == 1, f'Task "{task}" is not marked as completed'

@when('the user clears the to-do list')
def step_impl(context):
    global to_do_list
    clearList(to_do_list)

@then('the to-do list should be empty')
def step_impl(context):
    assert len(to_do_list) == 0, 'The to-do list is not empty'

@when('the user marks all tasks as completed')
def step_impl(context):
    global to_do_list
    markAllCompleted(to_do_list)

@then('all tasks in the to-do list should be completed')
def step_impl(context):
    for task, details in to_do_list.items():
        assert details[2] == 1, f'Task "{task}" is not marked as completed'
