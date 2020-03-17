# reinforcement-learning-basics

TLDR:
* Basic demonstration an comparison of Q-Learning and SARSA
* Small repo I intend to use as a basic cheat-sheet for OpenAI Gym projects (or even any similar Reinforcement Learning problem)


---


Q-Learning and SARSA are two of the most popular Reinforcement Learning Algorithms.

I had to compare them while solving a simple problem (Grid World), following [this medium post](https://towardsdatascience.com/reinforcement-learning-implement-grid-world-from-scratch-c5963765ebff), for a college assignment.

I decided to leave this repo as a mini-guide for whenever I want to revisit this subject and play around introducing some minor changes or maybe completely different algorithms.


I structured this small project in a way similar to [OpenAI Gym's API](https://gym.openai.com/docs/), so I can also use this repository as a basic cheat-sheet for when I am working with framework.

---

## Problem - Grid World

A simple problem often used in this context. We have a grid and start is a given cell. 
* Our goal is to reach a certain position (which will return a positive reward).
* Stepping on some cells make us lose (negative reward).
* There are some obstacles.

I first solved the problem for a very simple configuration (same as in the medium post linked above), and then implemented an abstraction of it (grid_world.py) in order to study the convergence of the algorithms in more complex configurations.

---

## Results
