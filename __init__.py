from mycroft import MycroftSkill, intent_file_handler


class Klikaan(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('klikaan.intent')
    def handle_klikaan(self, message):
        name = message.data.get('name')
        percent = message.data.get('percent')

        self.speak_dialog('klikaan', data={
            'name': name,
            'percent': percent
        })


def create_skill():
    return Klikaan()

