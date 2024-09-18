import json, os

# Change the file directory to where you have saved Telescope-Simulator/Resources
# CONFIG_FILE = os.path.join("Resources", "config.json")
CONFIG_FILE = os.path.join("c:/Users/User/Desktop/Code/Telescope-Simulator/Resources", "config.json")

class Config:
    def __init__(self, config_file=CONFIG_FILE):
        self.config_file = config_file
        self._data = self._load_config()
        
    def _load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading configuration: {e}")
            return {}
    
    def get(self, key, default=None):

        return self._data.get(key, default) # Get a configuration value by key.
    
    def reload(self):
        self._data = self._load_config() # Reload the configuration from the file.
    
    def update(self, key, value):
        # Update a specific configuration value and save to the file.
        self._data[key] = value
        self._save_config()
    
    def _save_config(self):
        # Save the current configuration data to the file.
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self._data, file, indent=4)
        except IOError as e:
            print(f"Error saving configuration: {e}")
    
    def validate(self):
        # Validate the configuration data.
        required_keys = ['latitude', 'longitude', 'elevation', 'time_to_wait', 'altitude_limits', 'azimuth_limits']
        missing_keys = [key for key in required_keys if key not in self._data]
        if missing_keys:
            print(f"Missing configuration keys: {missing_keys}")
            return False
        return True

config = Config() # Instantiate a single Config object