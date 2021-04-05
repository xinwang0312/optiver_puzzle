# A solution to the optiver puzzle
## The puzzle
Three players A, B, C play the following game. First, A picks a real number between 0 and 1 (both inclusive), then B picks a number in the same range (different from A’s choice) and finally C picks a number, also in the same range, (different from the two chosen numbers). We then pick a number in the range uniformly randomly. Whoever’s number is closest to this random number wins the game. Assume that A, B and C all play optimally and their sole goal is to maximise their chances of winning. Also assume that if one of them has several optimal choices, then that player will randomly pick one of the optimal choices.

1. If A chooses 0, then what is the best choice for B?
2. What is the best choice for A?
3. Can you write a program to figure out the best choice for the first player when the game is played among four players?

## An example output of (3)
First prepare the environment
```
pipenv --python 3.7
pipenv install
```

Then by running
```
pipenv run python solve.py --n 30 --eps 1e-8
```
in a terminal, we have
```
Start to solve the puzzle with n = 30...
Building the game tree...
Optimizing the strategy of D...
Optimizing the strategy of C...
Optimizing the strategy of B...
Optimizing the strategy of A...
The optimal game tree is
AnyNode(win_prob=array([0.29166667, 0.29166667, 0.25      , 0.16666667]))
|--- AnyNode(a=0.16666666666666666, win_prob=array([0.29166667, 0.29166667, 0.25      , 0.16666667]))
    |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, win_prob=array([0.29166667, 0.29166667, 0.25      , 0.16666667]))
        |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, win_prob=array([0.29166667, 0.29166667, 0.25      , 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.2, win_prob=array([0.18333333, 0.33333333, 0.31666667, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.23333333333333334, win_prob=array([0.2       , 0.33333333, 0.3       , 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.26666666666666666, win_prob=array([0.21666667, 0.33333333, 0.28333333, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.3, win_prob=array([0.23333333, 0.33333333, 0.26666667, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.3333333333333333, win_prob=array([0.25      , 0.33333333, 0.25      , 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.36666666666666664, win_prob=array([0.26666667, 0.33333333, 0.23333333, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.4, win_prob=array([0.28333333, 0.33333333, 0.21666667, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.43333333333333335, win_prob=array([0.3       , 0.33333333, 0.2       , 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.4666666666666667, win_prob=array([0.31666667, 0.33333333, 0.18333333, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.5333333333333333, win_prob=array([0.33333333, 0.31666667, 0.18333333, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.5666666666666667, win_prob=array([0.33333333, 0.3       , 0.2       , 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.6, win_prob=array([0.33333333, 0.28333333, 0.21666667, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.6333333333333333, win_prob=array([0.33333333, 0.26666667, 0.23333333, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.6666666666666666, win_prob=array([0.33333333, 0.25      , 0.25      , 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.7, win_prob=array([0.33333333, 0.23333333, 0.26666667, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.7333333333333333, win_prob=array([0.33333333, 0.21666667, 0.28333333, 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.7666666666666666, win_prob=array([0.33333333, 0.2       , 0.3       , 0.16666667]))
            |--- AnyNode(a=0.16666666666666666, b=0.8333333333333334, c=0.5, d=0.8, win_prob=array([0.33333333, 0.18333333, 0.31666667, 0.16666667]))
```