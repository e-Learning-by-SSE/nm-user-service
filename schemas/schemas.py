from ma import ma
from models.entities    import User, LearningProfile, SkillProfile


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
class LearningProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LearningProfile
        load_instance = True
class SkillProfileSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SkillProfile
        load_instance = True