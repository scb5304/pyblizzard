class Follower:
    TEMPLAR = 'templar'
    SCOUNDREL = 'scoundrel'
    ENCHANTRESS = 'enchantress'

    def __init__(self, **kwargs):
        self.slug = kwargs.get('slug')
        self.name = kwargs.get('name')
        self.real_name = kwargs.get('realName')
        self.portrait = kwargs.get('portrait')
        self.skills = kwargs.get('skills')
