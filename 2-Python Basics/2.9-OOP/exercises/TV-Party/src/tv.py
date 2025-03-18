class TV:
    def __init__(self):
        """The constructor. Called when you instantiate a TV."""
        self.channel = 1
        self.volume_level = 1
        self.turned_on = False

    def turn_on(self):
        """Turns the TV on."""
        pass

    def turn_off(self):
        """Turns the TV off."""
        pass

    def channel_up(self):
        """Scrolls the channel up."""
        pass

    def channel_down(self):
        """Scrolls the channel down."""
        pass

    def set_channel(self, new_channel: int):
        """
        Sets the channel to the desired channel.

        :param int new_channel: The new channel
        """
        pass

    def volume_up(self):
        """Increases the volume."""
        pass

    def volume_down(self):
        """Decreases the volume."""
        pass

    def is_on(self):
        """Returns 'on' when the TV is on and otherwise 'off'."""
        if self.turned_on:
            return "on"
        return "off"
