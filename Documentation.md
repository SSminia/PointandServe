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

#### Servoing
1. Determine distance and angle towards goal
2. Accelerate given a formula, given a set number multiplied by the distance away from the goal and a small addition to prevent slowdown of robot
3. Adjust angular velocity of the robot, by a set number, depending on the difference between robot orientation and the goal
4. Once the robot is within a very close distance of the goal, it will rotate again, to match itself with the goal orientation by comparing itself to it. 
5. Idle until a new goal is given

### 2 - Results

 
### 3 - Limitations / errors

### 4 - Videos

#### Point&Shoot
https://www.dropbox.com/s/bojkjsl3wfkhi2r/Point%26Shoot.mp4?dl=0

#### Servoing
https://www.dropbox.com/s/6g3ch67zjptvth0/Servoing.mp4?dl=0
