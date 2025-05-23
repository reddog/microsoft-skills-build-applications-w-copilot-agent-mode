import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://legendary-broccoli-jr7qww5jwfp4w5-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Activities</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Type</th>
              <th>Duration (minutes)</th>
            </tr>
          </thead>
          <tbody>
            {activities.map(activity => (
              <tr key={activity.id}>
                <td>{activity.type}</td>
                <td>{activity.duration}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Activities;
