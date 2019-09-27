## Coversion from 3D Space coordinate to 2D- Image Coordinate

Let us consider (X,Y,Z) are the 3D Space coordinates and fx, fy are the focal length of Kinect.


![posture](https://user-images.githubusercontent.com/33776142/65754039-d2ec7300-e12d-11e9-8bad-43d4a32f7954.png)

We can obtain 2D- image Coordinte (u,v) by using following formula: 

```
Color Space Coordinates:
u=(X*fx /Z) + Cx
v=(Y*fy /Z) + Cy
where (X,Y,Z) are the Camera Coordinates and fx, fy are the focal lengths.
```
