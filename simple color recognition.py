
import cv2 as cv
import controller
# import controller as ct
# import controller2 as ct2

cap = cv.VideoCapture(2)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

txt1=""

while True:
    k,frame=cap.read()   #k = True or False, frame=3x3x3 matrix
    hsv_frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    height,width,depth=frame.shape

    x1=630 #horizontal 
    x2=650 

    #Left points
    point2=hsv_frame[270,x1]
    point3=hsv_frame[315,x1]
    point4=hsv_frame[360,x1]
    
    #Right points
    point6=hsv_frame[270,x2]
    point7=hsv_frame[315,x2]
    point8=hsv_frame[360,x2]    

    hue2=point2[0]
    hue3=point3[0]
    hue4=point4[0]
    hue6=point6[0]
    hue7=point7[0]
    hue8=point8[0]

    hue_yellow=60

    #for point 2
    color2="Undefined"
    if hue2<5:
        color2="RED"
    elif hue2 < 22:
        color2="ORANGE"
    elif hue2<hue_yellow:
        color2="YELLOW"
    elif hue2<78:
        color2="GREEN"
    elif hue2<131:
        color2="BLUE"
    elif hue2<170:
        color2="VIOLET"
    else:
        color2="RED"

    #for point 3
        color3="Undefined"
    if hue3<5:
        color3="RED"
    elif hue3 < 22:
        color3="ORANGE"
    elif hue3<hue_yellow:
        color3="YELLOW"
    elif hue3<78:
        color3="GREEN"
    elif hue3<131:
        color3="BLUE"
    elif hue3<170:
        color3="VIOLET"
    else:
        color3="RED"

    #for point 4
        color4="Undefined"
    if hue4<5:
        color4="RED"
    elif hue4 < 22:
        color4="ORANGE"
    elif hue4<hue_yellow:
        color4="YELLOW"
    elif hue4<78:
        color4="GREEN"
    elif hue4<131:
        color4="BLUE"
    elif hue4<170:
        color4="VIOLET"
    else:
        color4="RED"
    
    #for point 6
        color6="Undefined"
    if hue6<5:
        color6="RED"
    elif hue6 < 22:
        color6="ORANGE"
    elif hue6<hue_yellow:
        color6="YELLOW"
    elif hue6<78:
        color6="GREEN"
    elif hue6<131:
        color6="BLUE"
    elif hue6<170:
        color6="VIOLET"
    else:
        color6="RED"

    #for point 7
        color7="Undefined"
    if hue7<5:
        color7="RED"
    elif hue7 < 22:
        color7="ORANGE"
    elif hue7<hue_yellow:
        color7="YELLOW"
    elif hue7<78:
        color7="GREEN"
    elif hue7<131:
        color7="BLUE"
    elif hue7<170:
        color7="VIOLET"
    else:
        color7="RED"

    #for point 8
        color8="Undefined"
    if hue8<5:
        color8="RED"
    elif hue8 < 22:
        color8="ORANGE"
    elif hue8<hue_yellow:
        color8="YELLOW"
    elif hue8<78:
        color8="GREEN"
    elif hue8<131:
        color8="BLUE"
    elif hue8<170:
        color8="VIOLET"
    else:
        color8="RED"

    print('('+str(hue4)+','+str(hue8)+')','('+str(hue3)+','+str(hue7)+')','('+str(hue2)+','+str(hue6)+')')
    
    point2_bgr=frame[270,640]
    point3_bgr=frame[315,640]
    point4_bgr=frame[360,640]

    b2,g2,r2=int(point2_bgr[0]),int(point2_bgr[1]),int(point2_bgr[2])
    b3,g3,r3=int(point3_bgr[0]),int(point3_bgr[1]),int(point3_bgr[2])
    b4,g4,r4=int(point4_bgr[0]),int(point4_bgr[1]),int(point4_bgr[2])

 
    cv.rectangle(frame,(740,295),(940,335),(255,255,255),-1)
  

    if color4=="YELLOW" and color8=="YELLOW" and color3!="YELLOW" and color7!="YELLOW" and color2!="YELLOW" and color6!="YELLOW":
        txt="Low fill"
        controller.off_LED_GREEN()
        controller.off_LED_RED()
        controller.on_LED_YEL()
    elif color4!="YELLOW" and color8!="YELLOW" and color3!="YELLOW" and color7!="YELLOW" and color2!="YELLOW" and color6!="YELLOW":
        txt="No fill"
        controller.off_LED_YEL()
        controller.off_LED_RED()
        controller.on_LED_GREEN()
    elif color4=="YELLOW" and color8=="YELLOW" and color3=="YELLOW" and color7=="YELLOW" and color2!="YELLOW" and color6!="YELLOW":
        txt="STOP filling"
        controller.off_LED_GREEN()
        controller.off_LED_YEL()
        controller.on_LED_RED()
    elif color4=="YELLOW" and color8=="YELLOW" and color3=="YELLOW" and color7=="YELLOW" and color2=="YELLOW" and color6=="YELLOW":
        txt="Over filled" 
        controller.on_LED_GREEN()
        controller.on_LED_YEL()
        controller.on_LED_RED()


    cv.putText(frame,txt,(745,325),0,1,(70,3,138),2)

    cv.circle(frame,(630,270),1,(25,25,25),2)
    cv.circle(frame,(630,315),1,(25,25,25),2)
    cv.circle(frame,(630,360),1,(25,25,25),2)
    cv.circle(frame,(650,270),1,(25,25,25),2)
    cv.circle(frame,(650,315),1,(25,25,25),2)
    cv.circle(frame,(650,360),1,(25,25,25),2)

    cv.imshow("frame",frame)
    key=cv.waitKey(1)
    if key==27:
        break

cap.release()
cv.destroyAllWindows

controller.off_LED_GREEN()
controller.off_LED_RED()
controller.off_LED_YEL()



