
### Introduction
- Coming up with the solution is not the end goal. It would be good to identify solutions that are not optimal and self-criticize.
- Short presentation will introduce different tools, or the same tool with different aspects.
- Final research project will have three milestones where we will incrementally develop it.
- MEng: Need to look into solutions, papers, and more on the tools and implementations. Something that can be published with a bit of innovation, but can't be something that's pulled off of GitHub. Understand and present it.
- Main textbook: Metaheuristics: From Design to Implementation
- Presentation: 
	- Discuss from reading material. 
	- Discuss one/two paper related. Demo one tool that will address topic in discussion. Core idea is to present tools that can be used by project or others. Not innovation. Gathering info and analyzing to show how tool works. More like getting understanding of whole thing so that everyone can learn about the tools and such.
	- Problem statement should mention whether we are trying to maximize or minimize something. Minimization or maximization problem.
- Project:
	- Three submissions
		- Page summary that is approved by the professor - 5 marks
			- Title
			- Write the major
			- Problem Statement
			- Abstract
			- IEEE paper that is 9 pages long + reference. Not more, not less.
			- Use Overleaf
			- Few reference works
			- Don't just come up with a tool that exists. Enhance something. 
			-  Problem statement should mention whether we are trying to maximize or minimize something. Minimization or maximization problem.
		- Project checkpoint submission - 5 marks
			- Project paper draft (Introduction, Related work, New papers, challenges)
			- Submit at least 5 pages by this point.
			- More references
			- Make sure all comments posted by the prof are addressed at this point. If not, it will impact the final submission grade.
			- Mention challenges you have to solve
		- Project final package - 20 marks
			- Demo presentation
			- 10 page submission by the end.
			- Final paper (IEEE conference format 12pt font as pdf)
			- Group member evaluation (Individual submission)

### Problem Statement
- Identify the problem
- The goal
- Start by mentioning the gap
- And the objectives
- What is not there, and if it is there, why is it not efficient? Any number put in any context must be supported with reference.
- Don't say it doesn't exist or no work has been done. We have not yet found a solution.

### EXAM
- Prof might remove/change parts of code he's given us and ask us to change it/fix it.
- He might as us to do pseudocode or create a flow chart.
- If prof provides an extra bit, positive and negative, what are the two solutions we get instead of just one?

### Next submission
- Explain why we chose PSO & GA for each problem or area.


### Genetic Algorithm
	- Population of Solutions
	- Fitness Evaluation
	- Selection
	- 

### What is Optimization?
- Whatever problem you are trying to deal with, the goal is to get the best result out of it.
- Simplest example is a bucket that you are trying to fill up. What is the fastest way to fill up the bucket in the most optimal way. 
- If you have a car weighing 100lbs, and you need it to go from 0 to 100 in three seconds. What is the easiest solution? 
	- What is the simplest change you can make to a variable to make the car run faster?
		- Reduce its weight
- The core idea of optimization is creating a model that can be replicated.
	-  For example when testing different weights of a car, there is a model/simulation to test it ahead of time.
	- Any model has a mathematical formula that can be used to simulate/optimize a solution.
- Choosing the inputs that will result in the best possible outputs or making things the best they can be.
	- Allocate resources
	- Design solutions
	- Choosing control variables for best desired outcome
- Optimization problem eg.
	- Given a parabola choose x to get the maximum y.
		- Choose various values of x until the max value is identified.
			- This method of guessing and checking can take too long, especially for complex models.
		- Optimization algorithms can be applied
- Are we trying to maximize something or minimize something.
- Optimization is changed to different terms. The latest is:
	- fine-tuning
- If a horse race is being optimized where slowest horse is the winner. These will be the same criteria (coefficient) as with the fastest horse, but we would be evaluating different values. Same but in opposite direction.
	- Past performance and other details about the Jockey
	- Past performance and fitness of the horse
	- Breed of the horse
- First define objective functions, then define constraints to create a well defined problem and the solution being considered.
	- ***Objective functions*** are those that we are trying to maximize or minimize. 
	- ***Constraints***
Dictionary of optimization problems
- ***Objective function***: are those that we are trying to either maximize or minimize. 
- ***Mathematical/Simulator/Experimental***: 
	- ***Math***: A method that uses **mathematical models and equations** to represent, analyze, and solve problems.
	- ***Simulation***: A method that uses **computer programs to imitate real-world systems** to study their behavior under various conditions.
	- ***Experimental***: A method that involves **testing through real-world trials or lab experiments** to observe and collect data.
- ***Black-box/grey box problem***:
	- ***Black-box***: A problem where the **internal workings are completely unknown or inaccessible** — you can only observe **inputs and outputs**.
	- ***Grey-box***: A problem where **some internal information is available**, but **not fully** — partial transparency.
- ***Constraint, box-constraint***:
	- ***Constraint***: A **rule or condition** that limits the set of feasible solutions in an optimization problem. Equality constraint, inequality constraint.
	- ***Box-constraint***: A special type of constraint that limits each variable to a **range (a “box”)**. Upperbound, lowerbound.
- ***Minimization/Maximization***:
	- Minimization: Find the input x that gives the **lowest** value of an objective function f(x).
	- Find the input x that gives the **highest** value of an objective function f(x).
- ***Static/Dynamic***:
	- A **static** problem/system does **not change over time**. All data and parameters are fixed.
	- A **dynamic** problem/system evolves **over time**, often with feedback or changing conditions.
- ***Dimension***:
	- 
- ***Noisy***:
- ***Large-scale***:
- ***Single- or Multi-level***:
- ***Landscape***:
- ***Deceptive***:
- ***Discrete/continuous/mixed-type***:

Look into how AI models can be optimized under the hood. Not just training the model with more data and showing that it is optimal because it is better trained.
