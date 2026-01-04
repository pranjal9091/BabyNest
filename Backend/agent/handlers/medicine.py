from db.db import open_db

def handle(query, user_context):
    db = open_db()
    try:
        
        name = "Folic Acid"
        dose = "1 tablet"
        time = "08:00"
        week = user_context.get('week_number', 1)

        db.execute(
            'INSERT INTO weekly_medicine (week_number, name, dose, time) VALUES (?, ?, ?, ?)',
            (week, name, dose, time)
        )
        db.commit()
        return f"Logged {name} for week {week}."
    except Exception as e:
        return f"Error: {str(e)}"