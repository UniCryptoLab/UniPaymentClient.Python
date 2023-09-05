# coding: utf-8


import json
import time

class JSONifiedState:
    """Store the state of testing.

    All state is an in-memory dict.
    Simple load/store massive JSON on start up.
    """

    def __init__(self):
        self.data = None
        self.fname = "test.json"
        self.last_save = 0

    def reset(self):
        """Create initial state of nothing scanned."""
        self.data = {
            "withdrawal_id": "",
            "invoice_id": "",
        }

    def restore(self):
        """Restore the testing state from a file."""
        try:
            self.data = json.load(open(self.fname, "rt"))
        except (IOError, json.decoder.JSONDecodeError):
            self.reset()

    def save(self):
        """Save everything we have so far in a file."""
        with open(self.fname, "wt") as f:
            json.dump(self.data, f)
        self.last_save = time.time()

    def on_create_withdraw(self, withdrawal):
        self.data['withdrawal_id'] = withdrawal.id
        self.save()
