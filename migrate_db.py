import os
import django
import dj_database_url
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soluserv.settings')
django.setup()

from django.conf import settings

def migrate_data():
    print("Starting database migration from SQLite to PostgreSQL...")
    
    sqlite_db = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
    
    postgres_db = dj_database_url.parse(os.environ.get('DATABASE_URL'))
    
    settings.DATABASES = {
        'default': sqlite_db,
        'postgres': postgres_db
    }
    
    print("\n1. Dumping data from SQLite database...")
    call_command('dumpdata', '--database=default', '--natural-foreign', '--natural-primary', 
                 '--exclude=contenttypes', '--exclude=auth.permission', 
                 '--indent=2', '--output=data_dump.json')
    print("   ✓ Data dumped to data_dump.json")
    
    print("\n2. Switching to PostgreSQL database...")
    settings.DATABASES = {
        'default': postgres_db
    }
    
    print("\n3. Running migrations on PostgreSQL...")
    call_command('migrate', '--database=default', '--run-syncdb')
    print("   ✓ Migrations completed")
    
    print("\n4. Loading data into PostgreSQL database...")
    call_command('loaddata', 'data_dump.json', '--database=default')
    print("   ✓ Data loaded successfully")
    
    print("\n✅ Migration completed successfully!")
    print("\nNext steps:")
    print("1. Verify the data in your PostgreSQL database")
    print("2. Update settings.py to use DATABASE_URL permanently")
    print("3. Delete data_dump.json if no longer needed")

if __name__ == '__main__':
    try:
        migrate_data()
    except Exception as e:
        print(f"\n❌ Error during migration: {e}")
        print("\nPlease ensure:")
        print("- DATABASE_URL environment variable is set correctly")
        print("- PostgreSQL server is running and accessible")
        print("- Database credentials are correct")
