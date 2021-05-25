# amplicon_libraries_pooling.py
Script amplicon_libraries_pooling.py pools samples from up to five plates to up to 24 tubes. Script is design to work on Opentrons OT-2 robot. It was written basing on opentrons “Consolidation from .csv” script. Before running the script you need to prepare a csv file with pooling information (see example) and [upload it to the robot](https://support.opentrons.com/en/articles/3690659-copying-files-to-and-from-your-ot-2-with-scp). As default the script uses pipette p10 GEN1 (right mount) and NEST 96 Well Plate (100 µL PCR Full Skirt), however it is easy to change pipette type or any labware (plates, racks etc.) to the one that suits you. The csv file should be stored in the robot at '/data/user_storage/pooling.csv’, but you can change the path and file name.

**Requirements:**
OT-2 robot, Opentrons App, pooling.csv

**Usage:**
Upload your csv file to the '/data/user_storage/’ on the robot.
Open the Opentrons App and upload the amplicon_libraries_pooling.py protocol.
Prepare robot deck according to the picture and start the protocol.

![image](https://user-images.githubusercontent.com/11144828/119493180-3a722000-bd60-11eb-8eab-c602600f2cff.png)

If you are pooling less than 5 plates, some slots on the deck will remain empty. Robot by itself, basing on the csv file, will check how many plates are you pooling and how many tipboxes do you need.

**Example of input csv file:**

Plate Position,Source Well ID,Destination Tube ID,Volume

1,B2,A1,1

1,B3,A2,2

1,C4,A2,4

1,E9,A2,1

1,H11,A1,4

2,E1,A1,1

2,D6,A2,2

...
