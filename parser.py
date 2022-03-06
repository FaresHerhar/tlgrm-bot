import telegram


class TelegramParser:
    """ Telegram Parser class.
    
    A class containg methods that allows to parse data to a telegram chat,
    channel using a telegram bot.

    Attributes:
        _tlgrm_bot: A protectd Telegram Bot agent, that allows us to parse data.
        _channel_id: A protectd Telegram Channel ID, that allows us to
                     to push messages to the specific channel.
    """

    def __init__(self, TLGRM_BOT_TOKEN: str, TLGRM_CHAT_ID: str) -> None:
        """Constructor.
        
        Intitiate a telegram bot connection, and a the channel.
        """
        # Authenticate
        self._tlgrm_bot = telegram.Bot(token=TLGRM_BOT_TOKEN)
        self._channel_id = TLGRM_CHAT_ID

    def send_message(self, tlgrm_message: str, parse_mode: str = 'HTML') -> None:
        """ Push messages to Telegram..

        Push messages to a specific Telegram Channel, using the telegram bot id,
        and the channel id, while specifying the Parse mode.

        Args:
        tlgrm_message (str):
            The message to send.
        parse_mode (str):
            The parse mode, is either in HTML (by default), or MARKDOWN.
        
        Returns:
            None
        """
        # Check this pase mode, HTML by default
        if parse_mode == 'MARKDOWN':
            self._tlgrm_bot.send_message(chat_id=self._channel_id, text=tlgrm_message,
                                    parse_mode=telegram.ParseMode.MARKDOWN_V2)

        self._tlgrm_bot.send_message(chat_id=self._channel_id, text=tlgrm_message,
                                    parse_mode=telegram.ParseMode.HTML)
