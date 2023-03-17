from ampalibe.ui import QuickReply, Payload


class BackAndMenuButton:
    def __init__(self, payload=None, title="Iverina"):
        self.title = title
        self.payload = payload

    @property
    def toQuickreply(self):
        return (
            [
                QuickReply(
                    title=self.title,
                    payload=self.payload,
                    image_url="https://img.icons8.com/ios-filled/100/008080/circled-left-2.png",
                ),
            ]
            if self.payload
            else []
        ) + [
            QuickReply(
                title="Menu",
                payload=Payload("/"),
                image_url="https://img.icons8.com/ios-glyphs/30/008080/menu-rounded.png",
            ),
        ]
