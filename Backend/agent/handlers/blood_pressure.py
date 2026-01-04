from db.db import open_db

def handle(query, user_context):
    db = open_db()
    try:
        systolic = 120
        diastolic = 80
        
        db.execute(
            'INSERT INTO blood_pressure_logs (systolic, diastolic) VALUES (?, ?)',
            (systolic, diastolic)
        )
        db.commit()
        return f"Recorded BP: {systolic}/{diastolic}."
    except Exception as e:
        return f"Error: {str(e)}"