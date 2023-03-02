from db import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    skill_id = db.Column(db.Integer, db.ForeignKey("skillProfile.id"))
    learningProfile_id = db.Column(db.Integer, db.ForeignKey("learningProfile.id"))
    def __str__(self):
        return 'ItemModel(id=%d,name=%s, skill_id=%d,learningProfile_id=%d )' % (self.id,self.name, self.skill_id, self.learningProfile_id)

    def json(self):
        return {'id':self.id,'name': self.name, 'skill_id':self.skill_id,'learningProfile_id':self.learningProfile_id}
    
class LearningProfile(db.Model):
    __tablename__ = "learningProfile"

    id = db.Column(db.Integer, primary_key=True)
    semanticDensity = db.Column(db.Integer)
    semanticGravity = db.Column(db.Integer)
    mediaType = db.Column(db.String(80), nullable=False)
    language = db.Column(db.String(80), nullable=False)
    processingTimePerUnit = db.Column(db.Integer)
    

    def __str__(self):
        return 'ItemModel(id=%d,semanticDensity=%d , semanticGravity=%d,mediaType=%s, language=%s, processingTimePerUnit=%s)' % (self.id,self.semanticDensity, self.semanticGravity, self.mediaType, self.language, self.processingTimePerUnit)

    def json(self):
        return {'id':self.id,'semanticDensity': self.semanticDensity, 'semanticGravity': self.semanticGravity, 'mediaType':self.mediaType,'language':self.language,'processingTimePerUnit':self.processingTimePerUnit}
    
class SkillProfile(db.Model):
    __tablename__ = "skillProfile"

    id = db.Column(db.Integer, primary_key=True)
    jobHistory = db.Column(db.String(200))
    professionalInterests = db.Column(db.String(200))
    
    

    def __str__(self):
        return 'ItemModel(id=%d,jobHistory=%s , professionalInterests=%s)' % (self.id,self.jobHistory, self.professionalInterests)

    def json(self):
        return {'id':self.id,'jobHistory': self.jobHistory, 'professionalInterests': self.professionalInterests}
    