# CS5950-Project1

Using MapReduce perform some tasks on the Parking Violation and NBC Shot_logs Dataset.

This project contains two parts: Parking and Basketball

**Parking**
Link for the dataset: https://data.cityofnewyork.us/City-Government/Parking-Violations-Issued-Fiscal-Year-2023/pvqr-7yc4
In the dataset, each row represents a parking ticket and the columns are the details of the tickets.

We created a Python program using the MapReduce framework that performs the following 4 tasks by analyzing the parking violation dataset:
1. Printing the times when tickets are most likely to be issued
2. Printing the years and types of cars that are most commonly ticketed
3. Printing the places where tickets are most commonly issued
4. Printing the color of the vehicles that are most likely to get a ticket


**Basketball**
Link for the dataset: https://www.kaggle.com/dansbecker/nba-shot-logs
In the dataset, each row represents a shot and the columns are the details of the shot, e.g. the game ID, who is the defender, what is the distance between them.

There are two tasks in this section:

**Task 1**

We created a Python program using the MapReduce framework to answer the following:

For each pair of the players (A, B), we define the fear sore of A when facing B is the hit rate, such that B is the closest defender when A is shoting. Based on the fear sore, for each player, please find out who is his ”most unwanted defender”.

**Task 2**

We created Python program using multiple rounds of MapReduce to answer the following:

For each player, we define the comfortable zone of shooting is a matrix of, {SHOT DIST, CLOSE DEF DIST, SHOT CLOCK}
Please develop a MapReduce-based algorithm to classify each player’s records into 4 comfortable zones. Considering the hit rate, which zone is the best for James Harden, Chris Paul, Stephen Curry and Lebron James.

