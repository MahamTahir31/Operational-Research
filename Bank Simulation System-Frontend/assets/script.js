// Customers script 

// Function to convert Day1.csv to HTML table
function csvToTable(csvData) {
    var lines = csvData.split('\n');
    var tableHTML = '<table>';
  
    // Create table rows
    for (var i = 0; i < lines.length; i++) {
      tableHTML += '<tr>';
      var rowData = lines[i].split(',');
  
      for (var j = 0; j < rowData.length; j++) {
        if (i === 0) {
          tableHTML += '<th>' + rowData[j] + '</th>'; // Use <th> for header row
        } else {
          tableHTML += '<td>' + rowData[j] + '</td>'; // Use <td> for data rows
        }
      }
  
      tableHTML += '</tr>';
    }
  
    tableHTML += '</table>';
    return tableHTML;
  }
  
  // Read "Day1.csv" file
  fetch('Day1.csv')
    .then(response => response.text())
    .then(data => {
      var csvTableContainer = document.getElementById('csvTableContainer');
      csvTableContainer.innerHTML = csvToTable(data);
      document.body.appendChild(csvTableContainer);
    })
    .catch(error => console.error('Error:', error));
// Function to convert Day2.csv to HTML table
function csvToTable(csvData) {
    var lines = csvData.split('\n');
    var tableHTML = '<table>';
  
    // Create table rows
    for (var i = 0; i < lines.length; i++) {
      tableHTML += '<tr>';
      var rowData = lines[i].split(',');
  
      for (var j = 0; j < rowData.length; j++) {
        if (i === 0) {
          tableHTML += '<th>' + rowData[j] + '</th>'; // Use <th> for header row
        } else {
          tableHTML += '<td>' + rowData[j] + '</td>'; // Use <td> for data rows
        }
      }
  
      tableHTML += '</tr>';
    }
  
    tableHTML += '</table>';
    return tableHTML;
  }
  
  // Read "Day2.csv" file
  fetch('Day2.csv')
    .then(response => response.text())
    .then(data => {
      var csvTableContainer = document.getElementById('csvTableContainer');
      csvTableContainer.innerHTML = csvToTable(data);
      document.body.appendChild(csvTableContainer);
    })
    .catch(error => console.error('Error:', error));
// Function to convert Day3.csv to HTML table
function csvToTable(csvData) {
    var lines = csvData.split('\n');
    var tableHTML = '<table>';
  
    // Create table rows
    for (var i = 0; i < lines.length; i++) {
      tableHTML += '<tr>';
      var rowData = lines[i].split(',');
  
      for (var j = 0; j < rowData.length; j++) {
        if (i === 0) {
          tableHTML += '<th>' + rowData[j] + '</th>'; // Use <th> for header row
        } else {
          tableHTML += '<td>' + rowData[j] + '</td>'; // Use <td> for data rows
        }
      }
  
      tableHTML += '</tr>';
    }
  
    tableHTML += '</table>';
    return tableHTML;
  }
  
  // Read "Day3.csv" file
  fetch('Day3.csv')
    .then(response => response.text())
    .then(data => {
      var csvTableContainer = document.getElementById('csvTableContainer');
      csvTableContainer.innerHTML = csvToTable(data);
      document.body.appendChild(csvTableContainer);
    })
    .catch(error => console.error('Error:', error));
  
// Customers script end