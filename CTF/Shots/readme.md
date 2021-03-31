# Shots

![Shots Challenge](Shots.PNG)

### Challenge:
##### Lesly accidently deleted her photos from camera. She gave you the camera to figure it out. BTW, Lesly is Marvel fan.
##### 500 Points
##### Files: [sdcard](sdcard)

### Solve:

The file that comes with the challenge does not have an extension provided, however from context I was able to determine that it should be an **.iso** file. Addiing this extension to the file allowed me to open the archive using 7zip and explore the filesystem.

Insize the archive there were 2 folders, **lost+found** and **[SYS]**. Inside the [SYS] folder was a single file **Journal**.

Opening the Journal file in a hex editor provided no relevant information as to its source. A quick Google search suggested that the file, when associated with SD cards should have the file extension of **.dat** so I made a copy of the Jornal file to test with.


Exploring the challenge creators GitHub, I also discovered a CTF repository that contained a 'Stego' folder with a single image.

![Marvel](Marvel.jpg)

It may or may not be related, and this is most likely not the intended path, however I cannot discount the reference to Marvel in the provided clue. 

More investigation needs to be done for this solve.

### Flag
```
TBD
```
