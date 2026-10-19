import flet as ft



# ДАННЫЕ САМОЛЕТОВ


aircrafts = [

    {
        "manufacturer": "Airbus",
        "model": "A320neo",
        "engine": "LEAP-1A"
    },

    {
        "manufacturer": "Airbus",
        "model": "A350-900",
        "engine": "Trent XWB"
    },

    {
        "manufacturer": "Airbus",
        "model": "A380-800",
        "engine": "Trent 900"
    },


    {
        "manufacturer": "Boeing",
        "model": "737-800",
        "engine": "CFM56-7B"
    },

    {
        "manufacturer": "Boeing",
        "model": "737 MAX 8",
        "engine": "LEAP-1B"
    },

    {
        "manufacturer": "Boeing",
        "model": "777-300ER",
        "engine": "GE90"
    },


    {
        "manufacturer": "Cessna",
        "model": "C172 Skyhawk",
        "engine": "Lycoming IO-360"
    },


    {
        "manufacturer": "ATR",
        "model": "ATR 72-600",
        "engine": "PW127M"
    },


    {
        "manufacturer": "Embraer",
        "model": "E190-E2",
        "engine": "PW1900G"
    }

]



# =========================
# ЧЕК-ЛИСТЫ
# =========================

# =========================
# ЧЕК-ЛИСТЫ ПО ЭТАПАМ
# =========================


checklists = {


"A320neo": {

"COCKPIT PREPARATION": [

("BATTERY", "ON", "Aircraft electrical power"),

("EXT PWR", "ON", "External power"),

("APU", "START / ON", "Auxiliary Power Unit (ВСУ)"),

("ADIRS", "ALIGN", "Air Data Inertial Reference System"),

("OXYGEN", "CHECK", "Crew oxygen system"),

("FIRE TEST", "TEST", "Fire detection system"),

("FUEL", "CHECK", "Fuel quantity and pumps"),

("HYDRAULICS", "CHECK", "Hydraulic system"),

("MCDU", "SET", "Flight management system")

],

"BEFORE START": [

("DOORS", "CLOSED", "Aircraft doors"),

("BEACON", "ON", "Anti-collision light"),

("PARKING BRAKE", "SET", "Parking brake"),

("PUSHBACK", "CLEAR", "Pushback clearance")

],

"ENGINE START": [

("ENGINE 2", "START", "Engine start sequence"),

("ENGINE 1", "START", "Engine start sequence"),

("OIL PRESSURE", "CHECK", "Engine oil pressure"),

("EGT", "MONITOR", "Exhaust gas temperature"),

("GENERATORS", "ON", "Electrical generators")

],

"AFTER START": [

("PACKS", "ON", "Air conditioning packs"),

("BLEED AIR", "SET", "Pneumatic system"),

("ANTI-ICE", "AS REQUIRED", "Engine anti-ice"),

("FLIGHT CONTROLS", "CHECK", "Flight controls"),

("FLAPS", "SET", "Takeoff configuration")

],

"TAXI": [

("BRAKES", "CHECK", "Brake system"),

("FLIGHT INSTRUMENTS", "CHECK", "Flight instruments"),

("TAKEOFF BRIEFING", "COMPLETE", "Crew briefing"),

("LIGHTS", "AS REQUIRED", "Exterior lights")

],

"BEFORE TAKEOFF": [

("FLAPS", "SET", "Takeoff configuration"),

("SPOILERS", "ARM", "Automatic spoiler system"),

("AUTOTHRUST", "ARM", "Automatic thrust system"),

("TCAS", "TA/RA", "Traffic collision avoidance"),

("CABIN", "READY", "Cabin ready")

],

"AFTER TAKEOFF": [

("GEAR", "UP", "Landing gear"),

("FLAPS", "RETRACT", "Flap retraction"),

("CLIMB POWER", "SET", "Engine thrust")

],

"CLIMB": [

("ENGINE PARAMETERS", "MONITOR", "Engine monitoring"),

("PRESSURIZATION", "CHECK", "Cabin pressure"),

("ANTI-ICE", "AS REQUIRED", "Ice protection")

],

"CRUISE": [

("FUEL", "MONITOR", "Fuel monitoring"),

("SYSTEMS", "CHECK", "Aircraft systems"),

("WEATHER RADAR", "SET", "Weather radar")

],

"DESCENT": [

("DESCENT BRIEFING", "COMPLETE", "Approach briefing"),

("LANDING DATA", "SET", "Landing performance"),

("AUTOBRAKE", "SET", "Automatic braking")

],

"APPROACH": [

("LANDING GEAR", "DOWN", "Landing gear"),

("FLAPS", "SET", "Landing configuration"),

("LANDING LIGHTS", "ON", "Landing lights"),

("CABIN", "READY", "Cabin preparation")

],

"LANDING": [

("REVERSE THRUST", "AS REQUIRED", "Reverse thrust"),

("BRAKES", "APPLY", "Wheel brakes"),

("SPOILERS", "CHECK", "Ground spoilers")

],

"AFTER LANDING": [

("FLAPS", "UP", "Flap retraction"),

("SPOILERS", "DISARM", "Spoilers"),

("APU", "START", "Auxiliary Power Unit"),

("LIGHTS", "AS REQUIRED", "Taxi lights")

],

"PARKING / SHUTDOWN": [

("PARKING BRAKE", "SET", "Parking brake"),

("ENGINES", "OFF", "Engine shutdown"),

("FUEL PUMPS", "OFF", "Fuel system"),

("BEACON", "OFF", "Anti-collision light"),

("BATTERY", "OFF", "Electrical system")

]

},



"A350-900": {

"COCKPIT PREPARATION": [

("BATTERY", "ON", "Aircraft electrical power"),

("EXT PWR", "ON", "External power"),

("APU", "START / ON", "Auxiliary Power Unit (ВСУ)"),

("ADIRS", "ALIGN", "Air Data Inertial Reference System"),

("FMS", "SET", "Flight management system"),

("FUEL", "CHECK", "Fuel system"),

("HYDRAULICS", "CHECK", "Hydraulic system")

],

"BEFORE START": [

("DOORS", "CLOSED", "Aircraft doors"),

("BEACON", "ON", "Anti-collision light"),

("PARKING BRAKE", "SET", "Parking brake"),

("PUSHBACK", "CLEAR", "Pushback clearance")

],

"ENGINE START": [

("ENGINE 1", "START", "Trent XWB engine start"),

("ENGINE 2", "START", "Trent XWB engine start"),

("ENGINE PARAMETERS", "CHECK", "Engine indications"),

("GENERATORS", "ON", "Electrical generators")

],

"AFTER START": [

("PACKS", "ON", "Air conditioning"),

("BLEED AIR", "SET", "Pneumatic system"),

("ANTI-ICE", "AS REQUIRED", "Engine anti-ice"),

("FLIGHT CONTROLS", "CHECK", "Flight controls")

],

"TAXI": [

("BRAKES", "CHECK", "Brake system"),

("TAKEOFF BRIEFING", "COMPLETE", "Crew briefing"),

("LIGHTS", "AS REQUIRED", "Exterior lights")

],

"BEFORE TAKEOFF": [

("FLAPS", "SET", "Takeoff configuration"),

("SPOILERS", "ARM", "Ground spoilers"),

("AUTOTHROTTLE", "ARM", "Automatic thrust"),

("TCAS", "TA/RA", "Collision avoidance"),

("CABIN", "READY", "Cabin ready")

],"BEFORE TAKEOFF": [

("FLAPS", "SET", "Takeoff configuration"),

("SPOILERS", "ARM", "Ground spoilers"),

("AUTOTHROTTLE", "ARM", "Automatic thrust"),

("TCAS", "TA/RA", "Collision avoidance"),

("CABIN", "READY", "Cabin ready")

],"AFTER TAKEOFF": [

("GEAR", "UP", "Landing gear"),

("FLAPS", "RETRACT", "Flap retraction"),

("CLIMB POWER", "SET", "Engine thrust")

],

"CLIMB": [

("ENGINE PARAMETERS", "MONITOR", "Engine monitoring"),

("PRESSURIZATION", "CHECK", "Cabin pressure"),

("ANTI-ICE", "AS REQUIRED", "Ice protection")

],

"CRUISE": [

("FUEL", "MONITOR", "Fuel monitoring"),

("SYSTEMS", "CHECK", "Aircraft systems"),

("WEATHER RADAR", "SET", "Weather radar")

],

"DESCENT": [

("DESCENT BRIEFING", "COMPLETE", "Approach briefing"),

("LANDING DATA", "SET", "Landing performance"),

("AUTOBRAKE", "SET", "Automatic braking")

],

"APPROACH": [

("LANDING GEAR", "DOWN", "Landing gear"),

("FLAPS", "SET", "Landing configuration"),

("LANDING LIGHTS", "ON", "Landing lights"),

("CABIN", "READY", "Cabin preparation")

],

"LANDING": [

("REVERSE THRUST", "AS REQUIRED", "Reverse thrust"),

("BRAKES", "APPLY", "Wheel brakes"),

("SPOILERS", "CHECK", "Ground spoilers")

],

"AFTER LANDING": [

("FLAPS", "UP", "Flap retraction"),

("SPOILERS", "DISARM", "Spoilers"),

("APU", "START", "Auxiliary Power Unit"),

("LIGHTS", "AS REQUIRED", "Taxi lights")

],

"PARKING / SHUTDOWN": [

("PARKING BRAKE", "SET", "Parking brake"),

("ENGINES", "OFF", "Engine shutdown"),

("FUEL PUMPS", "OFF", "Fuel system"),

("BEACON", "OFF", "Anti-collision light"),

("BATTERY", "OFF", "Electrical system")

]

},



"A380-800": {


"COCKPIT PREPARATION": [

("BATTERY", "ON", "Aircraft electrical power"),

("EXT PWR", "ON", "External power"),

("APU", "START / ON", "Auxiliary Power Unit (ВСУ)"),

("ADIRS", "ALIGN", "Air Data Inertial Reference System"),

("FMS", "SET", "Flight management system"),

("FUEL", "CHECK", "Fuel system"),

("HYDRAULICS", "CHECK", "Hydraulic system")

],


"BEFORE START": [

("DOORS", "CLOSED", "Aircraft doors"),

("BEACON", "ON", "Anti-collision light"),

("PARKING BRAKE", "SET", "Parking brake"),

("PUSHBACK", "CLEAR", "Pushback clearance")

],


"ENGINE START": [

("ENGINE 1", "START", "Engine start sequence"),

("ENGINE 2", "START", "Engine start sequence"),

("ENGINE 3", "START", "Engine start sequence"),

("ENGINE 4", "START", "Engine start sequence"),

("GENERATORS", "ON", "Electrical generators")

],


"AFTER START": [

("PACKS", "ON", "Air conditioning"),

("BLEED AIR", "SET", "Pneumatic system"),

("ANTI-ICE", "AS REQUIRED", "Engine anti-ice"),

("FLIGHT CONTROLS", "CHECK", "Flight controls"),

("FLAPS", "SET", "Takeoff configuration")

],


"TAXI": [

("BRAKES", "CHECK", "Brake system"),

("TAKEOFF BRIEFING", "COMPLETE", "Crew briefing"),

("LIGHTS", "AS REQUIRED", "Exterior lights")

],


"BEFORE TAKEOFF": [

("FLAPS", "SET", "Takeoff configuration"),

("SPOILERS", "ARM", "Ground spoilers"),

("AUTOTHRUST", "ARM", "Automatic thrust"),

("TCAS", "TA/RA", "Collision avoidance"),

("CABIN", "READY", "Cabin ready")

],


"AFTER TAKEOFF": [

("GEAR", "UP", "Landing gear"),

("FLAPS", "RETRACT", "Flap retraction")

],


"CLIMB": [

("ENGINE PARAMETERS", "MONITOR", "Engine monitoring"),

("PRESSURIZATION", "CHECK", "Cabin pressure")

],


"CRUISE": [

("FUEL", "MONITOR", "Fuel monitoring"),

("SYSTEMS", "CHECK", "Aircraft systems")

],


"DESCENT": [

("LANDING DATA", "SET", "Landing performance"),

("AUTOBRAKE", "SET", "Automatic braking")

],


"APPROACH": [

("GEAR", "DOWN", "Landing gear"),

("FLAPS", "SET", "Landing configuration"),

("CABIN", "READY", "Cabin ready")

],


"LANDING": [

("REVERSE THRUST", "AS REQUIRED", "Reverse thrust"),

("BRAKES", "APPLY", "Wheel brakes")

],


"AFTER LANDING": [

("FLAPS", "UP", "Flap retraction"),

("SPOILERS", "DISARM", "Spoilers"),

("APU", "START", "Auxiliary Power Unit")

],


"PARKING / SHUTDOWN": [

("PARKING BRAKE", "SET", "Parking brake"),

("ENGINES", "OFF", "Engine shutdown"),

("BATTERY", "OFF", "Electrical system")

],
},


"Boeing 737 MAX 8": {


"COCKPIT PREPARATION": [

("BATTERY", "ON", "Aircraft electrical system"),

("GROUND POWER", "ON", "External electrical power"),

("APU", "START / ON", "Auxiliary Power Unit (ВСУ)"),

("IRS", "ALIGN", "Inertial Reference System"),

("FMC", "SET", "Flight Management Computer"),

("FUEL", "CHECK", "Fuel quantity"),

("HYDRAULICS", "CHECK", "Hydraulic system")

],


"BEFORE START": [

("DOORS", "CLOSED", "Aircraft doors"),

("BEACON", "ON", "Anti-collision light"),

("PARKING BRAKE", "SET", "Parking brake"),

("PUSHBACK", "CLEAR", "Pushback clearance")

],


"ENGINE START": [

("ENGINE 2", "START", "LEAP-1B engine start"),

("ENGINE 1", "START", "LEAP-1B engine start"),

("N1/N2", "CHECK", "Engine rotation"),

("EGT", "MONITOR", "Exhaust temperature"),

("GENERATORS", "ON", "Electrical generators")

],


"AFTER START": [

("PACKS", "ON", "Air conditioning"),

("BLEEDS", "ON", "Pneumatic system"),

("ANTI-ICE", "AS REQUIRED", "Engine anti-ice"),

("FLIGHT CONTROLS", "CHECK", "Flight controls"),

("FLAPS", "SET", "Takeoff configuration")

],


"TAXI": [

("BRAKES", "CHECK", "Brake system"),

("TAKEOFF BRIEFING", "COMPLETE", "Crew briefing"),

("LIGHTS", "AS REQUIRED", "Exterior lights")

],


"BEFORE TAKEOFF": [

("FLAPS", "SET", "Takeoff configuration"),

("SPEED BRAKE", "ARM", "Speed brake"),

("AUTOTHROTTLE", "ARM", "Automatic thrust"),

("TCAS", "TA/RA", "Traffic avoidance"),

("CABIN", "READY", "Cabin ready")

],


"AFTER TAKEOFF": [

("GEAR", "UP", "Landing gear"),

("FLAPS", "UP", "Flap retraction"),

("CLIMB POWER", "SET", "Engine thrust")

],


"CLIMB": [

("ENGINE PARAMETERS", "MONITOR", "Engine monitoring"),

("PRESSURIZATION", "CHECK", "Cabin pressure"),

("ANTI-ICE", "AS REQUIRED", "Ice protection")

],


"CRUISE": [

("FUEL", "MONITOR", "Fuel monitoring"),

("SYSTEMS", "CHECK", "Aircraft systems"),

("WEATHER RADAR", "SET", "Weather radar")

],


"DESCENT": [

("DESCENT BRIEFING", "COMPLETE", "Approach briefing"),

("LANDING DATA", "SET", "Landing performance"),

("AUTOBRAKE", "SET", "Automatic braking")

],


"APPROACH": [

("GEAR", "DOWN", "Landing gear"),

("FLAPS", "SET", "Landing configuration"),

("LANDING LIGHTS", "ON", "Landing lights"),

("CABIN", "READY", "Cabin ready")

],


"LANDING": [

("REVERSE THRUST", "AS REQUIRED", "Reverse thrust"),

("BRAKES", "APPLY", "Wheel brakes"),

("SPOILERS", "CHECK", "Ground spoilers")

],


"AFTER LANDING": [

("FLAPS", "UP", "Flap retraction"),

("SPEED BRAKE", "DOWN", "Speed brake"),

("APU", "START", "Auxiliary Power Unit"),

("LIGHTS", "AS REQUIRED", "Taxi lights")

],


"PARKING / SHUTDOWN": [

("PARKING BRAKE", "SET", "Parking brake"),

("ENGINES", "OFF", "Engine shutdown"),

("FUEL PUMPS", "OFF", "Fuel system"),

("BEACON", "OFF", "Anti-collision light"),

("BATTERY", "OFF", "Electrical system")

]

},"Boeing 777-300ER": {


"COCKPIT PREPARATION": [

("BATTERY", "ON", "Aircraft electrical system"),

("GROUND POWER", "ON", "External electrical power"),

("APU", "START / ON", "Auxiliary Power Unit (ВСУ)"),

("IRS", "ALIGN", "Inertial Reference System"),

("FMS", "SET", "Flight Management System"),

("OXYGEN", "CHECK", "Crew oxygen system"),

("FIRE TEST", "TEST", "Fire warning system"),

("FUEL", "CHECK", "Fuel quantity and pumps"),

("HYDRAULICS", "CHECK", "Hydraulic system")

],



"BEFORE START": [

("DOORS", "CLOSED", "Aircraft doors"),

("BEACON", "ON", "Anti-collision light"),

("PACKS", "OFF", "Engine start configuration"),

("PARKING BRAKE", "SET", "Parking brake"),

("PUSHBACK", "CLEAR", "Pushback clearance")

],



"ENGINE START": [

("ENGINE 2", "START", "GE90 engine start"),

("ENGINE 1", "START", "GE90 engine start"),

("N1/N2", "MONITOR", "Engine rotation"),

("EGT", "CHECK", "Exhaust gas temperature"),

("OIL PRESSURE", "CHECK", "Engine oil pressure"),

("GENERATORS", "ON", "Electrical generators")

],



"AFTER START": [

("PACKS", "ON", "Air conditioning system"),

("BLEEDS", "ON", "Pneumatic system"),

("ANTI-ICE", "AS REQUIRED", "Engine anti-ice"),

("FLIGHT CONTROLS", "CHECK", "Flight controls"),

("FLAPS", "SET", "Takeoff configuration")

],



"TAXI": [

("BRAKES", "CHECK", "Brake system"),

("FLIGHT INSTRUMENTS", "CHECK", "Flight instruments"),

("TAKEOFF BRIEFING", "COMPLETE", "Crew briefing"),

("LIGHTS", "AS REQUIRED", "Exterior lights")

],



"BEFORE TAKEOFF": [

("FLAPS", "SET", "Takeoff configuration"),

("SPEED BRAKE", "ARM", "Speed brake system"),

("AUTOTHROTTLE", "ARM", "Automatic thrust"),

("TRANSPONDER", "TA/RA", "Traffic avoidance system"),

("CABIN", "READY", "Cabin ready"),

("TAKEOFF WARNING", "TEST", "Warning system")

],



"AFTER TAKEOFF": [

("GEAR", "UP", "Landing gear"),

("FLAPS", "RETRACT", "Flap retraction"),

("CLIMB POWER", "SET", "Engine thrust")

],



"CLIMB": [

("ENGINE PARAMETERS", "MONITOR", "Engine monitoring"),

("PRESSURIZATION", "CHECK", "Cabin pressure"),

("ANTI-ICE", "AS REQUIRED", "Ice protection"),

("FUEL BALANCE", "CHECK", "Fuel system")

],



"CRUISE": [

("FUEL", "MONITOR", "Fuel monitoring"),

("SYSTEMS", "CHECK", "Aircraft systems"),

("WEATHER RADAR", "SET", "Weather radar"),

("ETOPS", "CHECK", "Long range operations")

],



"DESCENT": [

("DESCENT BRIEFING", "COMPLETE", "Approach briefing"),

("LANDING DATA", "SET", "Landing performance"),

("AUTOBRAKE", "SET", "Automatic braking"),

("APPROACH SETUP", "COMPLETE", "Navigation setup")

],



"APPROACH": [

("LANDING GEAR", "DOWN", "Landing gear"),

("FLAPS", "SET", "Landing configuration"),

("LANDING LIGHTS", "ON", "Landing lights"),

("CABIN", "READY", "Cabin preparation"),

("SPEED BRAKE", "ARM", "Speed brake")

],



"LANDING": [

("REVERSE THRUST", "AS REQUIRED", "Reverse thrust"),

("BRAKES", "APPLY", "Wheel brakes"),

("SPOILERS", "CHECK", "Ground spoilers"),

("CENTERLINE", "MAINTAIN", "Runway tracking")

],



"AFTER LANDING": [

("FLAPS", "UP", "Flap retraction"),

("SPEED BRAKE", "DOWN", "Speed brake"),

("APU", "START", "Auxiliary Power Unit"),

("LIGHTS", "AS REQUIRED", "Taxi lights"),

("TRANSPONDER", "STANDBY", "Traffic system")

],



"PARKING / SHUTDOWN": [

("PARKING BRAKE", "SET", "Parking brake"),

("ENGINES", "OFF", "Engine shutdown"),

("FUEL PUMPS", "OFF", "Fuel system"),

("BEACON", "OFF", "Anti-collision light"),

("EXTERNAL POWER", "ON", "Ground power"),

("BATTERY", "OFF", "Electrical system")

]

},"737-800": {


"COCKPIT PREPARATION": [

("BATTERY", "ON", "Aircraft electrical system"),

("GROUND POWER", "ON", "External power"),

("APU", "START / ON", "Auxiliary Power Unit"),

("IRS", "ALIGN", "Inertial Reference System"),

("FMC", "SET", "Flight Management Computer"),

("FUEL", "CHECK", "Fuel quantity"),

("HYDRAULICS", "CHECK", "Hydraulic system")

],


"BEFORE START": [

("DOORS", "CLOSED", "Aircraft doors"),

("BEACON", "ON", "Anti-collision light"),

("PARKING BRAKE", "SET", "Parking brake"),

("PUSHBACK", "CLEAR", "Pushback clearance")

],


"ENGINE START": [

("ENGINE 2", "START", "CFM56 engine start"),

("ENGINE 1", "START", "CFM56 engine start"),

("N1/N2", "CHECK", "Engine rotation"),

("EGT", "MONITOR", "Exhaust gas temperature"),

("GENERATORS", "ON", "Electrical generators")

]
    },
    "C172 Skyhawk": {


"COCKPIT PREPARATION": [

("DOCUMENTS", "CHECK", "Aircraft documents"),

("BATTERY", "ON", "Electrical system"),

("FUEL SELECTOR", "BOTH", "Fuel selector"),

("FUEL QUANTITY", "CHECK", "Fuel quantity"),

("OIL LEVEL", "CHECK", "Engine oil"),

("MASTER SWITCH", "ON", "Electrical power"),

("MIXTURE", "RICH", "Engine mixture"),

("CARB HEAT", "COLD", "Carburetor heat")

],



"BEFORE START": [

("PARKING BRAKE", "SET", "Parking brake"),

("AREA", "CLEAR", "Propeller area"),

("BEACON", "ON", "Anti-collision light"),

("PRIMER", "AS REQUIRED", "Engine priming")

],



"ENGINE START": [

("STARTER", "ENGAGE", "Engine start"),

("RPM", "CHECK", "Engine RPM"),

("OIL PRESSURE", "CHECK", "Engine oil pressure"),

("ALTERNATOR", "ON", "Electrical charging")

],



"AFTER START": [

("AVIONICS", "ON", "Avionics system"),

("RADIOS", "SET", "Communication radios"),

("FLIGHT CONTROLS", "CHECK", "Control surfaces"),

("TRIM", "SET", "Aircraft trim")

],



"TAXI": [

("BRAKES", "CHECK", "Brake system"),

("COMPASS", "CHECK", "Heading indication"),

("INSTRUMENTS", "CHECK", "Flight instruments"),

("LIGHTS", "AS REQUIRED", "Exterior lights")

],



"BEFORE TAKEOFF": [

("FLAPS", "SET", "Takeoff configuration"),

("MIXTURE", "RICH", "Engine mixture"),

("CARB HEAT", "COLD", "Carburetor heat"),

("ENGINE INSTRUMENTS", "CHECK", "Engine parameters"),

("RUNWAY", "CLEAR", "Runway check")

],



"AFTER TAKEOFF": [

("CLIMB POWER", "SET", "Engine power"),

("FLAPS", "UP", "Flap retraction"),

("GEAR", "UP", "Landing gear if installed")

],



"CLIMB": [

("ENGINE PARAMETERS", "MONITOR", "Engine monitoring"),

("ALTIMETER", "CHECK", "Altitude"),

("TRIM", "ADJUST", "Aircraft trim")

],



"CRUISE": [

("POWER", "SET", "Cruise power"),

("FUEL", "MONITOR", "Fuel monitoring"),

("ENGINE", "MONITOR", "Engine condition")

],



"DESCENT": [

("DESCENT BRIEFING", "COMPLETE", "Landing preparation"),

("POWER", "REDUCE", "Engine power"),

("ALTITUDE", "CHECK", "Altitude control")

],



"APPROACH": [

("LANDING LIGHTS", "ON", "Landing lights"),

("MIXTURE", "RICH", "Engine mixture"),

("FLAPS", "SET", "Landing configuration")

],



"LANDING": [

("TOUCHDOWN", "COMPLETE", "Landing"),

("BRAKES", "APPLY", "Wheel brakes"),

("FLAPS", "AS REQUIRED", "Flap setting")

],



"AFTER LANDING": [

("FLAPS", "UP", "Flap retraction"),

("TRANSPONDER", "STANDBY", "Transponder"),

("LIGHTS", "AS REQUIRED", "Taxi lights")

],



"PARKING / SHUTDOWN": [

("PARKING BRAKE", "SET", "Parking brake"),

("AVIONICS", "OFF", "Avionics"),

("MASTER SWITCH", "OFF", "Electrical system"),

("FUEL SELECTOR", "OFF", "Fuel system")

]

},



"ATR 72-600": {


"COCKPIT PREPARATION": [

("BATTERY", "ON", "Electrical system"),

("EXT PWR", "ON", "External power"),

("APU", "START / ON", "Auxiliary Power Unit"),

("FUEL", "CHECK", "Fuel system"),

("HYDRAULICS", "CHECK", "Hydraulic system"),

("FMS", "SET", "Flight management system")

],



"BEFORE START": [

("DOORS", "CLOSED", "Aircraft doors"),

("BEACON", "ON", "Anti-collision light"),

("PARKING BRAKE", "SET", "Parking brake"),

("PUSHBACK", "CLEAR", "Pushback clearance")

],



"ENGINE START": [

("ENGINE 2", "START", "PW127 engine start"),

("ENGINE 1", "START", "PW127 engine start"),

("ENGINE PARAMETERS", "CHECK", "Engine indications"),

("GENERATORS", "ON", "Electrical generators")

],



"AFTER START": [

("BLEEDS", "SET", "Pneumatic system"),

("ANTI-ICE", "AS REQUIRED", "Ice protection"),

("FLIGHT CONTROLS", "CHECK", "Flight controls"),

("FLAPS", "SET", "Takeoff configuration")

],



"TAXI": [

("BRAKES", "CHECK", "Brake system"),

("INSTRUMENTS", "CHECK", "Flight instruments"),

("LIGHTS", "AS REQUIRED", "Exterior lights")

],



"BEFORE TAKEOFF": [

("FLAPS", "SET", "Takeoff configuration"),

("POWER LEVERS", "SET", "Engine power"),

("TAKEOFF WARNING", "TEST", "Warning system"),

("CABIN", "READY", "Cabin ready")

],



"AFTER TAKEOFF": [

("GEAR", "UP", "Landing gear"),

("FLAPS", "RETRACT", "Flap retraction")

],



"CLIMB": [

("ENGINE PARAMETERS", "MONITOR", "Engine monitoring"),

("PRESSURIZATION", "CHECK", "Cabin pressure")

],



"CRUISE": [

("FUEL", "MONITOR", "Fuel monitoring"),

("SYSTEMS", "CHECK", "Aircraft systems")

],



"DESCENT": [

("LANDING DATA", "SET", "Landing performance"),

("APPROACH", "BRIEF", "Approach briefing")

],



"APPROACH": [

("GEAR", "DOWN", "Landing gear"),

("FLAPS", "SET", "Landing configuration"),

("CABIN", "READY", "Cabin preparation")

],



"LANDING": [

("REVERSE", "AS REQUIRED", "Reverse thrust"),

("BRAKES", "APPLY", "Wheel brakes")

],



"AFTER LANDING": [

("FLAPS", "UP", "Flap retraction"),

("APU", "START", "Auxiliary Power Unit")

],



"PARKING / SHUTDOWN": [

("PARKING BRAKE", "SET", "Parking brake"),

("ENGINES", "OFF", "Engine shutdown"),

("BATTERY", "OFF", "Electrical system")

]

},"Embraer E190-E2": {


"COCKPIT PREPARATION": [

("BATTERY", "ON", "Aircraft electrical system"),

("EXT PWR", "ON", "External power"),

("APU", "START / ON", "Auxiliary Power Unit"),

("IRS", "ALIGN", "Inertial Reference System"),

("FMS", "SET", "Flight management system"),

("FUEL", "CHECK", "Fuel quantity"),

("HYDRAULICS", "CHECK", "Hydraulic system")

],



"BEFORE START": [

("DOORS", "CLOSED", "Aircraft doors"),

("BEACON", "ON", "Anti-collision light"),

("PARKING BRAKE", "SET", "Parking brake"),

("PUSHBACK", "CLEAR", "Pushback clearance")

],



"ENGINE START": [

("ENGINE 2", "START", "PW1900G engine start"),

("ENGINE 1", "START", "PW1900G engine start"),

("ENGINE PARAMETERS", "CHECK", "Engine indications"),

("GENERATORS", "ON", "Electrical generators")

],



"AFTER START": [

("PACKS", "ON", "Air conditioning"),

("BLEEDS", "SET", "Pneumatic system"),

("ANTI-ICE", "AS REQUIRED", "Ice protection"),

("FLIGHT CONTROLS", "CHECK", "Flight controls"),

("FLAPS", "SET", "Takeoff configuration")

],



"TAXI": [

("BRAKES", "CHECK", "Brake system"),

("FLIGHT INSTRUMENTS", "CHECK", "Flight instruments"),

("TAKEOFF BRIEFING", "COMPLETE", "Crew briefing"),

("LIGHTS", "AS REQUIRED", "Exterior lights")

],



"BEFORE TAKEOFF": [

("FLAPS", "SET", "Takeoff configuration"),

("SPOILERS", "ARM", "Ground spoilers"),

("AUTOTHROTTLE", "ARM", "Automatic thrust"),

("TCAS", "TA/RA", "Traffic avoidance"),

("CABIN", "READY", "Cabin ready")

],



"AFTER TAKEOFF": [

("GEAR", "UP", "Landing gear"),

("FLAPS", "RETRACT", "Flap retraction"),

("CLIMB POWER", "SET", "Engine thrust")

],



"CLIMB": [

("ENGINE PARAMETERS", "MONITOR", "Engine monitoring"),

("PRESSURIZATION", "CHECK", "Cabin pressure"),

("ANTI-ICE", "AS REQUIRED", "Ice protection")

],



"CRUISE": [

("FUEL", "MONITOR", "Fuel monitoring"),

("SYSTEMS", "CHECK", "Aircraft systems"),

("WEATHER RADAR", "SET", "Weather radar")

],



"DESCENT": [

("DESCENT BRIEFING", "COMPLETE", "Approach briefing"),

("LANDING DATA", "SET", "Landing performance"),

("AUTOBRAKE", "SET", "Automatic braking")

],



"APPROACH": [

("LANDING GEAR", "DOWN", "Landing gear"),

("FLAPS", "SET", "Landing configuration"),

("LANDING LIGHTS", "ON", "Landing lights"),

("CABIN", "READY", "Cabin preparation")

],



"LANDING": [

("REVERSE THRUST", "AS REQUIRED", "Reverse thrust"),

("BRAKES", "APPLY", "Wheel brakes"),

("SPOILERS", "CHECK", "Ground spoilers")

],



"AFTER LANDING": [

("FLAPS", "UP", "Flap retraction"),

("SPOILERS", "DISARM", "Spoilers"),

("APU", "START", "Auxiliary Power Unit"),

("LIGHTS", "AS REQUIRED", "Taxi lights")

],



"PARKING / SHUTDOWN": [

("PARKING BRAKE", "SET", "Parking brake"),

("ENGINES", "OFF", "Engine shutdown"),

("FUEL PUMPS", "OFF", "Fuel system"),

("BEACON", "OFF", "Anti-collision light"),

("BATTERY", "OFF", "Electrical system")

]


}



}



# =========================
# ОСНОВНОЙ КЛАСС
# =========================


class SkyBook:


    def __init__(self, page):

        self.page = page

        self.page.title = "SkyBook EFB"

        self.page.theme_mode = ft.ThemeMode.DARK

        self.page.bgcolor = "#101820"

        self.page.padding = 20

        self.page.window.width = 1200

        self.page.window.height = 800


        self.current_manufacturer = None

        self.current_aircraft = None


        self.show_manufacturers()

    def save_checklist_state(self):

        import json
        import os


        state = {}


        for key, checkbox in self.check_vars.items():

            state[key] = checkbox.value


        os.makedirs(
            "data",
            exist_ok=True
        )


        with open(
            "data/checklists_state.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                state,
                f,
                ensure_ascii=False,
                indent=4
            )



    def load_checklist_state(self):

        import json
        import os


        filename = "data/checklists_state.json"


        if not os.path.exists(filename):

            return



        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as f:

            state = json.load(f)



        for key, checkbox in self.check_vars.items():

            if key in state:

                checkbox.value = state[key]

    def clear_page(self):

        self.page.controls.clear()



    def refresh(self):

        self.page.update()



    def title(self, text):

        return ft.Text(

            text,

            size=30,

            weight=ft.FontWeight.BOLD

        )


    def back_to_aircraft(self):

        manufacturer = getattr(
            self,
            "current_manufacturer",
            None
        )


        if manufacturer:

            self.show_aircraft(
                manufacturer
            )

        else:

            self.show_manufacturers()

    def back_button(self, action):

        return ft.IconButton(

            icon=ft.Icons.ARROW_BACK,

            on_click=action

        )
    # =========================
    # ЭКРАН ПРОИЗВОДИТЕЛЕЙ
    # =========================


    def show_manufacturers(self, e=None):


        self.clear_page()


        companies = [

            "Airbus",

            "Boeing",

            "Cessna",

            "ATR",

            "Embraer"

        ]


        cards = []


        for company in companies:


            cards.append(

                ft.Container(

                    width=260,

                    height=160,

                    bgcolor="#1B2631",

                    border_radius=20,

                    padding=20,


                    content=ft.Column(

                        [

                            ft.Text(

                                company,

                                size=26,

                                weight=ft.FontWeight.BOLD

                            ),


                            ft.Button(

                                content=ft.Text(

                                    "SELECT"

                                ),


                                on_click=lambda e, c=company:

                                self.show_aircraft(c)

                            )

                        ],


                        horizontal_alignment=

                        ft.CrossAxisAlignment.CENTER

                    )

                )

            )



        self.page.add(

            ft.Column(

                [

                    self.title(

                        "SkyBook EFB"

                    ),


                    ft.Text(

                        "Select manufacturer",

                        size=18

                    ),



                    ft.GridView(

                        expand=True,

                        max_extent=280,

                        spacing=20,

                        run_spacing=20,

                        controls=cards

                    )

                ],


                expand=True

            )

        )


        self.refresh()


        # ЭКРАН САМОЛЕТОВ


        def show_aircraft(self, manufacturer):

            self.current_manufacturer = manufacturer

            self.clear_page()

            cards = []

            for aircraft in aircrafts:

                if aircraft["manufacturer"] == manufacturer:
                    cards.append(

                        ft.Container(

                            width=300,

                            height=180,

                            bgcolor="#1B2631",

                            border_radius=20,

                            padding=20,

                            content=ft.Column(

                                [

                                    ft.Text(

                                        aircraft["model"],

                                        size=24,

                                        weight=

                                        ft.FontWeight.BOLD

                                    ),

                                    ft.Text(

                                        aircraft["engine"],

                                        size=16

                                    ),

                                    ft.Button(

                                        content=

                                        ft.Text(

                                            "OPEN CHECKLIST"

                                        ),

                                        on_click=

                                        lambda e, a=aircraft:

                                        self.open_checklist(a)

                                    )

                                ]

                            )

                        )

                    )

            self.page.add(

                ft.Column(

                    [

                        ft.Row(

                            [

                                self.back_button(

                                    self.show_manufacturers

                                ),

                                self.title(

                                    manufacturer

                                )

                            ]

                        ),

                        ft.GridView(

                            expand=True,

                            max_extent=320,

                            spacing=20,

                            run_spacing=20,

                            controls=cards

                        )

                    ],

                    expand=True

                )

            )

            self.refresh()

    # ЭКРАН ЧЕК-ЛИСТА


    def open_checklist(self, aircraft):

        if isinstance(aircraft, dict):
            aircraft = aircraft.get(
                "name",
                aircraft.get(
                    "model",
                    ""
                )
            )

        self.current_aircraft = aircraft

        data = checklists.get(aircraft, {})

        if not data:

            aliases = {

                "737 MAX 8": "Boeing 737 MAX 8",

                "777-300ER": "Boeing 777-300ER",

                "E190-E2": "Embraer E190-E2",

            }

            if aircraft in aliases:
                data = checklists.get(
                    aliases[aircraft],
                    {}
                )

        if not data:
            self.page.controls.clear()

            self.page.add(
                ft.Column(
                    [
                        ft.Text(
                            "Checklist not found",
                            size=24
                        ),

                        ft.Button(
                            content="← Back",
                            on_click=lambda e: self.back_to_aircraft()
                        )
                    ]
                )
            )

            self.page.update()
            return

        self.check_vars = {}
        self.load_checklist_state()

        self.page.controls.clear()

        title = ft.Text(
            aircraft,
            size=28,
            weight=ft.FontWeight.BOLD
        )

        progress_text = ft.Text(
            "Progress: 0%",
            size=18
        )

        checklist_column = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )

        def update_progress():

            total = len(self.check_vars)

            if total == 0:
                progress_text.value = "Progress: 0%"
                self.page.update()
                return

            done = 0

            for item in self.check_vars.values():

                if item.value:
                    done += 1

            percent = int(done / total * 100)

            progress_text.value = (
                f"Progress: {percent}% "
                f"({done}/{total})"
            )

            self.page.update()

        for stage, items in data.items():

            stage_title = ft.Text(
                stage,
                size=20,
                weight=ft.FontWeight.BOLD
            )

            stage_items = ft.Column()

            for name, action, description in items:
                checkbox = ft.Checkbox()

                key = f"{stage}_{name}"

                self.check_vars[key] = checkbox

                def checkbox_changed(e):
                    self.save_checklist_state()

                    update_progress()

                checkbox.on_change = checkbox_changed

                row = ft.Row(

                    [

                        checkbox,

                        ft.Column(

                            [

                                ft.Text(
                                    name,
                                    weight=ft.FontWeight.BOLD
                                ),

                                ft.Text(
                                    action,
                                    size=14
                                ),

                                ft.Text(
                                    description,
                                    size=12
                                )

                            ],

                            expand=True

                        )

                    ]

                )

                stage_items.controls.append(row)

            section = ft.Column(

                controls=[
                    stage_title,
                    stage_items
                ]

            )

            checklist_column.controls.append(section)
        self.load_checklist_state()
        back_button = ft.Button(

            content="← Back",

            on_click=lambda e: self.back_to_aircraft()

        )

        self.page.add(

            ft.Column(

                [

                    ft.Row(

                        [

                            back_button,

                            title

                        ]

                    ),

                    progress_text,

                    checklist_column

                ],

                expand=True

            )

        )

        self.page.update()

        def checklist_back(self):

            self.show_aircrafts()

        def save_checklist_state(self):

            import json
            import os

            state = {}

            for key, checkbox in self.check_vars.items():
                state[key] = checkbox.value

            os.makedirs(
                "data",
                exist_ok=True
            )

            with open(
                    "data/checklists_state.json",
                    "w",
                    encoding="utf-8"
            ) as f:
                json.dump(
                    state,
                    f,
                    ensure_ascii=False,
                    indent=4
                )

        def load_checklist_state(self):

            import json
            import os

            filename = "data/checklists_state.json"

            if not os.path.exists(filename):
                return

            with open(
                    filename,
                    "r",
                    encoding="utf-8"
            ) as f:

                state = json.load(f)

            for key, checkbox in self.check_vars.items():

                if key in state:
                    checkbox.value = state[key]

        def checklist_back(self):

            self.show_aircrafts()

    # ЭКРАН САМОЛЕТОВ



    def show_aircraft(self, manufacturer):
        self.current_manufacturer = manufacturer

        self.current_manufacturer = manufacturer


        self.clear_page()


        cards = []


        for aircraft in aircrafts:


            if aircraft["manufacturer"] == manufacturer:


                cards.append(

                    ft.Container(

                        bgcolor="#1B2631",

                        border_radius=20,

                        padding=20,


                        content=ft.Column(

                            [

                                ft.Text(

                                    aircraft["model"],

                                    size=24,

                                    weight=ft.FontWeight.BOLD

                                ),


                                ft.Text(

                                    aircraft["engine"],

                                    size=16

                                ),


                                ft.Button(

                                    content=ft.Text(

                                        "OPEN CHECKLIST"

                                    ),


                                    on_click=lambda e, a=aircraft:

                                    self.open_checklist(a)

                                )

                            ]

                        )

                    )

                )



        self.page.add(

            ft.Column(

                [

                    ft.Row(

                        [

                            self.back_button(

                                self.show_manufacturers

                            ),


                            self.title(

                                manufacturer

                            )

                        ]

                    ),



                    ft.GridView(

                        expand=True,

                        max_extent=320,

                        spacing=20,

                        controls=cards

                    )

                ],

                expand=True

            )

        )


        self.refresh()

# ЗАПУСК ПРИЛОЖЕНИЯ



def main(page: ft.Page):

    SkyBook(page)



if __name__ == "__main__":

    ft.run(main)    