from opentrons import protocol_api

metadata = {
    'apiLevel': '2.4',
    'author': 'Buczek M. <mateusz.buczek@uj.edu.pl>',
    'protocolName': 'Extraction',
    'description': 'Extraction using magnetic beads.',
    'source': 'Symbiosis Evolution Group',}

def run(protocol: protocol_api.ProtocolContext):
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 9)
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_10ul', 1)
    # tiprack_3 = protocol.load_labware('opentrons_96_tiprack_300ul', 9)
    #tiprack_4 = protocol.load_labware('opentrons_96_tiprack_300ul', 10)
    #tiprack_5 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
    #tiprack_6 = protocol.load_labware('opentrons_96_tiprack_300ul', 5)
    #tiprack_7 = protocol.load_labware('opentrons_96_tiprack_300ul', 6)
    reservoir = protocol.load_labware('nest_12_reservoir_15ml', 8)
    plate_1 = protocol.load_labware('4titude_96_wellplate_onrack_200ul', 4)
    multi_300 = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tiprack_1])
    multi_10 = protocol.load_instrument('p10_multi', 'left', tip_racks=[tiprack_2])
    mag_mod = protocol.load_module('magnetic module', 7)
    plate_2 = mag_mod.load_labware('thermofisher_96_wellplate_800ul')
    plate_3 = protocol.load_labware('4titude_96_wellplate_onrack_200ul', 5)

    protocol.pause('Mix beads and place them in right position.\n')

    mag_mod.disengage()

    for i in ['A4', 'A11']:
        multi_10.pick_up_tip()
        multi_10.aspirate(8, plate_1[i], rate=.25)
        multi_10.dispense(8, plate_2[i], rate=.75) 
        multi_10.mix(10,10)
        multi_10.drop_tip()
    
    # multi_10.transfer(8, reservoir.wells_by_name()['A1'], [plate_2.wells_by_name()[well_name] 
    # for well_name in ['A4', 'A11']],
    # new_tip='always', mix_before=(2,80), mix_after=(6,80))

    protocol.delay(minutes=4)
    mag_mod.engage(height=17.5)
    protocol.delay(minutes=4)

    protocol.pause('Start step 2.\n')

    for i in ['A4', 'A11']:
        multi_300.pick_up_tip()
        multi_300.aspirate(25, plate_2[i], rate=.25)
        # multi_300.air_gap(10)
        multi_300.dispense(25, reservoir['A6'].top(-5), rate=.75) 
        multi_300.blow_out(reservoir['A6'].top(z=-5))
        multi_300.drop_tip()

    protocol.pause('Start step 3.\n')

    multi_300.pick_up_tip()

    for i in ['A4', 'A11']:
        multi_300.aspirate(100, reservoir['A10'], rate=.5)
        multi_300.air_gap(10)
        multi_300.dispense(110, plate_2[i].top(-10), rate=.75) # tips going to the well 10 mm belowe the surface
        multi_300.blow_out(plate_2[i].top(z=-10))

    multi_300.drop_tip()

    for i in ['A4','A11']:
        multi_300.pick_up_tip()
        multi_300.aspirate(110, plate_2[i], rate=.25)
        # multi_300.air_gap(10)
        multi_300.dispense(110, reservoir['A7'].top(-5), rate=.75)
        multi_300.blow_out(reservoir['A7'].top(z=-5))
        multi_300.drop_tip()

    multi_300.pick_up_tip()

    for i in ['A4', 'A11']:
        multi_300.aspirate(100, reservoir['A10'], rate=.5)
        multi_300.air_gap(10)
        multi_300.dispense(110, plate_2[i].top(-10), rate=.75) # tips going to the well 10 mm belowe the surface
        multi_300.blow_out(plate_1[i].top(z=-10))

    multi_300.drop_tip()

    for i in ['A4','A11']:
        multi_300.pick_up_tip()
        multi_300.aspirate(110, plate_2[i], rate=.25)
        # multi_300.air_gap(10)
        multi_300.dispense(110, reservoir['A7'].top(-5), rate=.75)
        multi_300.blow_out(reservoir['A7'].top(z=-5))
        multi_300.drop_tip()

    protocol.delay(minutes=4)
    mag_mod.disengage()

    multi_300.transfer(20.5, reservoir.wells_by_name()['A12'], [plate_1.wells_by_name()[well_name] 
    for well_name in ['A4']],
    new_tip='always', mix_after=(8,16))

    multi_300.transfer(30.5, reservoir.wells_by_name()['A12'], [plate_1.wells_by_name()[well_name] 
    for well_name in ['A11']],
    new_tip='always', mix_after=(6,16))

    protocol.delay(minutes=3)
    mag_mod.engage(height=17.5)
    protocol.delay(minutes=3)

    for i in ['A4']:
        multi_300.pick_up_tip()
        multi_300.aspirate(20, plate_2[i], rate=.25)
        multi_300.dispense(20, plate_3[i], rate=.75)
        # multi_50.blow_out(reservoir['A7'].top(z=-5)) # I would skip blowing here, to not contaminate the samples
        multi_300.drop_tip()

    for i in ['A11']:
        multi_300.pick_up_tip()
        multi_300.aspirate(30, plate_2[i], rate=.25)
        multi_300.dispense(30, plate_3[i], rate=.75)
        # multi_50.blow_out(reservoir['A7'].top(z=-5)) # I would skip blowing here, to not contaminate the samples
        multi_300.drop_tip()

    mag_mod.disengage()
    protocol.pause('This is the end!!!.\n')

