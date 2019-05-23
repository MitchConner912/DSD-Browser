class DSDCalls:

    def __init__(self, date, time, dur, type, cc, slot, calltype, group, rid, src):
        self.date = date
        self.time = time
        self.dur = dur
        self.type = type
        self.cc = cc
        self.slot = slot
        self.calltype = calltype
        self.group = group
        self.rid = rid
        self.src = src

    @property
    def call(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.date,
                                                self.time,
                                                self.dur,
                                                self.type,
                                                self.cc,
                                                self.slot,
                                                self.calltype,
                                                self.group,
                                                self.rid,
                                                self.src)