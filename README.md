# Challenge: Unit Testing

This repository contains an answer to an exercise to practice Unit Testing
in Python. The exercise is part of a training program at
[BeCode](https://becode.org/) Antwerp.

## Notes:

* The repository is still _under construction_.
* Currently, it just contains the instructions and the code to test.
* The provided instructions for the challenge are copied below.
* The provided code to test can be found in [`utils/challenge.py`](./utils/challenge.py)

## The instructions

> Below you can find the instructions as they were provided.

![Tests!](https://media.giphy.com/media/gw3IWyGkC0rsazTi/giphy.gif)

Let's partice now!

- Repository: `unit-testing`
- Type of Challenge: `Learning`
- Duration: `1 days`
- Deadline: `dd/mm/yy H:i AM/PM`
- Team challenge : `solo`

### Learning Objectives
You will learn how to take advantage of unit testing to create robust code.
At the end of the challenge, you will be able to:
- Test your code with the `assert` python keyword
- Test your code with the `unittest` module
- Test your code with `pytest` module
- Use Mock objects
- Use other features from `pytest`

### The Mission
You work for a company working in Python. Your customer complains that
your code crashes a lot and they're not able to access your services
half of the time.

You see all the seniors of your company debugging all day and being mad
at their colleagues breaking the code everytime they want to add a feature.

Your project manager asks you to write unit tests to fix the problem.

### Must-have features
- All the functions have to get at least one test.
- Use the Mock object
- Use `pytest` at least once

### Nice-to-have features
- Folow pep8 rules.
- Add a docstring for each test.
- Add type hinting for all your tests.
- Use `Black` to format your code.
- Use `pytest` for all your tests
- Try to mix `pytest` and `unittest`
- Create your own [fixture](https://www.tutorialspoint.com/pytest/pytest_fixtures.htm)
- Use [parametrization](https://docs.pytest.org/en/latest/parametrize.html#:~:text=pytest%20enables%20test%20parametrization%20at%20several%20levels%3A%20pytest.fixture%28%29,one%20to%20define%20custom%20parametrization%20schemes%20or%20extensions)

### Deliverables
1. Publish your source code on the GitHub repository.
2. Pimp up the readme file:
	- What, Why, When, How, Who.
	- Pending things to do
3. All the unit tests should pass
4. `connect_to_db()` function should be mocked to not raise an error when testing `get_users_list_from_db()`

### Evaluation criterias
| Criteria       | Indicator                                                                             | Yes/No |
|----------------|---------------------------------------------------------------------------------------|--------|
| 1. Is complete | The student has realized all must-have features.                                      |        |
| 2. Is Correct  | The code has been formated using Black.                                               |        |
| 3. Is clean    | There is a test for each function with pytest                                         |        |
|                | Each test is typed                                                                    |        |
|                | The student created his/her own fixture                                               |        |
|                | The student used [parametrization](https://docs.pytest.org/en/latest/parametrize.html#:~:text=pytest%20enables%20test%20parametrization%20at%20several%20levels%3A%20pytest.fixture%28%29,one%20to%20define%20custom%20parametrization%20schemes%20or%20extensions.)                                                                    |        |
