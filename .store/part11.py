w1 = window_about()  # about
w2 = window_update()  # update
w3 = window3()  # main1
# w4 = window4()  # main2
action1.triggered.connect(w1.activate)
action2.triggered.connect(w2.activate)
action3.triggered.connect(w3.activate)
# action4.triggered.connect(w4.activate)
# tray.activated.connect(w3.activate)
button_action.triggered.connect(w3.activate)
app.setStyleSheet(style_sheet)
app.exec()
