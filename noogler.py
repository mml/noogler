#!/usr/bin/env python2.6
from datetime import datetime
from dateutil.tz import *

class UntilCalc(object):
    """
    Pretty-prints the difference between the current time and a fixed point in
    time.
    """

    def __str__(self):
        return ' '.join(self.phrases)

    @property
    def phrases(self):
        """The phrases to be assembled in to a string representation."""
        return filter(None,
                      [self.context(), self.weeks(), self.days(), self.hm()])

    def weeks(self):
        """The 'weeks until/since' phrase."""
        count = self.diff.days / 7
        return '%d weeks' % count if count else None

    def days(self):
        """The 'days until/since' phrase."""
        count  = self.diff.days % 7
        return '%d days' % count if count else None

    def hm(self):
        """The HH:MM part."""
        return '%02d:%02d' % (self.diff.seconds/3600, self.diff.seconds%3600/60)

    def context(self):
        """The temporal positioning part."""
        return 't minus' if self.now < self.when else 't ='

    @property
    def diff(self):
        """The absolute difference between now and when."""
        if not hasattr(self, '_diff'): self._diff = abs(self.when - self.now)

        return self._diff

    @property
    def now(self):
        """Cache of the current time."""
        if not hasattr(self, '_now'): self._now = datetime.now(tzlocal())

        return self._now

    def __init__(self, when):
        """Constructs a new UntilCalc using the datetime when"""
        super(UntilCalc, self).__init__()
        self.when = when


if __name__ == '__main__':
    # 2010-06-07 0800 -0700
    START = datetime(2010, 6, 7, 8, 0, 0, tzinfo=tzstr('PST8PDT'))
    print UntilCalc(START)
