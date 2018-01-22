class Artisan:
    def __init__(self, **kwargs):
        self.slug = kwargs.get('slug')
        self.name = kwargs.get('name')
        self.portrait = kwargs.get('portrait')
        self.training = kwargs.get('training')
        self.skills = kwargs.get('skills')
