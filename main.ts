radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
})
input.onGesture(Gesture.Shake, function () {
    radio.sendNumber(randint(1, 6))
})
radio.setGroup(1)
