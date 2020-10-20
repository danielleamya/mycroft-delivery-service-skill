from mycroft import MycroftSkill, intent_file_handler


class MycroftDeliveryService(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('service.delivery.mycroft.intent')
    def handle_service_delivery_mycroft(self, message):
        self.speak_dialog('service.delivery.mycroft')


def create_skill():
    return MycroftDeliveryService()

