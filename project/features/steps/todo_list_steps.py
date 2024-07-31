to_do_list = {}
#Scenario: Add a task
# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
# Set the to-do list as an empty list
    global to_do_list
    to_do_list = {}
# Step 2: When the user adds a task "Buy groceries"
@when('the user adds a task "{task}"')
def step_impl(context, task):
# Add the task to the to-do list
    global to_do_list
    to_do_list.append(task)
# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    # Check if the task is in the to-do list
    assert task in to_do_list, f'Task "{task}" not found in the to-do list'
