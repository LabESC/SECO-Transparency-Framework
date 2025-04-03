from app import db
from models.enums import NavigationType

class CollectedData(db.Model):
    __tablename__ = 'collected_data'
    
    # Main Rows
    collected_data_id = db.Column(db.Integer, primary_key=True)
    seco_portal = db.Column(db.String(500), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    # Relationship with PerformedTask
    performed_tasks = db.relationship('PerformedTask',
                                    backref=db.backref('collected_data', lazy=True))
    
    # Relationship with DeveloperQuestionnaire
    developer_questionnaire = db.relationship('DeveloperQuestionnaire',
                                        backref=db.backref('collected_data', lazy=True, uselist=False),
                                        uselist=False)
    
    # Rlationship with Navigation
    navigation = db.relationship('Navigation',
                                backref=db.backref('collected_data', lazy=True, uselist=False),
                                uselist=False)

    # Foreign key to the evaluation table
    evaluation_id = db.Column(db.BigInteger, db.ForeignKey('evaluation.evaluation_id'), nullable=False) 

class Navigation(db.Model):
    __tablename__ = 'navigation'

    # Primary Key
    navigation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Main Rows
    action = db.Column(db.Enum(NavigationType), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    # Foreign key to the task table
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), nullable=False)

    # Foreign key to the collected data table
    collected_data_id = db.Column(db.Integer, db.ForeignKey('collected_data.collected_data_id'), nullable=False, unique=True)

