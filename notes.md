# Python Practice Notes

## Day 1
- Wrote first grade checker
- Input, output, conditional statements
- Learned why repeated variables are annoying

## Day 2
- Added validation for age, year, and grades
- Added comments for clarity
- Nested conditionals felt painful → loops soon
- **Time spent:** about 1 hour

## Day 3
- I did this at 1am of Day 4 because I got too busy today.
- Wrote the code from scratch
- Added validation for age, year, and grades
- Nested conditions are starting to annoy me.
- Made a clear summary of the grades.
- Computed the average and its letter equivalent.
- Included the name in the summary.
- **Time spent:** about 20-30 minutes

## Day 4
- About Conditionals, Input, Validation, and Grading Logic
- Rewrote the code from memory from scratch
- Added isalpha() for name validation to ensure the name variable is alphabet characters.
- Wanted to use isinstance ([grade], int) but it's too painful to implement for each variable. I'll do it when I get to dictionaries and functions. Perhaps it should be a separate method?
- Executed all printing of the summary in one block.
- **Time spent:** Approximately 28 minutes, 02.2 seconds.

## Day 5
- Focused heavily on input validation and user experience.
- Rewrote the program with stricter checks using is digit() before converting inputs to integers to avoid ugly runtime errors.
- Validated name, age, year level, and all grades step by step.
- Improved the grading logic to handle:
  - passing all subjects
  - passing overall average but failing specific subjects (retakes)
  - completely failing
- Added logic to explicitly list failed subjects instead of giving a vague result.
- This made the program feel more human and less “computer says no.”
- Realized how repetitive validation becomes without loops and functions — pain is now very obvious.
- Occasional Googling, but most of the work was reasoning and logic.
- **Time spent:** Approximately 00:52:45.775.

## Day 6
- Built the most complete version so far: name, age, year level, five subjects, average, pass/fail, and retake logic.
- Implemented full validation using:
  - `isalpha()` for names
  - `isdigit()` for all numeric inputs before casting
  - Range checks for age, year level, and grades
- Prevented ugly runtime errors caused by invalid user input.
- Added logic to:
  - pass only if the average **and** all subjects are ≥ 75
  - allow passing with retakes if the average is ≥ 75 but one or more subjects are below
  - list exactly which subjects need to be retaken
- Made the program communicate clearly with the user instead of just rejecting input.
- Code became deeply nested — readability is starting to suffer.
- This made it extremely clear why:
  - loops exist (retry instead of restart)
  - functions exist (validation logic is screaming to be reused)
- Started thinking in terms of *system behavior* and *user experience*, not just syntax.
- This stage is repetitive, but the logic is finally clicking.
- **Time spent:** 39 minutes, 41.89 seconds.

## Day 7
- First tried loops.
- started with while loops.
- Started streaming on twitch to build confidence. Struggled, lmao.
- Had a clearer mind when streaming was stopped and had a lunch break.
- Felt better, understood better.
- In while loops, you define what is wrong. While it's still wrong, do the code. If correct, do the code at the end.
- Infinite loops are annoying, lmao
- If an infinite loop happens, ask for another user input.
- **Time spent:** Did not record time because it took so much time, lol.

## Day 8
- Completely rewrote Day 7 from memory.
- Tried completely grasping the while loops.
- **Time spent:** Not recorded; at school.

## Day 9
- Applied all the learnings from Day 7 and 8 to ask for multiple inputs with while loops.
- Asked for name, age, and three subjects with validation.
- Displayed the summary of grades, and the rounded average.
- **Time spent:** 22:58.61