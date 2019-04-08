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

As the 2018-2019 NBA regular season winds down (2 days left) the MVP race is looking like a two-horse race. **James Harden** and **Giannis Antetkounmpo** are pretty far out ahead of the pack and the general consesus is that one or the other will end up winning the NBAs most prestigious individual award. I wanted to see if I could find any blatant statiscal, both "normal" and advanced, advantages for either side. And, while the end winner of the award usually comes to narrative or media/fan favoritism, see if I could determine statiscally who should win based purely on the measurables.

### Harden's Insane Usage Rate:

The first thing that stood out to me in this race is the amount each player is being asked to do by their team. Usage rating is determined by the amount of possessions "used" by a player during their time on the floor, this means anytime the teams possesion ends with the player:
- Attempting a field goal 
- Shooting Free-throws 
- Turning the ball over. 

The Rockets lean on Harden heavily each and every game, over 40% of their plays while he is on the floor end with a Harden action. He is also 2nd in the league in Minutes Played indicating  he gets very few games/quarters off unlike Giannis who is often sitting for most 4th quarters. When paired with his massive lead in usage it's even more obvious how much the Rocket's rely on Harden.

![alt text](https://raw.githubusercontent.com/wilsonmacleod/NBA-2018-19-Analysis/master/MVP_Race/figs/TotalMinsUsage.png?token=Ar6DDJyz9tbmFXb5yDDy6AWgFU3UXX5rks5cq56awA%3D%3D)

(Players with <500 minutes played (~10 full games) were not included in the figure as there are some meaningless high usage ratings in there (read garbage time chuckers.))

Given Harden's unheard of usage rate and his heavy minutes load, his scoring efficiency and shooting must be suffering right? Wrong. True Shooting Percentage (TS%) is a stat that factors and weighs 2 point shots, 3 point shots and free throws and aims to gauge a players true efficiency at shooting the ball (all kinds of shots)

## Figure for MPG, TS, USAGE








