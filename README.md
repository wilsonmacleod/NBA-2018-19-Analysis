# NBA-2018-19-Analysis

Analysis of various facets and storylines of the 2018-2019 NBA regular season using numpy, pandas, matplotlib and seaborn.

All data is courtesy of [Basketball Reference](https://www.basketball-reference.com/) unless otherwise noted.

## CONTENTS:
- MVP RACE 2019
- Consitency is key (coming soon)
- Bestbrook or Worstbrook? (coming soon)
- Player "Portability" (coming soon)
- NBA Trends (coming soon)
- The Veteran Effect (coming soon)
- Keys to team success (coming soon)
- Most Improved Player(s)

## MVP RACE 2019
 
### Introduction:

As the 2018-2019 NBA regular season winds down (2 days left) the MVP race is looking like a two-horse race. **James Harden** and **Giannis Antetkounmpo** are pretty far out ahead of the pack and the general consensus is that one or the other will end up winning the NBA's most prestigious individual award. I wanted to see if I could find any blatant statistical, both "normal" and advanced, advantages for either side. And, while the end winner of the award usually comes to narrative or media/fan favoritism, see if I could determine statistically who should win based purely on the measurables.

### Harden's Insane Usage Rate:

The first thing that stood out to me in this race is the amount each player is being asked to do by their team. Usage rating is determined by the amount of possessions "used" by a player during their time on the floor, this means anytime the teams possession ends with the player:
- Attempting a field goal 
- Shooting Free-throws 
- Turning the ball over. 

The Rockets lean heavily on Harden each and every game, over 40% of their plays while he is on the floor end with a Harden action. He is also 2nd in the league in Minutes Played indicating  he gets very few games/quarters off unlike Giannis who is often sitting for most 4th quarters. When paired with his massive lead in usage it's even more obvious how much the Rocket's rely on Harden.

![alt text](https://github.com/wilsonmacleod/NBA-2018-19-Analysis/blob/master/MVP_Race/figs/TotalMinsUsage.png)

(Players with <500 minutes played (~10 full games) were not included in the figure as there are some meaningless high usage ratings in there (read garbage time chuckers.))

Given Harden's unheard of usage rate and his heavy minutes load, his scoring efficiency and shooting must be suffering right? Wrong. True Shooting Percentage (TS%) is a stat that factors and weighs 2 point shots, 3 point shots and free throws and aims to gauge a players true efficiency at scoring the ball. Harden is currently leading the league in points per game by a sizable margin while maintaining a shooting efficiency  that is above the leagues other leading scorers. Giannis is no slouch in this department either being tied for the lead in TS% for players above 20 points per game while not shooting threes.

![alt text](https://github.com/wilsonmacleod/NBA-2018-19-Analysis/blob/master/MVP_Race/figs/ScoringTS.png)

This sustained performance despite hefty load is also evident in the two's PER scores. PER is Player Efficiency Rating, PER strives to measure a player's per-minute performance, while adjusting for pace.

![alt text](https://github.com/wilsonmacleod/NBA-2018-19-Analysis/blob/master/MVP_Race/figs/PERvUSG.png)
### The Ying and The Yang

So what are the keys to these two superstars offensive games? Getting to the line! Both Dominant the game scoring wise in their own ways, Giannis in the paint (2 pointers) and Harden from Three (only Steph Curry has him beat in makes per game.) But the thing they both have in common is they attempt and make free throws at a very high clip.

![alt text](https://github.com/wilsonmacleod/NBA-2018-19-Analysis/blob/master/MVP_Race/figs/ScoringRoots.png)

Harden leads the league in free throws attempted and made per game, but is this a product of flopping? Skill? Favoritism from the refs? Free throw rate is the number of free throw attempts per field goal attempt. While Harden is getting to the line with more volume than the rest of the league this may be down to his crazy usage rating and the volume of shots he is taking. Giannis and Joel Embiid are actually getting to the line at a higher rate per field goal attempt.

![alt text](https://github.com/wilsonmacleod/NBA-2018-19-Analysis/blob/master/MVP_Race/figs/FreeThrowRate.png)

### The "Other" Side of The Ball

Defensive impact is very hard to quantify even using advanced stats and lets be honest the MVP award is rarely decided on the defensive side of the ball. Giannis dominates the defensive boards and blocks a good amount of shots while Harden gets steals at a suprising rate.

![alt text](https://github.com/wilsonmacleod/NBA-2018-19-Analysis/blob/master/MVP_Race/figs/generalDEF.png)







