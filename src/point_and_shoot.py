#! /usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
import math
from tf.transformations import euler_from_quaternion, quaternion_from_euler



class PointyPepe: 
    def __init__ (self): 
        rospy.init_node("Sadness")
        self.move_base_goal = rospy.Subscriber("/move_base_simple/goal", PoseStamped, callback=self.Callgoal)
        self.odom = rospy.Subscriber("/odom", Odometry, callback=self.Calldom)
        self.vel = rospy.Publisher("/cmd_vel", Twist, latch=True, queue_size=1)
        self.NavGoal = None
        self.CurPos = None

    def Calldom (self, data):
        self.CurPos = data
    def Callgoal (self, data):
        self.NavGoal = data
    def rotate (self, rotTo):
        delta = 1
        
        veli = Twist()
        veli.angular.z = 0.3
        self.vel.publish(veli)
        while (abs(delta) > 0.0002):           
            Qar = [
                0,
                0,
                self.CurPos.pose.pose.orientation.z,
                self.CurPos.pose.pose.orientation.w
            ]
            MeAngle = euler_from_quaternion (Qar) [2]
            delta = rotTo - MeAngle              
            if delta < 0:
                veli.angular.z =-0.2
            if delta > 0:
                veli.angular.z = 0.2    
            self.vel.publish(veli)
        
            print (delta, rotTo, MeAngle)
        veli.angular.z = 0
        self.vel.publish(veli)
    def charge (self):
        dif = 2
        veli = Twist()
        veli.linear.x = 0.05
        self.vel.publish(veli)
        while(dif > 0.02):
            pain = self.CurPos.pose.pose.position
            suffer = self.NavGoal.pose.position
            dif = math.sqrt(((pain.x - suffer.x)**2)+((pain.y - suffer.y)**2))
            print dif
        veli.linear.x = 0
        self.vel.publish(veli)   
            
        

                
    
if __name__ == "__main__":
    das = PointyPepe()
    while (not rospy.is_shutdown()):
        while ((das.CurPos == None) or (das.NavGoal == None)) :
          pass

        Goal = das.NavGoal.pose.position
        Me = das.CurPos.pose.pose.position
        linx = Goal.x - Me.x
        liny = Goal.y - Me.y
        angle = math.atan2(liny, linx)   
        das.rotate(angle)
        print "-----------------------------------------------"
        rospy.sleep(rospy.Duration(1,0))
        das.charge()
        print "-----------------------------------------------"
        GoalRot = das.NavGoal.pose.orientation
        Qar = [
                0,
                0,
                GoalRot.z,
                GoalRot.w
            ]
        endAngle = euler_from_quaternion (Qar) [2]
        das.rotate(endAngle)
        print "end, kill me"
        das.NavGoal = None
            


        


    



 
