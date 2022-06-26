class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'auth', 'contenttypes','account'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to user.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'user'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to user.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'user'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        print('allow_relation')
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print('allow_migrate')
        """
        Make sure the auth and contenttypes apps only appear in the
        'user' database.
        """
        if app_label in self.route_app_labels:
            return db == 'user'
        return None
    
import random

class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        return random.choice(['replica1', 'replica2'])

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return 'admin'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set = {'admin', 'replica1', 'replica2'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True