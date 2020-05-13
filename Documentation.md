# ROS Assignment 2
### ROS Point&Shoot and Servoing by Sean Sminia and Ray Mindiola



### 1 - Logic

#### Point&Shoot
1. Determine goal
2. Determine current position
3. Calculate vector angle to desired goal
4. Rotate to target angle until within a precise threshold
5. Calculate distance between goal and robot
6. Move forward until distance is within a precise threshold
7. Calculate desired goal angle
8. Rotate until current orientation matches goal orientation
9. End operation and await new goal

### 2 - Results

#### point&Shoot
The robot follows the logic described herebove.By following these steps the robot gets to the end goal. The angular velocity is not regulated, as such the robot appears to be twitching when trying to align itself in the right angle. This causes the robot to sometimes have to attempt multiple tries at rotating before it aligns itself. The same issue persists for the end rotation. The lineair movement stops only is the distance is within a certain bounds. This means  

#### Servoing

 
### 3 - Limitations / Errors

### 4 - Video

