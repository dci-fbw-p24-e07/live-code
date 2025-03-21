""" 
Sample code for creating mixins. 
You are creating VoIP service that allows users to make calls 
but also send SMS's. The user will have to recharge their VoIP 
phone in order for them to access the calling and SMS services.
Define mixins for SMS and calling
"""


class TelephoneMixin:
    
    # Concrete methods
    def dial_number(self, number):
        return f"Calling: {number}"
    
    
class SMSMixin:
    
    def send_message(self, number, message):
        return f"To: {number}. \n Message: {message}"


class VoIPPhone(TelephoneMixin, SMSMixin):
    
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.airtime = 0
        
    def topup(self, amount):
        self.airtime += amount


phone_1 = VoIPPhone("+2579875323553")
print(phone_1.send_message("+679999876755", "Hey there buddy!"))