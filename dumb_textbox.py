#
# A rudimentary text box stimulus for PsychoPy experiments
# Author: Meng Du
# May 2017
#

from psychopy import visual, core, event

# TODO overflow control? try TextBox?


class DumbTextbox:
    def __init__(self, window, width, height, pos=(0, 0), bg_color='white', text_color='black', line_height=0.05,
                 padding=0.01, other_stim=(), **kwargs):
        """
        DumbTextbox draws itself right after it's created, and other psychopy.visual stimuli could be drawn together
        with it.
        DumbTextbox accepts all input parameters that psychopy.visual.TextStim accepts
        Usage:
            textbox = DumbTextbox(window=win, width=1, height=1)
            while True:
                response, rt = textbox.wait_key()
                if response[-1] == '\n':  # or other conditions when you want to end the response
                    break
        :param padding: (float) distance between text and the border of the text box
        """
        self._key_mapping = {
            'grave': ('`', '~'),
            'minus': ('-', '_'),
            'equal': ('=', '+'),
            'bracketleft': ('[', '{'),
            'bracketright': (']', '}'),
            'semicolon': (';', ':'),
            'apostrophe': ('\'', '"'),
            'comma': (',', '<'),
            'period': ('.', '>'),
            'slash': ('/', '?'),
            'backslash': ('\\', '|'),
            'return': '\n',
            'space': ' ',
            '1': '!',
            '2': '@',
            '3': '#',
            '4': '$',
            '5': '%',
            '6': '^',
            '7': '&',
            '8': '*',
            '9': '(',
            '0': ')',
        }
        self.window = window
        self.other_stim = other_stim
        self.text = ''
        text_pos = (pos[0] - float(width) / 2 + padding, pos[1] + float(height) / 2 - padding)
        wrap_width = width - padding * 2
        self.text_stim = visual.TextStim(self.window, self.text, color=text_color, pos=text_pos, height=line_height,
                                         alignHoriz='left', alignVert='top', wrapWidth=wrap_width, **kwargs)
        self.background = visual.Rect(window, width=width, height=height, pos=pos, fillColor=bg_color)
        self.draw()
        self.timer = core.Clock()

    def draw(self):
        self.background.draw()
        for stim in self.other_stim:
            if stim is not None:  # skipping "None"
                stim.draw()
        self.text_stim.draw()
        self.window.flip()

    def update(self, key):
        """
        :param key: a tuple containing information about the key pressed, as returned by psychopy.event.waitKeys where
                    modifiers=True
        """
        text_changed = True
        key_name = key[0]
        modifiers = key[1]
        if len(key_name) == 1:
            if key_name.isalpha():
                char = key_name.upper() if modifiers['shift'] or modifiers['capslock'] else key_name
            else:
                char = self._key_mapping[key_name] if modifiers['shift'] else key_name
            self.text += char
        elif key_name in self._key_mapping:
            if isinstance(self._key_mapping[key_name], tuple):
                self.text += self._key_mapping[key_name][1] if modifiers['shift'] else self._key_mapping[key_name][0]
            else:
                self.text += self._key_mapping[key_name]
        elif key_name == 'backspace':
            self.text = self.text[:-1]
        else:
            text_changed = False

        if text_changed:
            self.text_stim.setText(self.text)
            self.draw()

    def add_other_stim(self, other_stim):
        """
        :param other_stim: a psychopy visual stimulus or a list of them 
        """
        if isinstance(other_stim, visual.BaseVisualStim):
            self.other_stim.append(visual.BaseVisualStim)
        else:
            self.other_stim += other_stim
        self.draw()

    def wait_key(self):
        """
        :return: all input text, reaction time in seconds, and a information tuple about the last key pressed
                ('key_name', {'modifier_names': True/False})
        """
        key = event.waitKeys(modifiers=True, timeStamped=self.timer)[0]
        self.update(key)
        return self.text, key[2], (key[0], key[1])


if __name__ == '__main__':
    win = visual.Window(fullscr=False)
    textbox = DumbTextbox(window=win, width=1.5, height=1, pos=(0, -0.2))
    while True:
        response, rt, last_key = textbox.wait_key()
        if last_key[0] == 'return' and last_key[1]['command']:
            break
