import ffmpeg

from config import ConfigHandler


class AudioConverter:

    def __init__(self):
        self.config = None
        self.input_dir = ""
        self.output_dir = ""

    def setup(self, input_dir="", output_dir="", from_codec="", to_codec=""):
        if self.config is None:
            print("Loading config...")
            conf_handler = ConfigHandler()
            try:
                self.config = conf_handler.load_config()
                print("Config loaded.")
            except:
                print("Error loading config. Please check config.toml.")
                return
        elif (input_dir, output_dir, from_codec, to_codec != ""):
            print("Converter initialized..")
        else:
            print("Could not find necessary inputs for conversion. This should never happen.")

