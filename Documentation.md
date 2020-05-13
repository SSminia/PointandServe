# ROS Assignment 2
### ROS Point&Shoot and Servoing by Sean Sminia and Ray Mindiola



### 1 - Logic

#### Point&Shoot
1. Determine goal.
2. Determine current position.
3. Calculate vector angle to desired goal.
4. Rotate to target angle until within a precise threshold.
5. Calculate distance between goal and robot.
6. Move forward until distance is within a precise threshold.
7. Calculate desired goal angle.
8. Rotate until current orientation matches goal orientation.
9. End operation and await new goal.

#### Servoing
1. Determine distance and angle towards goal.
2. Accelerate given a formula, given a set number multiplied by the distance away from the goal and a small addition to prevent slowdown of robot.
3. Adjust angular velocity of the robot, by a set number, depending on the difference between robot orientation and the goal
4. Once the robot is within a very close distance of the goal, it will rotate again, to match itself with the goal orientation by comparing itself to it. 
5. Idle until a new goal is given.

#### Ros nodes
The node is named sadness. As the nodes and topics which are needed for the coed do not change between Servoing and point and shoot there is one graph. you can see that the odometry is read and the velocity is sent out.

### 2 - Results

#### Point&Shoot
The robot follows the logic described herebove. By following these steps the robot gets to the end goal. The angular velocity is not regulated, as such the robot appears to be twitching when trying to align itself in the right angle. This causes the robot to sometimes have to attempt multiple tries at rotating before it aligns itself. The same issue persists for the end rotation. Also the rotation direction is not always the shortest. Lineair traveling works only the velocity had to be lowered as the robots orientation can drift if its set to high. Ending the navigation and awaiting a new goal works.

#### Servoing
Sevroing alows the robot to both drive at an angular velocity and a lineair velocity at the same time. As per video evidence this works in our simulation. During servoing both the angular and lilneair velocity are scaled to their difference to their target. What was noticed in this approach is that if a large rotation had to be made, the robot needed a large space to perform its actions as it would be driving at max velocity during the whole rotation. The rotation direction was not always the most efficient. This causes a lot more surface area needed for the robot to navigate. The robot slows dont enough to get to the nav point within threshold. After this robot rotates toward the goal angle. While any actions are performed the robot can be given a new goal and will update its navigation accordingly.
 
### 3 - Limitations

#### Point&Shoot
For the point and shoot, we found that we had to reduce the speed of the robot. If the speed were to be increased the robot would slip. Slipping causes a magnitude of issues, as it would for instance, have the robot miss its goal completely, causing it to endlessly miss the goal and requiering a program restart. 

#### Servoing
For servoing there are a few current issues. The velocity is too high when needing to make a large rotation resulting in more distance to travel. more space and longer travel time. The part of the code that sets which direction to rotate doesn't always rotate in th emost efficient direction. Currently there are a few edge cases in which the robot switches between its rotation direction when driving towards the nav goal. This results in an infinite loop in which the robot tries to rotate but is never aligning itself. Increasing the angular velocity seems to have fixed this edge case but its not known for certain if its completely gone. Another issue is that the end rotation can increase the distance between the robot origin and the nav goal. upon reacvhing the nav goal the robot jitters trying to align itself within the treshold.

### 4 - Videos

#### Point&Shoot
https://www.dropbox.com/s/bojkjsl3wfkhi2r/Point%26Shoot.mp4?dl=0

#### Servoing
https://www.dropbox.com/s/6g3ch67zjptvth0/Servoing.mp4?dl=0
