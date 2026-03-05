import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

# Preview data
print("Matches Dataset")
print(matches.head())

print("\nDeliveries Dataset")
print(deliveries.head())

# -----------------------------
# 1. Teams with Most Wins
# -----------------------------

team_wins = matches['winner'].value_counts()

print("\nTeams With Most Wins")
print(team_wins)

plt.figure(figsize=(10,6))
team_wins.plot(kind='bar')

plt.title("Teams With Most IPL Wins")
plt.xlabel("Team")
plt.ylabel("Number of Wins")

plt.show()


# -----------------------------
# 2. Top Batsmen
# -----------------------------

batsman_runs = deliveries.groupby("batter")["batsman_runs"].sum()

top_batsmen = batsman_runs.sort_values(ascending=False).head(10)

print("\nTop Batsmen")
print(top_batsmen)

plt.figure(figsize=(10,6))
top_batsmen.plot(kind="bar")

plt.title("Top 10 IPL Batsmen")
plt.xlabel("Player")
plt.ylabel("Total Runs")

plt.show()


# -----------------------------
# 3. Top Bowlers
# -----------------------------

wickets = deliveries["player_dismissed"].dropna().value_counts()

top_bowlers = wickets.head(10)

print("\nTop Bowlers")
print(top_bowlers)

plt.figure(figsize=(10,6))
top_bowlers.plot(kind="bar")

plt.title("Top 10 Bowlers by Wickets")
plt.xlabel("Bowler")
plt.ylabel("Wickets")

plt.show()


# -----------------------------
# 4. Toss Impact
# -----------------------------

toss_match_win = matches[matches["toss_winner"] == matches["winner"]]

percentage = (len(toss_match_win) / len(matches)) * 100

print("\nToss Winner Match Win Percentage:")
print(round(percentage,2), "%")