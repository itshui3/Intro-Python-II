import os
import sys

def generate_pathing():

    paths = [

    os.path.abspath( os.path.dirname( __file__ ) + '/assets' ),
    os.path.abspath( os.path.dirname( __file__ ) + '/assets/entities' ),
    # os.path.abspath( os.path.dirname( __file__ ) + '/assets/resources' )

    ]

    for p in paths:
        sys.path.insert( 0, p )