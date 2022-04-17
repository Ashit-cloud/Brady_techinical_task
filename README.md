## First solution approach:
1. We read the file.
2. Extract the room names and removed all the empty and flatten the final room list.
3. Extract the area where chairs are available.
4. Solution of the 1st part is total number of chairs in the apartment sorted alphabetically.
5. The idea of second part of the solution is:
   - Firstly, finding the regex pattern and parse the horizontal boundary from + until next + (not sure this will work) and split it.
   - Secondly, split the vertical boundary '|', '/', or '\' to until next '|', ut this pattern is not the same for all of the rooms.
   - Thirdly, where ever the room name is found, start checking the 1st start vertical boundary and following that it will check top and bottom both direction then it will check the at list one horizontal line boundary to close the room.
   - Fourthly, we will iterate through flatten each rooms list and extract each room and save each room variable.
   - finally, once we've got each room... then we can easily count each type in each room.
   
   
## Challenges:
1. Although we where able to find the pattern by using regex, but the apartment design and each room design structure is quite different, so we are unable to capture the design properly.
2. No period. and we can read only line by line, hence its hard extract each lines room information.
3. Any how if we can get the information of each room and each types of chairs in the room. if the design has changed this solution might not work. it's hard to expect each line's room.

## Alternative solution approach:
Apart of this approach we might solve this problem converting '.txt' into image by using CNN technique like Open-cv ascii art to image.

1. Image can be convert ascii art. but ,txt to image (not sure) if yes. then
1. Ascii image command line tool that the image is essentially a grid that the grid can be converted to a numpy array.
3. Get distinct characters from the arrays use case sensitive regex to get the values.
4. For the rooms, similar thing, each line is a numpy array convert each array to a string of characters.
5. Using the regex to identify "(" and ")" in a single array which tells you if it's a room from there you are going to have to do some searching algorithm to find all upper case letters and stop searching when you hit a "/" "|" etc. and keep track of the values.
