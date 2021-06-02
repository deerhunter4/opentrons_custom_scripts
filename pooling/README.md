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


# csv_for_robot.R
Script csv_for_robot.R transform pooling volume data, stored as matrixes (PCR plates) in excel spreadsheet, into table, sored as csv file that can be used by amplicon_libraries_pooling.py. Script can transform as many plates as you need, unless they are sored in the same excel sheet. However, amplicon_libraries_pooling.py can pool up to five plates in one run.

**Requirements:**
RStudio, ‘readxl’ package, Excel

**Usage:**
Keep the script and excel files in the same folder. Open the script in the RStudio add in the first line the path to the folder in which you store the files. Install (line 3) and load (line 5) the ‘readxl’ package. Pooling destination wells (tubes) you can change in the line 26 and output file name in line 62. Next upload the function ‘csv_to_robot’ (lines 7-63) and finally in the last line (66) add name of your excel file and excel sheet name that contains your data. Run the function. Output csv file will appear in your working directory.

Structure of excel file is also important (check the Pooling_example.xlsx file). The most important part is that to add **number of the plate**, and word **“plate”** in the right position. Plate number should be in cell in the plate corner, bounded by A from below and 1 from the right. And “plate” world should located in the cell to the left of plate number cell. Particular location of your pooling plates in the spreadsheet doesn’t matter.


![image](https://user-images.githubusercontent.com/11144828/120454712-6ca10480-c394-11eb-81b0-373fa9c3804c.png)


