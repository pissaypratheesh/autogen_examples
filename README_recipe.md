# Autogen Recipe Example

 Initially, we are giving AUtoGen agent a small list of task to do (generic system design steps)

1. Task 1: Generate functional and non-functional requirements for a company's backend system design .
2. Task 2: Calculate Requests Per Second, storage, and bandwidth requirements for 1 billion Daily Active Users (DAUs) .
3. Task 3: Provide a high-level design (HLD) with a detailed data flow using the latest technologies .
4. Task 4: Create an Entity-Relationship (ER) diagram with a detailed database schema, sample APIs, and major services.
5. Task 5: Explain the low-level design of critical services and possible algorithms.
6. Task 6: List all possible single points of failure and their solutions.

### Here we are asking autogen agent to generate a recipe
7. Task 7: Reflect on the sequence and create a recipe containing all the above steps. Suggest well-documented, generalized Python functions to perform similar tasks for coding steps in the future.


After this, we will create another task using the above recipe to run a generic system design task by running: `python system_design_recipe.py --deisgn="netflix backend"`
