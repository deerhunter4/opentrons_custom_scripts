
# metadata
metadata = {
    'protocolName': 'amplicon_libraries_pooling',
    'author': 'Buczek M. <mateusz.buczek@uj.edu.pl>',
    'source': 'Symbiosis Evolution Group',
    'apiLevel': '2.9'
}

INPUT = open('/data/user_storage/for_robot_test.csv', "r") # add your csv file
TABLE = []
for line in INPUT:
    TABLE.append(line.strip().split(","))    
INPUT.close()

def run(ctx):

    # load labware
    source_plates = {
        str(i+1): ctx.load_labware('nest_96_wellplate_200ul_flat', slot, 'plate ' + str(i+1))
        for i, slot in enumerate(['2', '5', '8', '11', '6']) # enumerate() - at the same time you performe a loop on index(i) and value(slop)
    }
    tuberack = ctx.load_labware(
        'opentrons_24_aluminumblock_nest_1.5ml_snapcap', '9', 'pooling tuberack') # the name 'pooling tuberack' will appear on the screen during protocol run
    tipracks = [
        ctx.load_labware('opentrons_96_tiprack_10ul', slot, 'opentrons_96_tiprack_10ul')
        for slot in ['1', '4', '7', '10', '3']
    ]

    # load pipette
    p10 = ctx.load_instrument('p10_single', 'right', tip_racks=tipracks)

    # perform transfers
    for line in TABLE[1:]:
        slot, well, tube, volume = line[:4]
        source = source_plates[slot].wells_by_name()[well]
        destination_tube = tuberack.wells_by_name()[tube]
        vol = float(volume)
        p10.pick_up_tip()
        p10.aspirate(vol, source)
        p10.dispense(vol, destination_tube) # maybe insted put 'vol + 2' and skip p10.blow_out
        p10.blow_out(destination_tube.bottom(2))
        p10.drop_tip()
