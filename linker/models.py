from django.db import models

# Create your models here.
MAX_WEIGHT = 4
class ProposedLink(models.Model):
    assigned_user = models.CharField(max_length=80, default="no user")
    synset1id = models.IntegerField()
    synset1def = models.TextField(default="no definition")
    synset1pos = models.CharField(max_length=1, default="n")
    synset1words = models.CharField(max_length=200, default="no_words")
    synset2id = models.IntegerField()
    synset2def = models.TextField(default="no definition")
    synset2pos = models.CharField(max_length=1, default="n")
    synset2words = models.CharField(max_length=200, default="no_words")
    link_weight = models.PositiveIntegerField(default=0)

    def synset1(self):
        return {
            "id": self.synset1id,
            "def": self.synset1def,
            "pos": self.synset1pos,
            "words": [w.replace("_", " ") for w in self.synset1words.split()]
        }

    def synset2(self):
        return {
            "id": self.synset2id,
            "def": self.synset2def,
            "pos": self.synset2pos,
            "words": [w.replace("_", " ") for w in self.synset2words.split()]
        }

    def assign_weight(self, weight):
        self.link_weight = weight
        self.save()
