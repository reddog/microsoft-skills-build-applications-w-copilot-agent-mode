from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thunder God', age=25),
            User(email='metalgeek@mhigh.edu', name='Metal Geek', age=22),
            User(email='zerocool@mhigh.edu', name='Zero Cool', age=20),
            User(email='crashoverride@hmhigh.edu', name='Crash Override', age=23),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token', age=21),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team = Team(name='Blue Team', members=[user.email for user in users])
        team.save()

        # Create activities
        activities = [
            Activity(user=users[0].email, type='Cycling', duration=60),
            Activity(user=users[1].email, type='Crossfit', duration=120),
            Activity(user=users[2].email, type='Running', duration=90),
            Activity(user=users[3].email, type='Strength', duration=30),
            Activity(user=users[4].email, type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team='Blue Team', points=100),
            Leaderboard(team='Blue Team', points=90),
            Leaderboard(team='Blue Team', points=95),
            Leaderboard(team='Blue Team', points=85),
            Leaderboard(team='Blue Team', points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
