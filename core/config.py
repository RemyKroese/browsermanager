import yaml


class Config:
    def __init__(self, config_path='config.yaml'):
        self.config_path = config_path
        self.config = self.read()

    def write(self, config):
        with open(self.config_path, 'w') as f:
            yaml.dump(config, f, sort_keys=False, default_flow_style=False, indent=2)

    def read(self):
        try:
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            config = {
                'windows': [
                    {
                        'name': 'window_1',
                        'run_on_startup': True,
                        'monitor': 1,
                        'urls': ['https://github.com/RemyKroese/browsermanager#readme']
                    }],
            }
            self.write(config)
            return config
