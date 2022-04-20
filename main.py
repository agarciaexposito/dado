def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

def on_gesture_shake():
    radio.send_number(randint(1, 6))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

radio.set_group(1)