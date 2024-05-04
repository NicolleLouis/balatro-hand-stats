## Analysis

You can read the analysis in the analysis directory, following the description.md file.
Here is a summary

- [Discard vs Hand size](analysis/chapter_1/description.md)
- [Base vs Erratic Deck](analysis/chapter_2/description.md)
- [Impact of STC (Suit-change Tarot Card)](analysis/chapter_3/description.md)

## How to use:

Create a ProbabilityComputer with the following options:
- Deck: A base deck (You can create a new one in the Deck directory)
- Engine: An engine used to simulate player decisions, it has both a goal and a discard policy
- GameSettings: The meta settings of the game (discard number and number of cards in hand especially)

run computer.run() to get the results. 

Enjoy!

## Current Ideas:

- Impact of a suit changing tarot card on flushes
- Implement the suite engine
- Impact of the abandoned deck on the suite stats
- Multiple hand probability
