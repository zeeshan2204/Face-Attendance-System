import os
import pandas as pd
from flask import Flask, jsonify, send_file
from datetime import datetime

app = Flask(__name__)
ATTENDANCE_CSV = 'attendance.csv'


def get_df():
    if not os.path.exists(ATTENDANCE_CSV):
        return pd.DataFrame(columns=['Name', 'Date', 'Time', 'Status'])
    try:
        return pd.read_csv(ATTENDANCE_CSV)
    except:
        return pd.DataFrame(columns=['Name', 'Date', 'Time', 'Status'])


@app.route('/')
def home():
    return send_file(os.path.join(os.path.dirname(__file__), 'dashboard.html'))


@app.route('/api/attendance')
def get_attendance():
    df = get_df()
    today = datetime.now().strftime('%Y-%m-%d')

    total = len(df)
    present_today = len(df[df['Date'] == today]) if total > 0 else 0

    records = df.sort_values(['Date', 'Time'], ascending=[False, False]).to_dict('records')

    return jsonify({
        'total': total,
        'present_today': present_today,
        'today': today,
        'records': records,
        'persons': list(df['Name'].unique()) if total > 0 else []
    })


@app.route('/api/stats')
def get_stats():
    df = get_df()
    if df.empty:
        return jsonify({'labels': [], 'counts': []})

    counts = df['Name'].value_counts()

    return jsonify({
        'labels': list(counts.index),
        'counts': list(counts.values)
    })


if __name__ == '__main__':
    print("Dashboard: http://127.0.0.1:5000")
    app.run(debug=True)