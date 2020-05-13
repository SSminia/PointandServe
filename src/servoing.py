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
        dif = math.sqrt(((Me.x - Goal.x)**2)+((Me.y - Goal.y)**2))
        veli = Twist()
        veliR = Twist() 

        while (dif > 0.02) or (angle > 0.002):
            Goal = das.NavGoal.pose.position
            Me = das.CurPos.pose.pose.position
            linx = Goal.x - Me.x
            liny = Goal.y - Me.y
            angle = math.atan2(liny, linx)   
            dif = math.sqrt(((Me.x - Goal.x)**2)+((Me.y - Goal.y)**2))
            
            veli.linear.x = 0.25
            if dif < 1 :
                veli.linear.x = 0.20 * dif + 0.05
            #das.vel.publish(veli) 

            Qar = [
                0,
                0,
                das.CurPos.pose.pose.orientation.z,
                das.CurPos.pose.pose.orientation.w
            ]
            MeAngle = euler_from_quaternion (Qar) [2]
            delta = angle - MeAngle
            ABdelta = abs(delta)
            if delta < 0:
                veli.angular.z =-0.8
                if ABdelta < 0.05 :
                    veli.angular.z =-0.1 
            if delta > 0:
                veli.angular.z = 0.8    
                if ABdelta < 0.05 :
                    veli.angular.z = 0.1 
            das.vel.publish(veli)
            print "driving" 
        #veli.angular.z = 0.0 
    
        #das.veliR.publish(veliR)
        

        print "-----------------------------------------------"
        #rospy.sleep(rospy.Duration(1,0))
        while (dif < 0.2) and (angle < 0.002):
            Goal = das.NavGoal.pose.position
            Me = das.CurPos.pose.pose.position
            linx = Goal.x - Me.x
            liny = Goal.y - Me.y
            angle = math.atan2(liny, linx)   
            dif = math.sqrt(((Me.x - Goal.x)**2)+((Me.y - Goal.y)**2))
            
            print "end rotate"
            GoalR = [
                0,
                0,
                das.NavGoal.pose.orientation.z,
                das.NavGoal.pose.orientation.w
            ]
            endAngle = euler_from_quaternion (GoalR) [2]
            
            Qar = [
                0,
                0,
                das.CurPos.pose.pose.orientation.z,
                das.CurPos.pose.pose.orientation.w
            ]
            MeAngle = euler_from_quaternion (Qar) [2]
            delta = endAngle - MeAngle
            ABdelta = abs(delta)
            if delta < 0:
                veli.angular.z =-0.3
                if ABdelta < 0.05 :
                    veli.angular.z =-0.1 
            if delta > 0:
                veli.angular.z = 0.3    
                if ABdelta < 0.05 :
                    veli.angular.z = 0.1 
            das.vel.publish(veli)
            if ABdelta < 0.002:     
                #das.NavGoal = None
                veli.angular.z = 0.0 
                print "bye bye"
            veli.linear.x = 0.00
            das.vel.publish(veli)
            
            


        


    



 
