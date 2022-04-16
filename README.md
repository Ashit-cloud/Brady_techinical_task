## First solution approach 
1. we read the file.
2. Extract the room names and removed all the empty and flatter the final room list.
3. Extract the area where chairs are available.
4. Solution of the 1st part is total number of chairs in the apartment sorted alphabetically.
5. The idea of second part of the solution is:
   - Firstly, finding the regex pattern and parse the horizontal boundary from + until next + (not sure this will work) and split it.
   - Secondly, Split the vertical boundary '|', '/', or '\' to until next '|', but this pattern not same for all the room.
   - Thirdly, where ever room name found start checking the 1st start vertical boundary and following that it will check top and bottom both direction then it will check the at list one horizontal line boundary to close the room.
   - Fourthly, we will iterate through flatten each rooms list and extract each room and save each room variable.
   -finlay, once we got the each room separately. easily we can count the each type of in the each room.
   
   
## Challenges
1. Although we can able to find the pattern by using regex, but the apartment design and each room design structure is quit different, so we are unable to capture the design properly.
2. since the design in txt file. and we can read only line by line, hence its hard extract each lines room information.
3. Any how if we can get the information of each room and each types of chairs in the room. if the design has changed this solution might not work.
hence , we need to build a robust solution.

## Alternative solution approach
1. Apart of this approach we might solve this problem converting .txt into image by using CNN technique  like Open-cv or other technique. 
