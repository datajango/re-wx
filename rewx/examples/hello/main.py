import wx
from rewx import create_element, wsx, render
from rewx.components import StaticText, Frame

if __name__ == '__main__':
    app = wx.App()
    element = create_element(Frame, {'title': 'My Cool Application', 'show': True}, children=[
        create_element(StaticText, {'label': 'Howdy, cool person!'})
    ])
    frame = render(element, None)
    app.MainLoop()