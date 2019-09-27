## Coversion from 3D Space coordinate to 2D Image Coordinate

Let us consider (X,Y,Z) are the 3D Space coordinates and fx, fy are the focal lengths of Kinect V2.


![posture](https://user-images.githubusercontent.com/33776142/65754039-d2ec7300-e12d-11e9-8bad-43d4a32f7954.png)

### Formula: 

```
Color Space Coordinates:
u = (X*fx /Z) + Cx
v = (Y*fy /Z) + Cy
where (X,Y,Z) are the Camera Coordinates and fx, fy are the focal lengths.
```

In our case:
```
Principal point (Cx, Cy) = (989.3053162, 555.9211734) and focal length fx = 1045.640667, fy = -1073.818121
```
