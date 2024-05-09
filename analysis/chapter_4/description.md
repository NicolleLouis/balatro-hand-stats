# Straight Analysis

## Intro 

- We are going to compare the probability of Straight and Flushes. 
- We are going to refine the StraightEngine and see how we can bolster it's efficiency

## First Engine

The first engine is fairly naive. It looks at each possible series of 5 value that make a straight.
Those series are: Ace/2/3/4/5 -> ... -> 10/Jack/Queen/King/Ace.
For each of those 'locations' it count the number of card already present. And then pick the most full one. 
It doesn't care for now for any cards in the deck or the order of the cards. 4 cards in a row vs 2 and 2 + a hole seems
equally good to him.

First results:

> Probability: 78.5%

![engine-1](engine-1.png)

## Second Engine

In order to test the new improvement we are going to switch to the abandoned deck.
This is the deck without any face cards.
It's also the deck with which we tend to go with straight. 

The main difference for this deck is that now, there are straights that become impossible
(All those including a face card. So 7/8/9/10/Jack for example).
We are going to teach the engine to avoid those locations in its computation.

Before improvement, the results for the abandoned deck are: 

> Probability (Abandoned) : 90,5%

![engine-1_abandoned](engine-1_abandoned.png)

We are also trying on the erratic deck, instinctively, when this deck's variance was impacting positively the flushes
it will probably be negative for the straight. 

> Probability (Erratic): 65%

![engine-1_erratic](engine-1_erratic.png)

Let's see how forbidding the impossible location security improve those performances.

