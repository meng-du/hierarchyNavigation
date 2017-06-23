# Experimental parameters
SERIAL_PORT = '/dev/tty.UC-232AC1'
BAUD_RATE = 19200  # TODO
NUM_PRACTICE_TRIALS = 10
MAX_NUM_TRIALS = 5  # -> just to test the program
NUM_RUNS = 4  # TODO
NUM_TRIALS_PER_RUN = 24
NUM_FACES = 9
NUM_OPTIONS = 4
DIRECTIONS = ('D', 'U')
ANCHOR_INDEXES = (2, 3, 4, 5, 6)
MIN_DISTANCE = 2
MAX_DISTANCE = 4
RESPONSE_KEYS = ('1', '2', '3', '4')  # TODO
# Colors
DIR_COLORS = ('#f0ad4e', '#5bc0de')
COLOR_NAMES = {'#f0ad4e': 'Orange', '#5bc0de': 'Blue'}
RED = '#ff0000'
GREEN = '#84ff84'
BLACK = '#000000'
# Paths
IMG_FOLDER = 'img/'
DATA_FOLDER = 'data/'
LOG_FOLDER = 'log/'
DESIGN_FILENAME = 'test_designs.pkl'
# Positions
TOP_INSTR_POS = (0, 0.85)
IMG_DIST = 415  # horizontal or vertical distance from images to the middle of screen, in pixels
# Times
FACE_TRIGGER = 1
FIXATION_TIME = 0.5
NUMBER_TRIGGER = 1
BLANK_TRIGGER = 6
SELECTION_TIME = 1.5
FEEDBACK_TRIGGER = 1  # TODO should be 2?
# Strings
FEEDBACK_RIGHT = 'Correct!'
FEEDBACK_WRONG = 'Wrong.'
FEEDBACK_SLOW = 'Too slow. Please respond faster.'
# Instructions
INSTR_0 = ['Welcome!\n\nIn this task, you will be asked about the organization you\'ve learned about.',
           'Each trial will begin with a "reference" face.\n\nA few seconds later, a number will appear.',
           'Your job is to figure out who is that number of steps MORE or LESS powerful than the "reference" face ' +
           'in the organization.\n\nThe color of the number indicates whether you need to figure out who is that ' +
           'number of steps MORE or LESS powerful than the reference face.']
INSTR_COLOR = '{down_color} numbers mean figure out who is that number of steps LESS powerful than the reference ' + \
              'face in the organization.\n\n{up_color} numbers mean figure out who is that number of steps MORE ' + \
              'powerful than the reference face in the organization.'
INSTR_1 = 'You\'ll have a few seconds to figure out your response. \n\nAfter that, 4 faces will be briefly ' + \
          'presented as possible response options. They won\'t be on the screen for very long, so it\'s important ' + \
          'to figure out your response before they appear so that you can respond in time.'
INSTR_2 = 'When the response options are presented, they\'ll look like this:'
INSTR_3 = 'Press the Q, W, A or S key to select a given face, like this:'
INSTR_PRACTICE = 'We\'ll start by doing some practice trials.\n\nIn these practice trials, you\'ll be reminded of ' + \
                 'the meaning of the numbers\' colors before each trial (but this won\'t happen in the main task).'
INSTR_4 = 'You\'ve completed all of the practice trials.\n\nNow we\'ll begin the task.'
INSTR_END = 'The experiment is complete!\nThank you for participating!'
