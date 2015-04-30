#!/usr/bin/env python
import wx

# Create a new app, don't redirect stdout/stderr to a window.
app = wx.App(False)
# A Frame is a top-level window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)     # Show the frame.
app.MainLoop()
